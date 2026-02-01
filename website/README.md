# axiom.winv2 — website

Landing for Axiom.win. One loader, one copy button, game cards.

- **index.html** — Hero, copy-loader block, why cards, FAQ, supported games. Loader fetches `scripts/core.lua` from GitHub.
- **api/games.js** — Vercel serverless: returns supported games (MM2 place IDs + Universal) with names and Roblox thumbnails.
- **axiom.css** — Tokens and base styles.

Deploy this folder (e.g. Vercel) so `/api/games` works. The copied loader is:  
`loadstring(game:HttpGet("https://raw.githubusercontent.com/itssor/axiom.winv2/main/scripts/core.lua"))()`
