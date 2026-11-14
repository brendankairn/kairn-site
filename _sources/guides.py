# ---------- GUIDES PRATIQUES ----------
# Contenus de fond pour le référencement : faits réglementaires vérifiables, aucun taux ni chiffre de marché inventé.
import json as _json

GUIDE_DATE = "2026-11-14"

GUIDES = [
dict(
  f="guide-assurance-pret-loi-lemoine.html",
  court="Changer d'assurance de prêt",
  tag="Assurance de prêt",
  seo=("Changer d'assurance de prêt avec la loi Lemoine : le guide | KAIRN",
       "Résilier son assurance emprunteur à tout moment, sans frais : conditions, équivalence des garanties, délais de la banque et étapes. Le guide KAIRN, courtier à Lorient."),
  h1="Changer d'assurance de prêt : ce que la loi Lemoine permet",
  chapo="Depuis 2022, vous pouvez changer d'assurance emprunteur quand vous voulez, sans frais. Beaucoup d'emprunteurs ne le font pas, faute de savoir par où commencer. Voici comment ça marche, étape par étape.",
  minutes=6,
  points=[("À tout moment","Plus besoin d'attendre la date anniversaire du contrat."),
          ("Sans frais","Ni pénalité, ni changement du taux de votre prêt."),
          ("10 jours ouvrés","C'est le délai de réponse imposé à la banque.")],
  body='''
<h2 id="principe">Le principe : vous choisissez votre assureur</h2>
<p>L'assurance de prêt protège la banque, et vous avec, en cas de décès, d'invalidité ou d'arrêt de travail. La banque l'exige presque toujours, mais elle ne peut pas vous imposer la sienne. C'est la <strong>délégation d'assurance</strong>.</p>
<p>La loi Lemoine du 28 février 2022 est allée plus loin : vous pouvez <strong>résilier votre contrat à tout moment</strong> et le remplacer par un autre. C'est vrai pour les prêts en cours comme pour les nouveaux, sans frais et sans toucher au taux de votre crédit.</p>

<h2 id="condition">La seule condition : des garanties équivalentes</h2>
<p>Le nouveau contrat doit offrir un <strong>niveau de garanties au moins équivalent</strong> à celui exigé par votre banque. Ce n'est pas une question de prix, mais de couverture : décès, invalidité, incapacité de travail, franchise, exclusions.</p>
<p>Chaque banque publie la liste des critères qu'elle exige. Vous les trouvez dans la fiche standardisée d'information remise lors de votre prêt. C'est sur cette base que la comparaison se fait.</p>

<h2 id="sante">Questionnaire de santé et droit à l'oubli</h2>
<p>La loi Lemoine a aussi supprimé le questionnaire médical dans un cas précis : quand la part assurée ne dépasse pas <strong>200 000 € par personne</strong> et que le prêt se termine <strong>avant vos 60 ans</strong>.</p>
<p>Le <strong>droit à l'oubli</strong> a été raccourci : après un cancer ou une hépatite C, vous n'avez plus à le déclarer <strong>5 ans</strong> après la fin du protocole thérapeutique, sans rechute.</p>

<h2 id="etapes">Les étapes, concrètement</h2>
<ol class="guide-steps">
<li><b>Retrouvez vos documents.</b> Votre offre de prêt, votre tableau d'amortissement et la fiche standardisée d'information de votre banque.</li>
<li><b>Faites comparer.</b> Nous étudions votre contrat actuel et calculons gratuitement ce que vous pouvez économiser, à garanties équivalentes.</li>
<li><b>Souscrivez le nouveau contrat.</b> Il ne prend effet qu'une fois la banque d'accord.</li>
<li><b>Demandez la substitution.</b> La demande part à votre banque avec le nouveau contrat. Nous pouvons nous en charger.</li>
<li><b>La banque répond sous 10 jours ouvrés.</b> Un refus doit être motivé. En cas d'accord, elle vous adresse un avenant, et l'ancien contrat est résilié.</li>
</ol>

<h2 id="interet">Est-ce intéressant pour vous ?</h2>
<p>L'écart de prix entre un contrat de groupe bancaire et un contrat individuel peut représenter plusieurs milliers d'euros sur la durée d'un prêt. Il est souvent plus marqué si vous êtes jeune, non-fumeur, ou si votre prêt a encore de nombreuses années à courir.</p>
<p>Le plus simple reste de faire le calcul sur votre propre contrat. C'est gratuit, et vous décidez ensuite.</p>
''',
  sim="sim_assurance", sim_titre="Estimez votre économie",
  lien=("assurance-emprunteur.html","Notre service assurance de prêt"),
  faqs=[("Ma banque peut-elle refuser ?","Oui, mais uniquement si les garanties du nouveau contrat ne sont pas équivalentes à celles qu'elle exige. Elle doit alors expliquer par écrit ce qui manque."),
        ("Le taux de mon prêt peut-il changer ?","Non. La banque ne peut ni modifier le taux, ni facturer de frais parce que vous changez d'assurance."),
        ("Combien de temps faut-il ?","La banque a 10 jours ouvrés pour répondre à compter de la réception de la demande complète. En pratique, comptez quelques semaines entre la comparaison et l'avenant.")]
),
dict(
  f="guide-capacite-emprunt-35.html",
  court="Capacité d'emprunt",
  tag="Prêt immobilier",
  seo=("Capacité d'emprunt et règle des 35 % : comment calcule la banque | KAIRN",
       "Taux d'endettement de 35 %, durée de 25 ans, reste à vivre, apport : comment les banques calculent ce que vous pouvez emprunter. Le guide KAIRN, courtier à Lorient."),
  h1="Capacité d'emprunt : comment la banque fait le calcul",
  chapo="Avant de visiter, mieux vaut savoir ce que les banques accepteront de vous prêter. Les règles sont fixées au niveau national, mais chaque banque les applique à sa façon. Voici ce qui compte vraiment.",
  minutes=5,
  points=[("35 %","Taux d'endettement maximum, assurance comprise."),
          ("25 ans","Durée maximale, 27 ans dans certains cas de travaux ou de neuf."),
          ("Reste à vivre","Ce qu'il vous reste chaque mois compte autant que le ratio.")],
  body='''
<h2 id="regle">La règle des 35 %</h2>
<p>Depuis 2022, une règle du Haut Conseil de stabilité financière s'impose aux banques : vos mensualités de crédit, <strong>assurance comprise</strong>, ne doivent pas dépasser <strong>35 % de vos revenus nets</strong>.</p>
<p>Un exemple simple : avec 4 000 € de revenus nets par mois pour le foyer, la mensualité maximale est de 1 400 €. Si vous remboursez déjà 300 € par mois pour une voiture, il reste 1 100 € pour le prêt immobilier.</p>
<p>Une marge existe : chaque banque peut déroger à la règle pour une petite partie de ses dossiers, en priorité pour l'achat d'une résidence principale et pour les primo-accédants. C'est là que le choix de la bonne banque fait la différence.</p>

<h2 id="duree">La durée : 25 ans maximum</h2>
<p>La durée d'un prêt immobilier est plafonnée à <strong>25 ans</strong>. Elle peut aller jusqu'à 27 ans pour un achat dans le neuf ou avec de gros travaux, quand le remboursement démarre plus tard.</p>
<p>Allonger la durée baisse la mensualité, donc augmente le montant empruntable. Mais le coût total du crédit augmente aussi. Tout est question d'équilibre.</p>

<h2 id="revenus">Quels revenus sont retenus ?</h2>
<p>Les salaires nets avant impôt, les revenus d'indépendant (en général la moyenne des dernières années), les pensions. Les loyers perçus sont souvent pris en compte à 70 %, pour tenir compte de la vacance et des charges.</p>
<p>Les primes variables et les revenus récents sont regardés de près. Un CDI hors période d'essai rassure, mais ce n'est pas le seul profil qui obtient un prêt.</p>

<h2 id="autres">Ce que la banque regarde aussi</h2>
<ul class="guide-list">
<li><b>Le reste à vivre.</b> Ce qu'il vous reste une fois la mensualité payée. Avec de hauts revenus, 35 % passent facilement. Avec des revenus modestes, la banque sera plus prudente.</li>
<li><b>L'apport.</b> Les banques aiment qu'il couvre au moins les frais de notaire et de garantie. Ce n'est pas toujours obligatoire, mais ça pèse.</li>
<li><b>La tenue de vos comptes.</b> Pas de découvert répété, une épargne régulière, même modeste : c'est souvent ce qui fait basculer un dossier.</li>
<li><b>Votre projet.</b> Résidence principale, investissement locatif, travaux : chaque cas se présente différemment.</li>
</ul>

<h2 id="courtier">Pourquoi passer par un courtier ?</h2>
<p>Les banques n'ont pas toutes la même lecture d'un dossier. Notre travail est de présenter le vôtre à celles qui le comprendront, et de négocier le taux, l'assurance et les conditions. L'étude est gratuite, et nos honoraires ne sont dus qu'une fois votre financement obtenu.</p>
''',
  sim="sim_capacite", sim_titre="Calculez votre capacité d'emprunt",
  lien=("credit-immobilier.html","Notre service prêt immobilier"),
  faqs=[("Les 35 % incluent-ils l'assurance ?","Oui. Le taux d'endettement se calcule avec l'assurance emprunteur, et avec tous vos autres crédits en cours."),
        ("Peut-on emprunter sans apport ?","C'est plus difficile, mais possible selon votre profil, vos revenus et votre épargne. C'est typiquement le genre de dossier que nous présentons aux banques les plus ouvertes."),
        ("Un regroupement de crédits peut-il aider ?","Parfois. Regrouper vos crédits en cours peut faire baisser vos mensualités et libérer de la capacité. Il faut le vérifier au cas par cas.")]
),
dict(
  f="guide-pret-hypothecaire.html",
  court="Prêt hypothécaire",
  tag="Prêt hypothécaire",
  seo=("Prêt hypothécaire : principe, usages et précautions | KAIRN",
       "Emprunter en apportant votre bien immobilier en garantie : à quoi sert le prêt hypothécaire, pour qui, coûts, risques et solutions pour les seniors. Le guide KAIRN."),
  h1="Prêt hypothécaire : emprunter grâce à votre patrimoine",
  chapo="Vous êtes propriétaire et votre banque hésite à vous prêter ? Votre bien peut servir de garantie. Le prêt hypothécaire ouvre des portes, à condition de bien le comprendre.",
  minutes=6,
  points=[("Votre bien en garantie","Il rassure la banque quand les revenus seuls ne suffisent pas."),
          ("Chez le notaire","L'hypothèque est inscrite par acte notarié."),
          ("Un vrai engagement","En cas d'impayés, le bien peut être vendu.")],
  body='''
<h2 id="principe">Le principe</h2>
<p>Un prêt hypothécaire est un crédit garanti par un bien immobilier dont vous êtes propriétaire : résidence principale, résidence secondaire ou bien locatif. Si le prêt n'est pas remboursé, le prêteur peut faire vendre le bien pour récupérer les sommes dues.</p>
<p>Cette garantie change la façon dont la banque regarde le dossier. Vos revenus comptent toujours, mais <strong>la valeur de votre patrimoine</strong> pèse davantage dans la décision.</p>

<h2 id="usages">À quoi peut-il servir ?</h2>
<ul class="guide-list">
<li><b>Financer un projet.</b> Des travaux, l'aide à un enfant, un investissement, une trésorerie.</li>
<li><b>Regrouper ses crédits.</b> Le regroupement de crédits hypothécaire permet de rassembler crédits immobiliers et crédits à la consommation en une seule mensualité, sur une durée plus longue.</li>
<li><b>Débloquer une situation.</b> Revenus irréguliers, indépendant, retraité, dossier refusé ailleurs : la garantie peut faire la différence.</li>
</ul>

<h2 id="montant">Combien peut-on emprunter ?</h2>
<p>Le montant dépend de la valeur du bien, déduction faite des crédits qui sont déjà garantis dessus, et de votre capacité à rembourser. Le prêteur fait estimer le bien et ne prête qu'une partie de sa valeur, pour garder une marge de sécurité.</p>

<h2 id="seniors">Les solutions pour les seniors</h2>
<p>Certaines formules sont pensées pour les propriétaires âgés. Le <strong>prêt viager hypothécaire</strong> ne demande aucune mensualité : le capital et les intérêts sont remboursés à la vente du bien ou lors de la succession. Le <strong>prêt avance mutation</strong> permet de ne payer que les intérêts, ou rien, jusqu'à la vente.</p>
<p>Ces solutions engagent votre patrimoine et celui de vos héritiers. Nous prenons toujours le temps de les expliquer, et de les comparer avec les autres options.</p>

<h2 id="couts">Les coûts à prévoir</h2>
<p>En plus des intérêts et de l'assurance, l'hypothèque a un coût : les frais de notaire liés à l'acte, la taxe de publicité foncière et la contribution de sécurité immobilière. Ils dépendent du montant emprunté.</p>
<p>À la fin du prêt, l'hypothèque s'éteint d'elle-même un an après la dernière échéance. Si vous remboursez plus tôt ou vendez le bien avant, il faut une <strong>mainlevée</strong> chez le notaire, qui a aussi un coût.</p>

<h2 id="precautions">Nos conseils avant de signer</h2>
<p>Un prêt hypothécaire est un engagement sérieux. Vérifiez que la mensualité reste supportable dans la durée, comparez plusieurs offres, et lisez bien les conditions de remboursement anticipé. C'est précisément le rôle d'un courtier : trouver le bon prêteur, et vous dire aussi quand ce n'est pas la bonne solution.</p>
''',
  sim="sim_hypo", sim_titre="Simulez votre prêt hypothécaire",
  lien=("pret-hypothecaire.html","Notre service prêt hypothécaire"),
  faqs=[("Faut-il être propriétaire sans crédit en cours ?","Non. Il suffit que la valeur du bien dépasse suffisamment ce qui reste dû sur les crédits déjà garantis dessus."),
        ("Mon conjoint doit-il signer ?","Pour le logement de la famille, un couple marié doit donner son accord à deux, même si un seul des époux est propriétaire."),
        ("Est-ce possible à la retraite ?","Oui. C'est même l'une des situations où le prêt hypothécaire, ou le prêt viager hypothécaire, est le plus souvent utile.")]
),
]

