# Axiom

Axiom Roblox scripting project (https://axiomwin.vercel.app/).

## Folder structure

| Folder / file | Purpose |
|---------------|---------|
| **scripts/** | Main deliverable scripts. `axiommain.txt` = core UI/loader; `axiom_mm2.txt` = Murder Mystery 2 build. Both load Cascade from GitHub (biggaboy212/Cascade). |
| **docs/** | Engineering rules and reference. `READ THIS BEFORE EDITING.txt` = Axiom Engineering Core (AX-EC) rules; `cascade_knowledge.txt` = Cascade API reference for Cursor. |
| **website/** | Axiom site (Vercel): `index.html`, `axiom.css`, `api/games.js`. |

## Connecting Cursor to GitHub

To let Cursor (and the app) use your GitHub account (clone repos, push/pull, etc.):

1. **Sign in with GitHub**
   - Open **Command Palette**: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
   - Run **“GitHub: Sign In”**.
   - In the status bar you’ll see a **6‑digit code**.
   - In a browser go to **https://github.com/login/device** and enter that code.
   - Finish the flow; Cursor will then be connected to GitHub.

2. **If it fails**
   - Try **“GitHub: Sign Out”** in the Command Palette, restart Cursor, then **“GitHub: Sign In”** again.
   - Or clear GitHub data under `%AppData%\Cursor` and sign in again.

3. **Using Git in this project**
   - To turn this folder into a repo and push to GitHub: run `git init` here, create a repo on GitHub, then add the remote and push. Cursor’s **Source Control** view (branch icon or `Ctrl+Shift+G`) handles commit/push/pull once the repo is set up.

Once GitHub is connected, you can say things like “push this to GitHub” or “clone my repo X” and Cursor can run the right Git commands for you.
