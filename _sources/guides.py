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
  seo=("Capacité d'emprunt et règle des 35 % | KAIRN",
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
dict(
  f="guide-regroupement-credits.html",
  court="Regroupement de crédits",
  tag="Regroupement de crédits",
  seo=("Regroupement de crédits : quand est-ce une bonne idée ? | KAIRN",
       "Regrouper ses crédits pour baisser ses mensualités : principe, coûts, durée, règles de protection et pièges à éviter. Le guide KAIRN, courtier à Lorient."),
  h1="Regroupement de crédits : quand est-ce une bonne idée ?",
  chapo="Plusieurs crédits, plusieurs prélèvements, un budget qui se tend chaque mois. Le regroupement de crédits peut redonner de l'air, à condition de bien mesurer ce qu'il coûte. Voici comment le juger.",
  minutes=5,
  points=[("Une seule mensualité","Tous vos crédits remplacés par un seul prêt."),
          ("Plus d'air chaque mois","La mensualité baisse, la durée s'allonge."),
          ("Un coût à mesurer","Le coût total augmente presque toujours.")],
  body='''
<h2 id="principe">Le principe</h2>
<p>Un établissement rachète vos crédits en cours (crédit immobilier, prêts personnels, crédit auto, crédits renouvelables) et les remplace par <strong>un seul prêt</strong>. Vous n'avez plus qu'une mensualité, en général plus basse, parce qu'elle est étalée sur une durée plus longue.</p>
<p>On peut aussi y ajouter une trésorerie pour un projet : des travaux, une voiture, une dépense imprévue.</p>

<h2 id="quand">Quand y penser ?</h2>
<ul class="guide-list">
<li><b>Votre budget est trop serré.</b> Les mensualités cumulées pèsent trop lourd et l'épargne ne se reconstitue plus.</li>
<li><b>Vos revenus changent.</b> Départ à la retraite, séparation, baisse d'activité.</li>
<li><b>Vous avez un nouveau projet.</b> Regrouper peut libérer la capacité de remboursement nécessaire.</li>
</ul>
<p>Le regroupement n'est pas une solution pour des difficultés qui durent sans cause identifiée. Dans ce cas, nous vous le dirons franchement.</p>

<h2 id="cout">Ce que ça coûte vraiment</h2>
<p>Allonger la durée fait baisser la mensualité, mais augmente presque toujours le <strong>coût total</strong> des intérêts. Il faut aussi compter les frais de dossier, les éventuelles indemnités de remboursement anticipé de vos prêts actuels, et les frais de garantie.</p>
<p>Pour un crédit immobilier, ces indemnités sont plafonnées par la loi : 6 mois d'intérêts, dans la limite de 3 % du capital restant dû. Pour les crédits à la consommation, elles sont encore plus limitées.</p>

<h2 id="regles">Les règles qui vous protègent</h2>
<p>Si la part de crédit immobilier dépasse 60 % du total regroupé, le nouveau prêt suit les règles du crédit immobilier : une offre écrite et un <strong>délai de réflexion de 10 jours</strong> avant de pouvoir l'accepter. En dessous, ce sont les règles du crédit à la consommation, avec un <strong>délai de rétractation de 14 jours</strong> après la signature.</p>
<p>Si vous êtes propriétaire, le regroupement peut être garanti par une hypothèque. Il permet alors souvent une durée plus longue et un taux plus bas. Voir notre <a href="guide-pret-hypothecaire.html">guide du prêt hypothécaire</a>.</p>

<h2 id="courtier">Notre méthode</h2>
<p>Nous commençons par faire le point sur tous vos crédits, et nous comparons la situation actuelle avec plusieurs scénarios de regroupement : mensualité, durée et coût total. Vous voyez noir sur blanc ce que vous gagnez chaque mois et ce que vous payez en plus sur la durée. Ensuite seulement, vous décidez.</p>
''',
  sim="sim_rachat", sim_titre="Simulez votre regroupement",
  lien=("rachat-de-credits.html","Notre service regroupement de crédits"),
  faqs=[("Peut-on regrouper ses crédits sans être propriétaire ?","Oui. Les locataires peuvent regrouper leurs crédits à la consommation. Les conditions dépendent surtout des revenus et du niveau d'endettement."),
        ("Mon crédit renouvelable sera-t-il fermé ?","Oui, en général. Le regroupement rembourse le solde, et le contrat est clôturé pour éviter de se réendetter."),
        ("Est-ce possible à la retraite ?","Oui. L'âge est pris en compte pour la durée et l'assurance, mais beaucoup de retraités regroupent leurs crédits, souvent avec une garantie hypothécaire.")]
),
dict(
  f="guide-pret-professionnel.html",
  court="Prêt professionnel",
  tag="Prêt professionnel",
  seo=("Prêt professionnel : comment convaincre sa banque | KAIRN",
       "Création, reprise, murs, matériel ou trésorerie : ce que la banque regarde pour un prêt professionnel, les garanties demandées et le dossier à préparer. Le guide KAIRN."),
  h1="Prêt professionnel : comment convaincre sa banque",
  chapo="Créer, reprendre, investir : un projet professionnel se joue souvent sur la qualité du dossier présenté à la banque. Voici ce qu'elle regarde, et comment préparer le vôtre.",
  minutes=5,
  points=[("Un dossier solide","Chiffres, prévisionnel et projet bien expliqués."),
          ("Un apport","Il montre votre engagement dans le projet."),
          ("Des garanties","Caution, nantissement, garantie Bpifrance.")],
  body='''
<h2 id="projets">Quels projets financer ?</h2>
<ul class="guide-list">
<li><b>Création ou reprise.</b> Rachat d'un fonds de commerce, de parts sociales, d'une clientèle.</li>
<li><b>Murs professionnels.</b> L'achat de vos locaux, en direct ou par une SCI.</li>
<li><b>Équipement.</b> Matériel, véhicules, aménagement.</li>
<li><b>Trésorerie et développement.</b> Besoin en fonds de roulement, recrutement, nouveau local.</li>
</ul>

<h2 id="banque">Ce que la banque regarde</h2>
<p>Pour une entreprise existante, la banque analyse les <strong>derniers bilans</strong> : chiffre d'affaires, rentabilité, endettement, trésorerie. Pour une création ou une reprise, tout repose sur le <strong>prévisionnel</strong> et sur votre parcours.</p>
<p>Elle veut comprendre trois choses : pourquoi le projet va fonctionner, comment l'entreprise remboursera, et ce qui se passe si ça va moins bien que prévu.</p>

<h2 id="apport">L'apport</h2>
<p>La banque attend presque toujours un apport personnel. Il montre que vous prenez votre part du risque. Son niveau dépend du projet et du secteur : il est souvent plus élevé pour une création que pour l'achat de murs ou de matériel.</p>

<h2 id="garanties">Les garanties</h2>
<p>Selon le projet, la banque peut demander une <strong>caution personnelle</strong> du dirigeant, un <strong>nantissement</strong> du fonds de commerce ou des parts, une hypothèque sur les murs, ou une <strong>garantie de Bpifrance</strong>, qui couvre une partie du risque et limite la caution demandée.</p>
<p>Tout se négocie : le montant de la caution, sa durée, son plafond. C'est un point sur lequel un courtier fait souvent la différence.</p>

<h2 id="dossier">Le dossier à préparer</h2>
<ol class="guide-steps">
<li><b>La présentation du projet.</b> Ce que vous faites, pour qui, et pourquoi maintenant.</li>
<li><b>Les chiffres.</b> Bilans des dernières années ou prévisionnel sur trois ans, fait avec votre expert-comptable.</li>
<li><b>Le plan de financement.</b> Le besoin total, votre apport, le prêt demandé.</li>
<li><b>Votre situation personnelle.</b> Patrimoine, crédits en cours, revenus du foyer.</li>
</ol>
<p>Nous montons ce dossier avec vous, puis nous le présentons aux banques les plus adaptées à votre secteur et à votre taille.</p>
''',
  sim="sim_pro", sim_titre="Simulez votre prêt professionnel",
  lien=("pret-professionnel.html","Notre service prêt professionnel"),
  faqs=[("Combien de temps faut-il pour obtenir un prêt professionnel ?","Comptez généralement quelques semaines entre le dépôt d'un dossier complet et l'accord. Un dossier bien préparé fait gagner beaucoup de temps."),
        ("Faut-il passer par sa banque habituelle ?","Pas forcément. Votre banque connaît vos comptes, mais d'autres peuvent être plus à l'aise avec votre secteur ou votre projet. Nous les mettons en concurrence."),
        ("Peut-on financer l'achat des murs par une SCI ?","Oui, c'est fréquent. La SCI achète les locaux et les loue à votre société. Le montage se réfléchit avec votre expert-comptable.")]
),
dict(
  f="guide-premier-achat.html",
  court="Premier achat",
  tag="Prêt immobilier",
  seo=("Premier achat immobilier : les étapes du financement | KAIRN",
       "Budget, apport, frais de notaire, compromis, offre de prêt et délais : les étapes d'un premier achat immobilier, expliquées simplement. Le guide KAIRN, courtier à Lorient."),
  h1="Premier achat immobilier : les étapes du financement",
  chapo="Un premier achat, c'est beaucoup de questions et un calendrier serré. Voici les étapes dans l'ordre, pour savoir à chaque moment ce qui vous attend.",
  minutes=6,
  points=[("Avant de visiter","Connaître votre budget réel."),
          ("Au compromis","Une condition suspensive de prêt vous protège."),
          ("Avant de signer","10 jours de réflexion sur l'offre de prêt.")],
  body='''
<h2 id="budget">1. Définir votre budget</h2>
<p>Avant les visites, faites le point sur ce que les banques accepteront de vous prêter : revenus, charges, apport, durée. Notre <a href="guide-capacite-emprunt-35.html">guide de la capacité d'emprunt</a> explique les règles. Une étude avec un courtier vous donne un chiffre réaliste, et une attestation de financement qui rassure les vendeurs.</p>

<h2 id="apport">2. Préparer l'apport et les frais</h2>
<p>En plus du prix, prévoyez les <strong>frais de notaire</strong> : environ 7 à 8 % du prix dans l'ancien, 2 à 3 % dans le neuf. Ajoutez les frais de garantie du prêt et, le cas échéant, les frais d'agence.</p>
<p>Les banques aiment que l'apport couvre au moins ces frais. Ce n'est pas toujours obligatoire, mais c'est souvent ce qui fait la différence.</p>

<h2 id="aides">3. Vérifier les aides</h2>
<p>Le <strong>prêt à taux zéro</strong> peut compléter votre financement pour une première résidence principale, sous conditions de ressources. Ses règles évoluent régulièrement : nous vérifions votre éligibilité au moment de l'étude. Selon votre employeur, un prêt Action Logement peut aussi être possible.</p>

<h2 id="compromis">4. Signer le compromis</h2>
<p>Le compromis de vente contient une <strong>condition suspensive d'obtention de prêt</strong> : si vous n'obtenez pas votre financement aux conditions prévues, vous récupérez votre dépôt de garantie. Le délai pour obtenir le prêt est d'au moins un mois. En pratique, on prévoit souvent 45 à 60 jours.</p>
<p>Vous disposez aussi d'un délai de rétractation de 10 jours après la signature du compromis.</p>

<h2 id="offre">5. Obtenir l'offre de prêt</h2>
<p>Nous présentons votre dossier à plusieurs banques et négocions le taux, l'assurance et les conditions. Une fois l'accord obtenu, la banque émet une <strong>offre de prêt</strong>. La loi impose un délai de réflexion de <strong>10 jours</strong> avant de pouvoir l'accepter.</p>

<h2 id="acte">6. Signer chez le notaire</h2>
<p>Le notaire reçoit les fonds de la banque et organise la signature de l'acte authentique. Vous recevez les clés le jour même. Vos premières mensualités commencent en général le mois suivant.</p>
''',
  sim="sim_capacite", sim_titre="Calculez votre budget",
  lien=("credit-immobilier.html","Notre service prêt immobilier"),
  faqs=[("Combien de temps entre le compromis et l'acte ?","Comptez en général deux à trois mois, le temps d'obtenir le prêt et que le notaire réunisse les documents."),
        ("Faut-il voir sa banque avant un courtier ?","Vous pouvez faire les deux. Un courtier compare plusieurs banques, dont la vôtre si elle est bien placée."),
        ("Peut-on acheter seul ?","Bien sûr. Le budget est calculé sur vos seuls revenus, et la banque regardera de près votre reste à vivre.")]
),
dict(
  f="guide-rachat-pret-immobilier.html",
  date="2026-11-16",
  court="Rachat de prêt immobilier",
  tag="Refinancement",
  seo=("Rachat de prêt immobilier ou renégociation : comment décider | KAIRN",
       "Renégocier avec sa banque ou faire racheter son prêt ailleurs : indemnités, frais, garantie, assurance et calcul du gain réel. Le guide KAIRN, courtier en refinancement."),
  h1="Rachat de prêt immobilier : comment savoir si ça vaut le coup",
  chapo="Votre prêt a quelques années, les conditions ont changé, et vous vous demandez s'il est possible de payer moins. Il existe deux voies : renégocier avec votre banque, ou faire racheter le prêt par une autre. Voici comment les comparer.",
  minutes=6,
  points=[("Deux options","Renégocier chez vous, ou faire racheter ailleurs."),
          ("Des frais plafonnés","Indemnités limitées par la loi."),
          ("Un seul critère","Le gain net, frais compris.")],
  body='''
<h2 id="options">Renégociation ou rachat : la différence</h2>
<p>La <strong>renégociation</strong> se fait avec votre banque actuelle. Elle accepte de baisser le taux de votre prêt en cours, par un simple avenant. Pas de nouvelle garantie, peu de frais, mais la banque n'a aucune obligation de dire oui, et elle propose rarement ses meilleures conditions à un client qui ne part pas.</p>
<p>Le <strong>rachat</strong>, ou refinancement, consiste à souscrire un nouveau prêt dans une autre banque. Ce prêt rembourse l'ancien par anticipation. C'est plus de démarches, mais c'est souvent là que se trouvent les meilleures conditions, et la concurrence fait parfois bouger votre propre banque.</p>

<h2 id="frais">Les frais à mettre en face</h2>
<ul class="guide-list">
<li><b>Les indemnités de remboursement anticipé.</b> Elles sont plafonnées par la loi : 6 mois d'intérêts, dans la limite de 3 % du capital restant dû. Certains contrats les suppriment, relisez votre offre de prêt.</li>
<li><b>La nouvelle garantie.</b> Une nouvelle caution ou une nouvelle hypothèque. Si votre ancien prêt était cautionné, une partie de la participation versée à l'organisme de caution vous est souvent restituée.</li>
<li><b>La mainlevée.</b> Si l'ancien prêt était garanti par une hypothèque, il faut la lever chez le notaire.</li>
<li><b>Les frais de dossier</b> de la nouvelle banque, qui se négocient.</li>
</ul>
<p>Des indemnités ne sont pas dues dans certains cas prévus par la loi, par exemple quand vous vendez votre bien à la suite d'une mutation professionnelle.</p>

<h2 id="calcul">Le seul bon calcul : le gain net</h2>
<p>On entend souvent qu'un rachat n'est intéressant qu'au-delà d'un certain écart de taux. Cette règle est trop simple. Ce qui compte, c'est la différence entre ce que vous paieriez jusqu'à la fin avec votre prêt actuel et ce que vous paierez avec le nouveau, <strong>tous frais compris</strong>.</p>
<p>Trois choses font varier le résultat : le capital restant dû, la durée restante et le moment où vous en êtes. Dans un prêt, les intérêts pèsent surtout les premières années. Un rachat a donc en général plus d'effet dans la première moitié du prêt.</p>

<h2 id="assurance">Ne pas oublier l'assurance</h2>
<p>Le coût de l'assurance emprunteur compte autant que le taux. Un rachat est l'occasion de choisir un contrat individuel moins cher, à garanties équivalentes. Et si seul le taux de l'assurance vous gêne, vous pouvez la changer seule, à tout moment, grâce à la loi Lemoine. Voir notre <a href="guide-assurance-pret-loi-lemoine.html">guide de l'assurance de prêt</a>.</p>

<h2 id="autres">Ce que le rachat permet aussi</h2>
<p>Le rachat peut servir à autre chose qu'à baisser le taux : réduire la mensualité en allongeant la durée, au contraire raccourcir le prêt, ajouter une enveloppe pour des travaux, ou regrouper d'autres crédits. Chaque scénario se chiffre, avec son coût total. Pour le regroupement, voir notre <a href="guide-regroupement-credits.html">guide dédié</a>.</p>

<h2 id="regles">Les règles à connaître</h2>
<p>Le nouveau prêt est un crédit immobilier comme un autre : la banque vous remet une offre écrite, et vous disposez d'un <strong>délai de réflexion de 10 jours</strong> avant de l'accepter. Il doit aussi respecter les règles d'endettement en vigueur, dont le plafond de 35 % de vos revenus, assurance comprise.</p>

<h2 id="methode">Notre méthode</h2>
<p>Nous reprenons votre offre de prêt et votre tableau d'amortissement, puis nous calculons le gain net de plusieurs scénarios : renégociation, rachat, changement d'assurance seul. Si l'opération ne vous fait pas gagner d'argent, nous vous le disons.</p>
''',
  sim="sim_capacite", sim_titre="Calculez votre capacité d'emprunt",
  lien=("credit-immobilier.html","Notre service prêt immobilier"),
  faqs=[("Ma banque peut-elle refuser de renégocier ?","Oui. La renégociation est une négociation commerciale, pas un droit. Une offre de rachat d'une autre banque est souvent le meilleur argument."),
        ("Peut-on faire racheter un prêt à taux zéro ?","Le prêt à taux zéro n'a pas d'intérêt à racheter. On le garde en général, et seul le prêt principal est refinancé."),
        ("Combien de temps prend un rachat ?","Comptez en général un à deux mois entre la constitution du dossier et le remboursement de l'ancien prêt, délai de réflexion de 10 jours compris.")]
),
dict(
  f="guide-pret-viager-hypothecaire.html",
  date="2026-11-16",
  court="Prêt viager hypothécaire",
  tag="Prêt hypothécaire",
  seo=("Prêt viager hypothécaire : fonctionnement et coût | KAIRN",
       "Emprunter sans mensualité grâce à son logement, après 60 ou 70 ans : principe, remboursement à la succession, protection des héritiers et alternatives. Le guide KAIRN."),
  h1="Prêt viager hypothécaire : emprunter sans mensualité grâce à son logement",
  chapo="Vous êtes propriétaire, à la retraite, et vous avez besoin de liquidités sans alourdir votre budget mensuel. Le prêt viager hypothécaire répond à ce besoin. C'est une solution utile, mais engageante : voici ce qu'il faut savoir.",
  minutes=6,
  points=[("Aucune mensualité","Le prêt est remboursé à la vente du bien ou à la succession."),
          ("Vous restez chez vous","Vous gardez la propriété et l'usage de votre logement."),
          ("Dette plafonnée","Elle ne peut pas dépasser la valeur du bien.")],
  body='''
<h2 id="principe">Le principe</h2>
<p>Le prêt viager hypothécaire est prévu par le Code de la consommation. Un établissement vous prête une somme, versée en une fois ou en plusieurs, garantie par une hypothèque sur un bien immobilier à usage d'habitation dont vous êtes propriétaire.</p>
<p>Vous ne remboursez rien de votre vivant, ni capital ni intérêts. Le prêt est remboursé <strong>au décès</strong>, ou plus tôt si vous vendez le bien. Vous restez propriétaire et vous continuez à y vivre.</p>

<h2 id="pour-qui">Pour qui ?</h2>
<p>Cette formule s'adresse aux propriétaires âgés, en général à partir de 65 ou 70 ans selon les établissements, dont les revenus ne permettent pas de rembourser un crédit classique. Elle peut financer des travaux d'adaptation du logement, compléter une retraite, aider un enfant ou faire face à une dépense importante.</p>

<h2 id="montant">Combien peut-on obtenir ?</h2>
<p>Le montant dépend de la valeur du bien et de votre âge : plus vous êtes âgé, plus la part de la valeur prêtée est importante. Elle reste nettement inférieure à la valeur du bien, car les intérêts s'ajoutent au capital pendant toute la durée du prêt.</p>

<h2 id="cout">Ce que ça coûte</h2>
<p>Les intérêts ne sont pas payés au fil de l'eau : ils sont capitalisés, c'est-à-dire ajoutés chaque année à la dette. Sur une longue durée, la somme à rembourser peut donc représenter beaucoup plus que le montant emprunté. Il faut aussi compter les frais de l'acte notarié et de l'hypothèque, ainsi que l'expertise du bien.</p>

<h2 id="heritiers">Et pour les héritiers ?</h2>
<p>La loi apporte une protection importante : la dette ne peut jamais dépasser la valeur du bien au moment du remboursement. Si le bien vaut moins que la somme due, les héritiers ne paient pas la différence.</p>
<p>Au décès, les héritiers peuvent rembourser la dette et garder le bien, ou le vendre et rembourser le prêteur avec le prix de vente. Ce qui reste leur revient. C'est une décision qui se prépare en famille : nous recommandons d'en parler avec eux et avec votre notaire avant de signer.</p>

<h2 id="obligations">Vos engagements</h2>
<p>Vous devez entretenir le bien et l'assurer. Le contrat peut prévoir que le prêt devient exigible si le bien est mal entretenu, loué ou vendu sans accord. Comme pour tout crédit immobilier, l'offre est écrite et vous disposez d'un <strong>délai de réflexion de 10 jours</strong> avant de l'accepter.</p>

<h2 id="alternatives">Les alternatives à comparer</h2>
<ul class="guide-list">
<li><b>Le prêt hypothécaire classique</b>, avec des mensualités, si vos revenus le permettent. Il coûte souvent moins cher. Voir notre <a href="guide-pret-hypothecaire.html">guide du prêt hypothécaire</a>.</li>
<li><b>Le prêt avance mutation</b>, qui permet de ne payer que les intérêts, ou rien, jusqu'à la vente du bien.</li>
<li><b>La vente en viager</b> ou la vente de la nue-propriété : vous n'êtes plus propriétaire, mais vous percevez un capital et vous gardez l'usage du logement.</li>
</ul>
<p>Peu d'établissements proposent le prêt viager hypothécaire. Notre rôle est de savoir qui le fait, à quelles conditions, et de vous dire honnêtement si une autre solution vous convient mieux.</p>
''',
  sim="sim_hypo", sim_titre="Estimez ce que votre bien peut mobiliser",
  lien=("pret-hypothecaire.html","Notre service prêt hypothécaire"),
  faqs=[("Faut-il un bilan de santé ?","Non. Il n'y a pas d'assurance décès sur ce prêt, puisqu'il est justement remboursé au décès."),
        ("Le bien doit-il être libre de tout crédit ?","Pas forcément, mais le prêt viager sert d'abord à rembourser ce qui reste dû sur le bien. Le reste vous est versé."),
        ("Peut-on rembourser par anticipation ?","Oui. Vous ou vos héritiers pouvez rembourser à tout moment. Les conditions sont précisées dans l'offre.")]
),
dict(
  f="guide-garantie-pret-hypotheque-caution.html",
  date="2026-11-16",
  court="Hypothèque ou caution",
  tag="Prêt immobilier",
  seo=("Hypothèque ou caution : quelle garantie pour votre prêt ? | KAIRN",
       "Caution, hypothèque conventionnelle, hypothèque légale du prêteur de deniers (ex-PPD) : fonctionnement, coûts, mainlevée et restitution. Le guide KAIRN."),
  h1="Hypothèque ou caution : quelle garantie pour votre prêt ?",
  chapo="Toute banque demande une garantie pour un prêt immobilier. Selon le choix fait, les frais au départ et à la revente ne sont pas les mêmes. Voici les trois options, et ce qu'elles changent pour vous.",
  minutes=5,
  points=[("La caution","Un organisme se porte garant de vous."),
          ("L'hypothèque","Votre bien sert de garantie, chez le notaire."),
          ("À la revente","Mainlevée d'un côté, restitution partielle de l'autre.")],
  body='''
<h2 id="pourquoi">Pourquoi une garantie ?</h2>
<p>La garantie protège la banque si le prêt n'est plus remboursé. Elle ne remplace pas l'assurance emprunteur, qui couvre le décès, l'invalidité ou l'arrêt de travail. Les deux sont presque toujours demandées.</p>

<h2 id="caution">La caution d'un organisme spécialisé</h2>
<p>Un organisme de caution s'engage à rembourser la banque si vous ne le faites plus, puis se retourne contre vous. C'est la solution la plus courante pour une résidence principale.</p>
<p>Vous versez une commission et une participation à un fonds mutuel. À la fin du prêt, ou si vous le remboursez par anticipation, <strong>une partie de cette participation vous est en général restituée</strong>. Pas de passage supplémentaire chez le notaire, et rien à faire à la revente.</p>
<p>L'organisme étudie lui aussi votre dossier et peut refuser. Dans ce cas, la banque se tourne vers l'hypothèque.</p>

<h2 id="hypotheque">L'hypothèque conventionnelle</h2>
<p>Le bien financé, ou un autre bien que vous possédez, est apporté en garantie par un acte notarié. En cas d'impayés, la banque peut faire vendre le bien. Elle permet aussi de financer des biens ou des profils que les organismes de caution n'acceptent pas : construction, terrain, investissement, <a href="guide-pret-hypothecaire.html">prêt hypothécaire</a>.</p>
<p>Elle coûte des frais de notaire, une taxe de publicité foncière et la contribution de sécurité immobilière. L'inscription prend fin un an après la dernière échéance.</p>

<h2 id="pdd">L'hypothèque légale du prêteur de deniers</h2>
<p>C'est le nouveau nom, depuis la réforme des sûretés entrée en vigueur en 2023, de l'ancien <strong>privilège de prêteur de deniers</strong> (PPD). Elle fonctionne comme une hypothèque, mais ne peut garantir que l'achat d'un bien <strong>existant</strong> : elle ne couvre pas la construction ni les travaux. Son avantage : elle échappe à la taxe de publicité foncière, ce qui la rend moins chère qu'une hypothèque classique.</p>

<h2 id="revente">Ce qui se passe si vous vendez avant la fin</h2>
<p>Avec une hypothèque, le notaire doit demander une <strong>mainlevée</strong> pour lever la garantie, ce qui a un coût, prélevé sur le prix de vente. Avec une caution, rien de tel, et vous récupérez une partie de la participation versée au départ. C'est un point à regarder si vous pensez revendre dans quelques années.</p>

<h2 id="choix">Qui choisit ?</h2>
<p>C'est la banque qui accepte ou non une garantie, mais elle en propose souvent plusieurs. Le choix se négocie avec le reste de l'offre. Nous comparons le coût total de chaque option selon votre projet et la durée pendant laquelle vous comptez garder le bien.</p>
''',
  sim="sim_capacite", sim_titre="Calculez votre capacité d'emprunt",
  lien=("credit-immobilier.html","Notre service prêt immobilier"),
  faqs=[("La caution, c'est un proche qui se porte garant ?","Non, pas pour un prêt immobilier classique. Il s'agit d'un organisme spécialisé. La caution d'un proche existe, mais elle est rarement acceptée seule par les banques."),
        ("L'hypothèque m'empêche-t-elle de vendre ?","Non. Vous pouvez vendre à tout moment. Le prêt est remboursé avec le prix de vente et le notaire organise la mainlevée."),
        ("Quelle garantie coûte le moins cher ?","Cela dépend du montant, de la nature du bien et de la durée de détention. Une caution peut coûter plus au départ mais rendre une partie à la fin. Il faut chiffrer les deux.")]
),
]

