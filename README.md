### Hi, I'm Emanuele — [BiNeurale](https://github.com/BiNeurale)

Reverse engineer and Rust developer. I build small tools that fix real problems: signed-document
readers, OCR, CAD and 3D tooling, debugger plugins.
When I hit a bug in someone else's software, I isolate it, check it against the docs and against real
Windows or macOS, and send the fix upstream in the project's own style.

## Projects

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/BiNeurale/MiDas"><img src="https://raw.githubusercontent.com/BiNeurale/MiDas/main/docs/media/hero.png" alt="MiDas showing a signed PDF next to its signature verification panel"></a><br>
<b><a href="https://github.com/BiNeurale/MiDas">MiDas</a></b> · Rust<br>
Native Linux reader for signed <code>.p7m</code>, PDF, Markdown and office files, with local CAdES/PAdES verification against the EU trusted lists.
</td>
<td width="50%" valign="top">
<a href="https://github.com/BiNeurale/wariOCR"><img src="https://raw.githubusercontent.com/BiNeurale/wariOCR/main/docs/media/hero.jpg" alt="A skewed phone photo of a sheet next to the flat A4 page wariOCR made from it"></a><br>
<b><a href="https://github.com/BiNeurale/wariOCR">wariOCR</a></b> · Python<br>
Phone photos of documents to true-scale, clean A4 PDFs with optional OCR. Runs locally.
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/BiNeurale/muSCADier"><img src="https://raw.githubusercontent.com/BiNeurale/muSCADier/master/icons/muSCADier_screenshot.png" alt="An OpenSCAD model imported into Blender as native geometry"></a><br>
<b><a href="https://github.com/BiNeurale/muSCADier">muSCADier</a></b> · Blender add-on<br>
Import OpenSCAD files into Blender as native geometry: colors, fast Manifold rendering, live reload.
</td>
<td width="50%" valign="top">
<a href="https://github.com/BiNeurale/GraphOlly"><img src="https://raw.githubusercontent.com/BiNeurale/GraphOlly/main/docs/img/graph.png" alt="A function drawn as a basic-block graph inside OllyDbg 1.10"></a><br>
<b><a href="https://github.com/BiNeurale/GraphOlly">GraphOlly</a></b> · C, Win32<br>
Control-flow graph view for OllyDbg 1.10, following EIP, breakpoints and calls.
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/BiNeurale/acer-camera-black-screen-fix"><img src="https://raw.githubusercontent.com/BiNeurale/acer-camera-black-screen-fix/main/docs/media/social-preview.png" alt="Webcam black screen in every application: root cause, and a fix that survives the reboot"></a>
</td>
<td width="50%" valign="top">
<b><a href="https://github.com/BiNeurale/acer-camera-black-screen-fix">acer-camera-black-screen-fix</a></b> · PowerShell<br>
Acer webcams on Windows 11 show a black screen in every application while Device Manager says they are fine.
The Acer Device MFT is re-registered at every boot, so registry-only fixes stop working after a reboot.
This repo explains the root cause and ships a fix that survives it. Fixed on 10+ machines.
</td>
</tr>
</table>


## Upstream contributions

Fixes and bug reports I sent to other projects. Updated automatically every day.

<!-- contributions:start -->

**13 projects** · **2** merged · **8** in review · **4** bug reports

**Merged**

- **elalish/manifold** [#1926](https://github.com/elalish/manifold/pull/1926) — python: don't export the statically linked manifold and TBB symbols
- **gkjohnson/three-gpu-pathtracer** [#957](https://github.com/gkjohnson/three-gpu-pathtracer/pull/957) — Materials: default the color to white for materials without one

**In review**

- **godotengine/godot** [#125254](https://github.com/godotengine/godot/pull/125254) — Fix clearcoat_texture description: green channel is roughness, not glossiness
- **ArduPilot/ardupilot** [#35357](https://github.com/ArduPilot/ardupilot/pull/35357) — AP_Scripting: clarify set_output_pwm_chan_timeout expiry in docs
- **ValveSoftware/gamescope** [#2541](https://github.com/ValveSoftware/gamescope/pull/2541) — gamescopereaper, steamcompmgr: propagate the primary child's exit status
- **gumyr/build123d** [#1596](https://github.com/gumyr/build123d/pull/1596) — Return every face when an offset hole splits a face
- **KhronosGroup/glTF-Blender-IO** [#2789](https://github.com/KhronosGroup/glTF-Blender-IO/pull/2789) — Export: fix KeyError 'loglevel' when export_loglevel >= 0
- **riscv/riscv-opcodes** [#448](https://github.com/riscv/riscv-opcodes/pull/448) — Fix XLEN classification of Smrnmi and odd pmpcfg CSRs
- **Vector35/warp** [#46](https://github.com/Vector35/warp/pull/46) — Fix basic block order in function GUID description
- **vul337/DecompileBench** [#5](https://github.com/vul337/DecompileBench/pull/5) — extract_functions: fix crash on absolute seed corpus links and the -E fallback

**Bug reports**

- **VirusTotal/yara-x** [#894](https://github.com/VirusTotal/yara-x/issues/894) — yr scan: symlinks to files inside a scanned directory are silently skipped
- **Vector35/binaryninja-api** [#8734](https://github.com/Vector35/binaryninja-api/issues/8734) — [WARP] Blacklisted instructions (NOPs, self-moves) are still hashed into the basic block GUID
- **Wine** [59803](https://bugs.winehq.org/show_bug.cgi?id=59803) — WoW64 debugger break-in, reproducer + Windows 11 reference
- **Wine** [60719](https://bugs.winehq.org/show_bug.cgi?id=60719) — Schannel `DecryptMessage` ignores TLS `close_notify`

<!-- contributions:end -->
