"""Rewrites the upstream-contributions block of README.md from the GitHub search API."""
import json, os, re, urllib.parse, urllib.request

USER = "BiNeurale"
README = "README.md"
# Repos not worth showing (old coursework).
EXCLUDE = {"chiragchander/MONOPOLY-project"}
START, END = "<!-- contributions:start -->", "<!-- contributions:end -->"


def search(q):
    url = "https://api.github.com/search/issues?per_page=100&sort=created&q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req) as r:
        return json.load(r)["items"]


def line(it):
    repo = it["repository_url"].split("/repos/")[1]
    return f"- **{repo}** [#{it['number']}]({it['html_url']}) — {it['title']}"


base = f"is:pr author:{USER} -user:{USER}"
def keep(items):
    return [i for i in items if i["repository_url"].split("/repos/")[1] not in EXCLUDE]


merged = keep(search(base + " is:merged"))
open_ = keep(search(base + " is:open"))
parts = ["**Merged**", "", *(map(line, merged) or ["- none yet"]), ""]
if open_:
    parts += ["**In review**", "", *map(line, open_), ""]
block = "\n".join([START, "", *parts, END])

text = open(README, encoding="utf-8").read()
new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
if new != text:
    open(README, "w", encoding="utf-8").write(new)
