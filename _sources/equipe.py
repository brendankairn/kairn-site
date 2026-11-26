# ---------- PAGES CONSEILLERS ----------
# Une page par membre de l'équipe : faits validés (intitulés de Brendan) et avis Google réels
# (prénom + initiale, extraits fidèles, voir communication/avis-clients.md). Rien d'inventé.
import json as _jq

def _metiers(*keys):
    M = {"immo":("Prêt immobilier","credit-immobilier.html"),"pro":("Prêt professionnel","pret-professionnel.html"),
         "rachat":("Regroupement de crédits","rachat-de-credits.html"),"hypo":("Prêt hypothécaire","pret-hypothecaire.html"),
         "viager":("Prêt viager hypothécaire","pret-viager-hypothecaire.html"),"ass":("Assurance de prêt","assurance-emprunteur.html")}
    return [M[k] for k in keys]

CONSEILLERS = [
 {"slug":"brendan-le-roux","nom":"Brendan Le Roux","prenom":"Brendan","titre":"Dirigeant, expert en prêt hypothécaire","il":"il",
  "bio":"Fondateur et dirigeant de KAIRN, Brendan Le Roux exerce dans le courtage depuis plus de 15 ans. Il est l'expert du cabinet en prêt hypothécaire et en prêt viager hypothécaire : il monte les dossiers que les circuits bancaires classiques écartent, pour les propriétaires qui ont besoin de mobiliser la valeur de leur bien.",
  "metiers":_metiers("hypo","viager","immo","rachat"),
  "avis":[("Alexandre L.","Résidence principale","Disponible, réactif et toujours de très bon conseil, il a parfaitement analysé notre dossier et nous a trouvé la meilleure offre pour l'achat de notre résidence principale."),
          ("Manuel P.","Projet immobilier","Brendan a été de très bon conseil tout au long de notre projet et une réelle prise en compte de nos besoins. Je recommande vivement!"),
          ("Nathan L.","Achat d'un appartement","Brendan à répondu à toutes mes questions, à su se montrer patient et à l'écoute.")]},
 {"slug":"maxime-hellec-duval","nom":"Maxime Hellec-Duval","prenom":"Maxime","titre":"Expert en prêt immobilier","il":"il",
  "bio":"Expert en prêt immobilier chez KAIRN, Maxime Hellec-Duval accompagne les acheteurs du premier rendez-vous jusqu'à la signature chez le notaire : premier achat, résidence principale ou investissement. Il prépare le dossier, le présente aux banques partenaires et négocie les conditions.",
  "metiers":_metiers("immo","ass"),
  "avis":[("Chloé L.","Premier achat","Pour un premier achat immobilier, je suis vraiment contente d'avoir pu compter sur lui. Il a été présent du début à la fin, toujours joignable quand j'avais une question ou un doute, et surtout très investi dans mon dossier."),
          ("Sylvie C.","Projet immobilier","Un véritable pilier du début à la fin. […] Présent à chaque étape, rassurant et toujours disponible, il nous a permis de traverser ce projet en toute sérénité."),
          ("Charlotte G.","Acquisition","Accompagnés dans notre acquisition malgré un dossier difficile. Très professionnel et à l'écoute."),
          ("Alexandre N.","Jeune couple","Il a tout de suite compris notre situation et notre projet, surtout après les mauvais conseils que nous avions reçus de notre banque.")]},
 {"slug":"solen-rojouant","nom":"Solen Rojouant","prenom":"Solen","titre":"Experte en prêt immobilier","il":"elle",
  "bio":"Experte en prêt immobilier chez KAIRN, Solen Rojouant accompagne les acheteurs du premier rendez-vous jusqu'à la signature chez le notaire : premier achat, résidence principale ou investissement. Elle prépare le dossier, le présente aux banques partenaires et négocie les conditions.",
  "metiers":_metiers("immo","ass"),
  "avis":[("Loann C.","Premier achat","Toujours disponible, réactive et à l'écoute, elle a su me guider et me conseiller à chaque étape avec professionnalisme et bienveillance. Je recommande les yeux fermés !"),
          ("Delphine D.","Projet immobilier","D'une efficacité inégalable avec une grande écoute et des conseils qui nous ont amené à concrétiser ce projet de famille sans complication."),
          ("Kilian L.","Projet immobilier","Grâce à son professionnalisme, sa disponibilité et son écoute, notre projet a pu se concrétiser dans les meilleures conditions.")]},
 {"slug":"valerie-le-barber","nom":"Valérie Le Barber","prenom":"Valérie","titre":"Experte en prêt immobilier et professionnel","il":"elle",
  "bio":"Experte en prêt immobilier et professionnel chez KAIRN, Valérie Le Barber accompagne aussi bien les particuliers qui achètent leur logement que les entreprises et professions libérales qui financent leurs locaux, leur matériel ou une reprise. Elle travaille en binôme avec Aurélie Thouvard, coordinatrice de financement.",
  "metiers":_metiers("immo","pro","ass"),
  "avis":[("Mathieu C.","Prêt professionnel","C'est notre 3ème projet avec eux, en perso et en pro, et c'est une réussite à chaque fois. Grace au talent de Valérie Le Barber, notre entreprise va pouvoir s'installer dans un local sur mesure en 2027!"),
          ("Edwin L.","Dossier complexe","Merci infiniment a Valérie qui nous a sortie plusieurs offres avec un dossier compliqué […] nous avons enfin notre maison."),
          ("Emmanuelle J.","Deuxième achat","J'ai refait appel au cabinet 9 ans après pour un autre achat immobilier ! J'ai pu retrouver une seconde fois Valérie Le Barber."),
          ("Vincent G.","Appartement à Lorient","Valérie et Aurélie, duo de choc. […] l'acquisition de mon appartement sur Lorient malgré le contexte actuel du marché !")]},
 {"slug":"laetitia-leven","nom":"Laëtitia Leven","prenom":"Laëtitia","titre":"Experte en prêt immobilier et professionnel","il":"elle",
  "bio":"Experte en prêt immobilier et professionnel chez KAIRN, Laëtitia Leven accompagne aussi bien les particuliers qui achètent leur logement que les entreprises et professions libérales qui financent leurs locaux, leur matériel ou une installation.",
  "metiers":_metiers("immo","pro","ass"),
  "avis":[("Mathilde F.","Prêt professionnel","A su négocier le meilleur taux possible avec les banques pour l achat de mon cabinet d orthophonie."),
          ("Florian","Projet immobilier","Un grand merci à Laetitia pour sa réactivité, sa bonne humeur et son professionnalisme.")]},
 {"slug":"anais-dietrich","nom":"Anaïs Dietrich","prenom":"Anaïs","titre":"Experte en prêt immobilier","il":"elle",
  "bio":"Experte en prêt immobilier chez KAIRN, Anaïs Dietrich accompagne les acheteurs du premier rendez-vous jusqu'à la signature chez le notaire : premier achat, résidence principale ou investissement. Elle prépare le dossier, le présente aux banques partenaires et négocie les conditions.",
  "metiers":_metiers("immo","ass"),"avis":[]},
 {"slug":"laetitia-bernard","nom":"Laëtitia Bernard","prenom":"Laëtitia","titre":"Experte en regroupement de crédits et prêt hypothécaire","il":"elle",
  "bio":"Experte en regroupement de crédits et en prêt hypothécaire chez KAIRN, Laëtitia Bernard aide les foyers à réunir leurs crédits en une seule mensualité et les propriétaires à mobiliser la valeur de leur bien, y compris quand la banque habituelle a dit non.",
  "metiers":_metiers("rachat","hypo","viager"),"avis":[]},
 {"slug":"tifenn-le-bouedec","nom":"Tifenn Le Bouëdec","prenom":"Tifenn","titre":"Experte en regroupement de crédits","il":"elle",
  "bio":"Experte en regroupement de crédits chez KAIRN, Tifenn Le Bouëdec aide les propriétaires comme les locataires à réunir leurs crédits immobiliers et à la consommation en une seule mensualité, adaptée à leur budget.",
  "metiers":_metiers("rachat","hypo"),"avis":[]},
 {"slug":"aurelie-thouvard","nom":"Aurélie Thouvard","prenom":"Aurélie","titre":"Coordinatrice de financement","il":"elle",
  "bio":"Coordinatrice de financement chez KAIRN, Aurélie Thouvard suit les dossiers aux côtés des conseillers : collecte et vérification des pièces, échanges avec les banques et les notaires, jusqu'au déblocage des fonds. C'est grâce à ce binôme conseiller et coordinatrice que rien ne se perd en route.",
  "metiers":_metiers("immo","pro"),
  "avis":[("Léa","Projet pro et perso","Un grand merci à toute l'équipe, et particulièrement à Valérie Le Barber et Aurélie Thouvard […] Notre projet était complexe."),
          ("Vincent G.","Appartement à Lorient","Valérie et Aurélie, duo de choc. […] l'acquisition de mon appartement sur Lorient malgré le contexte actuel du marché !")]},
]