_ORDRE = ["guide-pret-hypothecaire.html","guide-pret-viager-hypothecaire.html","guide-capacite-emprunt-35.html","guide-premier-achat.html","guide-regroupement-credits.html","guide-pret-professionnel.html","guide-assurance-pret-loi-lemoine.html","guide-garantie-pret-hypotheque-caution.html","guide-rachat-pret-immobilier.html"]
GUIDES.sort(key=lambda g: _ORDRE.index(g["f"]) if g["f"] in _ORDRE else len(_ORDRE))

GUIDES_HUB = "guides.html"

def guide_cards(exclude=None):
    return "".join(f'''<a class="card" href="{g["f"]}"><span class="tag">{g["tag"]}</span><h3>{g["h1"]}</h3><p>{g["chapo"].split(". ")[0]}.</p><span class="more">Lire le guide · {g["minutes"]} min {I["arrow"]}</span></a>''' for g in GUIDES if g["f"]!=exclude)

def guide_schema(g):
    d={"@context":"https://schema.org","@graph":[
      {"@type":"Article","headline":g["h1"],"description":g["seo"][1],"datePublished":g.get("date",GUIDE_DATE),"dateModified":g.get("date",GUIDE_DATE),"inLanguage":"fr-FR",
       "mainEntityOfPage":"https://kairn-finance.com/"+g["f"],
       "author":{"@type":"Organization","name":"KAIRN","url":"https://kairn-finance.com/"},
       "publisher":{"@type":"Organization","name":"KAIRN","url":"https://kairn-finance.com/","logo":{"@type":"ImageObject","url":"https://kairn-finance.com/favicon.svg"}}},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://kairn-finance.com/"},
        {"@type":"ListItem","position":2,"name":"Guides","item":"https://kairn-finance.com/"+GUIDES_HUB},
        {"@type":"ListItem","position":3,"name":g["court"],"item":"https://kairn-finance.com/"+g["f"]}]}]}
    return '<script type="application/ld+json">'+_json.dumps(d,ensure_ascii=False)+'</script>'

