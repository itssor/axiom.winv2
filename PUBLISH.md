# Publishing Axiom changes

## 1. Commit and push script changes

Scripts and loader live in this repo. After editing `scripts/` or `docs/`:

```bash
git add scripts/ docs/ website/ PUBLISH.md
git status
git commit -m "Your message (e.g. Config fixes, ESP outlines, config generator site)"
git push origin main
```

- **Loader URL**: The in-game loader uses  
  `https://raw.githubusercontent.com/itssor/axiom.winv2/main/scripts/core.lua`  
  (see `scripts/core.lua`; update `AXIOM_SCRIPT_BASE` if the repo or path changes.)

- **No hosting of script files on the website**: Scripts are loaded from GitHub raw; the site does not serve them.

## 2. Deploy the website (optional)

The `website/` folder is a **Config Generator** (build Axiom config JSON and copy for in-game Import). It does not host script files or act as a landing page.

- **Vercel**: Deploy the repo; set root to `website` or deploy the `website` folder.  
  If you keep `/api/games` for future use, ensure `api/games.js` is in `website/api/` (Vercel serverless).
- **Static host**: If you drop the `/api/games` dependency, you can deploy only `website/*.html`, `website/axiom.css`, and any static JS as a static site (Netlify, GitHub Pages, etc.).

After deploy, the site is a tool only; users get the loader from GitHub (e.g. README or raw link).