def conseiller_url(slug): return f"conseiller-{slug}.html"

def _conseiller_page(c):
    f = conseiller_url(c["slug"])
    av = "".join(f'<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>{t}</p><footer><b>{a}</b>{p} · Avis Google</footer></article>' for a,p,t in c["avis"][:3])
    avis_sec = (f'<section class="section white"><div class="wrap"><div class="section-head"><span class="eyebrow">Avis clients</span><h2>Ce que disent les clients de {c["prenom"]}</h2><p class="lead">Extraits d\'avis Google laissés sur la fiche KAIRN, notée 5,0 sur 204 avis.</p></div><div class="reviews">{av}</div></div></section>') if c["avis"] else ""
    met = "".join(f'<a class="card" href="{u}"><h3>{n}</h3><span class="more">Découvrir {I["arrow"]}</span></a>' for n,u in c["metiers"])
    autres = "".join(f'<li><a href="{conseiller_url(o["slug"])}">{o["nom"]}</a> · {o["titre"]}</li>' for o in CONSEILLERS if o["slug"]!=c["slug"])
    body = f'''<section class="dark page-hero">{HEXWM}<div class="wrap conseiller-hero"><div><p class="crumbs"><a href="index.html">Accueil</a> / <a href="cabinet.html">Le cabinet</a> / {c["nom"]}</p>
<span class="eyebrow">KAIRN · Lorient</span><h1 style="margin-top:14px">{c["nom"]}</h1><p class="lead" style="margin-top:14px">{c["titre"]} chez KAIRN, courtier en financement à Lorient.</p>
<div class="hero-actions"><a class="btn btn-light" href="contact.html">Être accompagné par {c["prenom"]} {I["arrow"]}</a><a class="btn btn-ghost num" href="tel:{TEL}">{PHONE}</a></div>{trust_row()}</div>
<img class="portrait" src="equipe/portrait/{c["slug"]}.jpg" alt="{c["nom"]}, {c["titre"].lower()} chez KAIRN à Lorient" width="640" height="800"></div></section>
<section class="section"><div class="wrap split"><div class="prose"><span class="eyebrow">Son rôle</span><h2 style="color:var(--text)">{c["titre"]}</h2><p>{c["bio"]}</p>
<p>Comme toute l'équipe, {c["il"]} travaille depuis notre agence du 8 mail Jeanne Villepreux-Power, à Lorient, et accompagne nos clients en Bretagne et partout en France, sur place, en visio ou par téléphone.</p></div>
<div class="panel">{ticks([("Étude gratuite","Une première analyse de votre projet, sans engagement."),("Réponse sous 24 h","Par téléphone ou par e-mail."),("Plus de 20 banques partenaires","Votre dossier présenté là où il a le plus de chances."),("Honoraires au succès","Rien à payer avant l'obtention de votre financement.")])}</div></div></section>
{avis_sec}
<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">Expertises</span><h2>Les projets que suit {c["prenom"]}</h2></div><div class="cards">{met}</div></div></section>
<section class="section white"><div class="wrap"><div class="section-head"><span class="eyebrow">L'équipe</span><h2>Les autres experts KAIRN</h2></div><ul class="team-links">{autres}</ul></div></section>
{cta_band(f"Un projet ? Contactez {c['prenom']}", "Laissez-nous vos coordonnées : nous vous rappelons sous 24 h ouvrées. L'étude est gratuite, et vous ne payez nos honoraires qu'une fois votre financement obtenu.")}'''
    org={"@id":"https://kairn-finance.com/#kairn"}
    d={"@context":"https://schema.org","@graph":[
       {"@type":"ProfilePage","@id":"https://kairn-finance.com/"+f,"name":c["nom"]+" · KAIRN","mainEntity":{"@id":"https://kairn-finance.com/cabinet.html#"+c["slug"]}},
       {"@type":"Person","@id":"https://kairn-finance.com/cabinet.html#"+c["slug"],"name":c["nom"],"jobTitle":c["titre"],"url":"https://kairn-finance.com/"+f,
        "image":"https://kairn-finance.com/equipe/portrait/"+c["slug"]+".jpg","worksFor":org,"workLocation":{"@type":"Place","name":"Lorient"},"knowsAbout":[n for n,_ in c["metiers"]]},
       {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://kairn-finance.com/"},{"@type":"ListItem","position":2,"name":"Le cabinet","item":"https://kairn-finance.com/cabinet.html"},{"@type":"ListItem","position":3,"name":c["nom"],"item":"https://kairn-finance.com/"+f}]}]}
    page(f, f'{c["nom"]} · {c["titre"]} à Lorient | KAIRN',
         f'{c["nom"]}, {c["titre"].lower()} chez KAIRN, courtier en financement à Lorient. Étude gratuite, réponse sous 24 h, avis clients.',
         body, active="cabinet.html", extra_head='<script type="application/ld+json">'+_jq.dumps(d,ensure_ascii=False)+'</script>')

for _c in CONSEILLERS: _conseiller_page(_c)