import re as _re
_MOIS=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
def _date_fr(d):
    y,m,j=d.split("-"); return f"{int(j)} {_MOIS[int(m)-1]} {y}"
for g in GUIDES:
    toc = "".join('<li><a href="#%s">%s</a></li>' % (a, _re.sub(r"^\d+\. ", "", t)) for a,t in _re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', g["body"]))
    pts = "".join(f'<div><b>{b}</b><span>{s}</span></div>' for b,s in g["points"])
    simfn = globals()[g["sim"]]
    body = f'''
<section class="dark page-hero guide-hero">{HEXWM}<div class="wrap"><p class="crumbs"><a href="index.html">Accueil</a> / <a href="{GUIDES_HUB}">Guides</a> / {g["court"]}</p>
<span class="eyebrow">Guide · {g["tag"]}</span><h1 style="margin-top:14px;max-width:24ch">{g["h1"]}</h1><p class="lead" style="margin-top:18px">{g["chapo"]}</p>
<p class="guide-meta">Par l'équipe KAIRN · mis à jour le {_date_fr(g.get("date",GUIDE_DATE))} · {g["minutes"]} min de lecture</p></div></section>
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
page(GUIDES_HUB, "Guides du financement immobilier et hypothécaire | KAIRN",
     "Les guides pratiques de KAIRN, courtier à Lorient : capacité d'emprunt, assurance de prêt, prêt hypothécaire et viager, rachat de prêt, garanties. Des réponses claires, sans jargon.", _hub, active=GUIDES_HUB)
