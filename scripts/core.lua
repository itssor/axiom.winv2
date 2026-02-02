-- Axiom loader: picks script by game (MM2 vs universal)
-- Single source for script base URL (update here when repo changes)
local AXIOM_SCRIPT_BASE = "https://raw.githubusercontent.com/itssor/axiom.winv2/main/scripts/"
local placeId = game.PlaceId
local mm2PlaceIds = { [142823291] = true, [335132309] = true }
local scriptUrl = (mm2PlaceIds[placeId] and (AXIOM_SCRIPT_BASE .. "axiom_mm2.txt")) or (AXIOM_SCRIPT_BASE .. "axiommain.txt")
local ok, err = pcall(function()
    local src = game:HttpGet(scriptUrl)
    if not src or #src == 0 then error("Empty script response") end
    loadstring(src)()
end)
if not ok then warn("[Axiom] Loader failed: " .. tostring(err)) end
