const MM2_PLACE_IDS = [142823291, 335132309];
const UNIVERSAL_THUMB = "https://img.icons8.com/ios-filled/512/38bd7c/globe--v1.png";

export default async function handler(req, res) {
  res.setHeader("Cache-Control", "s-maxage=3600, stale-while-revalidate");
  res.setHeader("Access-Control-Allow-Origin", "*");
  const ids = MM2_PLACE_IDS.join(",");
  try {
    const [detailsRes, thumbRes] = await Promise.all([
      fetch(`https://games.roblox.com/v1/games/multiget-place-details?placeIds=${ids}`, {
        headers: { "User-Agent": "Axiom/1.0" },
      }),
      fetch(
        `https://thumbnails.roblox.com/v1/places/gameicons?placeIds=${ids}&size=512x512&format=Png&isCircular=false`
      ),
    ]);
    const details = await detailsRes.json();
    const thumbs = await thumbRes.json();
    const data = Array.isArray(details) ? details : [];
    const thumbMap = {};
    if (thumbs.data && Array.isArray(thumbs.data)) {
      thumbs.data.forEach((t) => {
        thumbMap[t.targetId] = t.imageUrl;
      });
    }
    const games = data.map((g) => ({
      placeId: g.id,
      name: g.name || "Unknown",
      thumbUrl: thumbMap[g.id] || null,
    }));
    games.push({
      placeId: "universal",
      name: "Universal",
      thumbUrl: UNIVERSAL_THUMB,
    });
    return res.status(200).json(games);
  } catch (e) {
    return res.status(200).json([
      { placeId: 142823291, name: "Murder Mystery 2", thumbUrl: null },
      { placeId: "universal", name: "Universal", thumbUrl: UNIVERSAL_THUMB },
    ]);
  }
}