GUIDES_HUB = "guides.html"

def guide_cards(exclude=None):
    return "".join(f'''<a class="card" href="{g["f"]}"><span class="tag">{g["tag"]}</span><h3>{g["h1"]}</h3><p>{g["chapo"].split(". ")[0]}.</p><span class="more">Lire le guide · {g["minutes"]} min {I["arrow"]}</span></a>''' for g in GUIDES if g["f"]!=exclude)

def guide_schema(g):
    d={"@context":"https://schema.org","@graph":[
      {"@type":"Article","headline":g["h1"],"description":g["seo"][1],"datePublished":GUIDE_DATE,"dateModified":GUIDE_DATE,"inLanguage":"fr-FR",
       "mainEntityOfPage":"https://kairn-finance.com/"+g["f"],
       "author":{"@type":"Organization","name":"KAIRN","url":"https://kairn-finance.com/"},
       "publisher":{"@type":"Organization","name":"KAIRN","url":"https://kairn-finance.com/","logo":{"@type":"ImageObject","url":"https://kairn-finance.com/favicon.svg"}}},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://kairn-finance.com/"},
        {"@type":"ListItem","position":2,"name":"Guides","item":"https://kairn-finance.com/"+GUIDES_HUB},
        {"@type":"ListItem","position":3,"name":g["court"],"item":"https://kairn-finance.com/"+g["f"]}]}]}
    return '<script type="application/ld+json">'+_json.dumps(d,ensure_ascii=False)+'</script>'

