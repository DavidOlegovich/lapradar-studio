# LapRadar Studio

The 3D video studio behind the short motorsport explainers on [lapradar.com](https://lapradar.com).

- `tools/studio/` — Three.js scene, cars, tracks and TikTok-style overlays, rendered headless in Chrome.
- `tools/video3d/` — one script per video: scenes, camera shots and narration in each language.
- `tools/render.py`, `tools/render_all.py` — render a video / all changed videos to MP4.

Rendering runs on GitHub Actions (`.github/workflows/render.yml`); results go to the `renders` branch, which the site picks up and voices over.

Synced from the private LapRadar repository. Please do not open pull requests here.
