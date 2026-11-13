# Site KAIRN

Site vitrine de KAIRN (BMB Financement), publié sur https://kairn-finance.com via le déploiement Git de l'hébergement OVH.

- Les pages HTML à la racine sont générées par `_sources/build.py` (contenu dans `_sources/pages.py`).
- Régénérer : `cd _sources && python3 build.py .. site`
- `envoi.php` reçoit les formulaires et les envoie à contact@kairn-finance.fr.