import re as _re
for g in GUIDES:
    toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a,t in _re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', g["body"]))
    pts = "".join(f'<div><b>{b}</b><span>{s}</span></div>' for b,s in g["points"])
    simfn = globals()[g["sim"]]
    body = f'''
<section class="dark page-hero guide-hero">{HEXWM}<div class="wrap"><p class="crumbs"><a href="index.html">Accueil</a> / <a href="{GUIDES_HUB}">Guides</a> / {g["court"]}</p>
<span class="eyebrow">Guide · {g["tag"]}</span><h1 style="margin-top:14px;max-width:24ch">{g["h1"]}</h1><p class="lead" style="margin-top:18px">{g["chapo"]}</p>
<p class="guide-meta">Par l'équipe KAIRN · mis à jour le 14 novembre 2026 · {g["minutes"]} min de lecture</p></div></section>
<section class="section white"><div class="wrap guide-grid">
<article class="guide-body"><div class="guide-points">{pts}</div>{g["body"]}</article>
<aside class="guide-aside"><nav class="panel guide-toc" aria-label="Sommaire"><h3>Sommaire</h3><ol>{toc}</ol></nav>
<div class="panel guide-cta"><h3>Un avis sur votre situation ?</h3><p class="fine">Un expert KAIRN étudie votre dossier gratuitement et vous répond sous 24 h.</p>
<button class="btn btn-primary" type="button" data-callback style="width:100%;justify-content:center">Être rappelé</button>
<a class="btn btn-outline" href="{g["lien"][0]}" style="width:100%;justify-content:center">{g["lien"][1]}</a></div></aside>
</div></section>
<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">Simulateur</span><h2>{g["sim_titre"]}</h2></div>{simfn("g"+g["f"][6:10])}</div></section>
<section class="section white"><div class="wrap split"><div class="section-head"><span class="eyebrow">Questions fréquentes</span><h2>Vos questions</h2></div>{faq(g["faqs"])}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">À lire aussi</span><h2>Nos autres guides</h2></div><div class="cards">{guide_cards(g["f"])}</div></div></section>
{cta_band()}'''
    page(g["f"], g["seo"][0], g["seo"][1], body, active=GUIDES_HUB, extra_head=guide_schema(g))

_hub = f'''
<section class="dark page-hero">{HEXWM}<div class="wrap"><p class="crumbs"><a href="index.html">Accueil</a> / Guides</p>
<span class="eyebrow">Guides pratiques</span><h1 style="margin-top:14px;max-width:22ch">Comprendre avant d'emprunter</h1>
<p class="lead" style="margin-top:18px">Des réponses claires aux questions que nos clients nous posent chaque jour. Écrites par l'équipe KAIRN, sans jargon.</p></div></section>
<section class="section"><div class="wrap"><div class="cards">{guide_cards()}</div></div></section>
{cta_band()}'''
page(GUIDES_HUB, "Guides du financement : prêt immobilier, assurance, hypothécaire | KAIRN",
     "Les guides pratiques de KAIRN, courtier à Lorient : capacité d'emprunt, assurance de prêt et loi Lemoine, prêt hypothécaire. Des réponses claires, sans jargon.", _hub, active=GUIDES_HUB)
