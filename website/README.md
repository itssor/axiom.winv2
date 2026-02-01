# axiom.winv2 — website

Landing for Axiom.win. One loader, one copy button, game cards with thumbnails.

- **index.html** — Landing: hero, **Copy loader** (top center), supported games grid. Loader code fetches **core.lua from GitHub** raw.
- **api/games.js** — Vercel serverless: returns supported games (MM2 place IDs + Universal) with names and Roblox thumbnails.
- **axiom.css** — Tokens and base styles.
- **core.lua** — Deprecated stub; real loader lives in GitHub (`axiom.win - roblox`).

Deploy this folder (e.g. Vercel) so `/api/games` works. The copied loader is:  
`loadstring(game:HttpGet("https://raw.githubusercontent.com/itssor/axiom.winv2/main/axiom.win%20-%20roblox/core.lua"))()`
