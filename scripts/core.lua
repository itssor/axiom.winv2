-- Axiom loader: picks script by game (MM2 vs universal)
local placeId = game.PlaceId
local mm2PlaceIds = { [142823291] = true, [335132309] = true }
local base = "https://raw.githubusercontent.com/itssor/axiom.winv2/main/scripts/"
local scriptUrl = (mm2PlaceIds[placeId] and (base .. "axiom_mm2.txt")) or (base .. "axiommain.txt")
local ok, err = pcall(function()
    local src = game:HttpGet(scriptUrl)
    if not src or #src == 0 then error("Empty script response") end
    loadstring(src)()
end)
if not ok then warn("[Axiom] Loader failed: " .. tostring(err)) end
