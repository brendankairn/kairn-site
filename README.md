# Site KAIRN

Site vitrine de KAIRN (BMB Financement), publié sur https://kairn-finance.com via le déploiement Git de l'hébergement OVH.

- Les pages HTML à la racine sont générées par `_sources/build.py` (contenu dans `_sources/pages.py`).
- Régénérer : `cd _sources && python3 build.py .. site`
- `envoi.php` reçoit les formulaires et les envoie à contact@kairn-finance.fr.
- IndexNow (Bing, Copilot, ChatGPT) : chaque matin à 7h, `.github/workflows/indexnow.yml` envoie automatiquement les pages modifiées sur main la veille. À la main : après chaque mise en ligne de pages nouvelles ou modifiées, lancer `node scripts/indexnow.js` (tout le sitemap) ou `node scripts/indexnow.js page.html` (seulement ces pages). La clé est dans `92e801dd3514fa6873ebbbcc29b568e0.txt` à la racine : ne pas le supprimer.
