# Kill Streak Remake — Axiom script plan

**Status:** In progress  
**Script name:** `killstreakremakeaxiom.txt`  
**From scratch, no base. Cascade + Axiom branding. Include full Speed from main script.**

---

## From your findings

### Remotes (explorer)
- **Charge**, **ClickingWhyyyyx2**, **HighlightPlayer**, **Spin5Purchased**
- **KillstreakEvents**, **MapEvents**, **MiscEvents**, **ModcallEvents**
- **TradingRemotes:** Killfeed, TeleportData, Explosion, rebound, Respawn, LightingRift, **Sounds** (backpackMode, Teleport, CandycornCollected, meteorshowerremove)
- **DeathMarkColorCorrection**, **MaxSouls**, **MinSouls**, **blackholeBeam**

### Code you shared
1. **SlapRemote** — `FireServer(targetCharacter, backpackTool, number)`  
   Hit/slap a player with your Killstreak tool (damage or intensity?).
2. **GetPing** — `InvokeServer()`  
   Returns ping (for watermark/ESP).
3. **GetBPStat** — `InvokeServer("OwnsBP")`  
   Backpack ownership or similar stat.
4. **SlapRemote** with `Instance.new("Model")` + Backpack Killstreak + float  
   Possibly fake/exploit hit (needs testing).

---

## Possible features (when we build)

| Idea | What | Risk / note |
|------|------|-------------|
| **Speed** | Full speed from main (CFrame/Velocity, magnitude, keybind, Toggle/Hold/Always On) | Copy logic from axiommain, no remotes |
| **Slap/Hit** | Button or key to fire SlapRemote at a chosen player (list/target) | Server may validate target/tool |
| **Ping in watermark** | Use GetPing in Axiom-style watermark | Safe |
| **BP stat** | Show OwnsBP (or other GetBPStat) in UI | Safe |
| **Explosion / Rebound / Respawn** | Buttons to fire these remotes (need args from your debug) | Depends on server |
| **Teleport** | TradingRemotes.Teleport or TeleportData — need correct args | Depends on server |
| **Sounds** | Trigger backpackMode, CandycornCollected, etc. (cosmetic?) | Depends on server |
| **Spin5Purchased** | Fire to fake "purchased" (if server trusts it) | Likely validated |
| **HighlightPlayer** | Use for ESP highlight or target list | Depends on game |

---

## Next steps

- You debug more and send images/details (remote args, folders, etc.).
- Then we add: `killstreakremakeaxiom.txt` from scratch, Cascade UI, Axiom branding, full Speed, plus any remotes that are safe/useful after testing.
