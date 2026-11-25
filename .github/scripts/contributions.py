"""Rewrites the upstream-contributions block of README.md from the GitHub search API."""
import json, os, re, urllib.parse, urllib.request

USER = "BiNeurale"
README = "README.md"
# Repos not worth showing (old coursework, unrelated reports).
EXCLUDE = {"chiragchander/MONOPOLY-project", "MetaMask/eth-phishing-detect"}
# Reports filed outside GitHub: (project, label, url, summary).
EXTERNAL_REPORTS = [
    ("Wine", "59803", "https://bugs.winehq.org/show_bug.cgi?id=59803",
     "WoW64 debugger break-in, reproducer + Windows 11 reference"),
    ("Wine", "60719", "https://bugs.winehq.org/show_bug.cgi?id=60719",
     "Schannel `DecryptMessage` ignores TLS `close_notify`"),
]
START, END = "<!-- contributions:start -->", "<!-- contributions:end -->"


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def repo_of(it):
    return it["repository_url"].split("/repos/")[1]


def search(q):
    url = "https://api.github.com/search/issues?per_page=100&sort=created&q=" + urllib.parse.quote(q)
    return [i for i in get(url)["items"] if repo_of(i) not in EXCLUDE]


_stars = {}
def stars(repo):
    if repo not in _stars:
        try:
            _stars[repo] = get("https://api.github.com/repos/" + repo)["stargazers_count"]
        except Exception:
            _stars[repo] = 0
    return _stars[repo]


def by_reach(items):
    # Biggest projects first, newest first within a project.
    return sorted(items, key=lambda i: (-stars(repo_of(i)), -i["number"]))


def line(it):
    # A closed-completed issue means upstream fixed what we reported.
    fixed = " ✅ fixed upstream" if it["state"] == "closed" and "pull_request" not in it else ""
    return f"- **{repo_of(it)}** [#{it['number']}]({it['html_url']}) — {it['title']}{fixed}"


prs = f"is:pr author:{USER} -user:{USER}"
merged = by_reach(search(prs + " is:merged"))
open_ = by_reach(search(prs + " is:open"))
pr_repos = {repo_of(i) for i in merged + open_}
# Issues are shown only where no PR of ours already tells the story, and never if declined.
issues = by_reach([i for i in search(f"is:issue author:{USER} -user:{USER}")
                   if repo_of(i) not in pr_repos
                   and (i["state"] == "open" or i.get("state_reason") == "completed")])

projects = pr_repos | {repo_of(i) for i in issues} | {p for p, *_ in EXTERNAL_REPORTS}
reports = len(issues) + len(EXTERNAL_REPORTS)
summary = (f"**{len(projects)} projects** · **{len(merged)}** merged · "
           f"**{len(open_)}** in review · **{reports}** bug reports")

parts = [summary, "", "**Merged**", "", *([*map(line, merged)] or ["- none yet"]), ""]
if open_:
    parts += ["**In review**", "", *map(line, open_), ""]
parts += ["**Bug reports**", "", *map(line, issues),
          *(f"- **{p}** [{n}]({u}) — {s}" for p, n, u, s in EXTERNAL_REPORTS), ""]
block = "\n".join([START, "", *parts, END])

text = open(README, encoding="utf-8").read()
new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
if new != text:
    open(README, "w", encoding="utf-8").write(new)
