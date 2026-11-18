#!/usr/bin/env node
// Signale des pages de kairn-finance.com à Bing (et aux autres moteurs IndexNow).
//   node scripts/indexnow.js                  -> toutes les URL du sitemap
//   node scripts/indexnow.js URL1 URL2 ...    -> seulement ces URL
// À lancer après chaque mise en ligne de pages nouvelles ou modifiées.
const HOST = "kairn-finance.com";
const KEY = "92e801dd3514fa6873ebbbcc29b568e0";
const KEY_LOCATION = `https://${HOST}/${KEY}.txt`;

async function urlsDuSitemap() {
  const r = await fetch(`https://${HOST}/sitemap.xml`);
  if (!r.ok) throw new Error(`sitemap.xml : HTTP ${r.status}`);
  const xml = await r.text();
  return [...xml.matchAll(/<loc>\s*([^<\s]+)\s*<\/loc>/g)].map(m => m[1]);
}

(async () => {
  let urlList = process.argv.slice(2);
  if (urlList.length === 0) urlList = await urlsDuSitemap();
  urlList = urlList.map(u => u.startsWith("http") ? u : `https://${HOST}/${u.replace(/^\//, "")}`);
  const autres = urlList.filter(u => new URL(u).host !== HOST);
  if (autres.length) throw new Error("URL hors kairn-finance.com : " + autres.join(", "));
  if (urlList.length === 0) throw new Error("Aucune URL à envoyer");

  const r = await fetch("https://api.indexnow.org/indexnow", {
    method: "POST",
    headers: { "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify({ host: HOST, key: KEY, keyLocation: KEY_LOCATION, urlList }),
  });
  const texte = await r.text();
  console.log(`${urlList.length} URL envoyées, réponse IndexNow : HTTP ${r.status} ${r.statusText}${texte ? " " + texte : ""}`);
  if (![200, 202].includes(r.status)) process.exit(1);
})().catch(e => { console.error(e.message); process.exit(1); });
