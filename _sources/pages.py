# ---------- ACCUEIL ----------
cards = "".join(f'''<a class="card{' card-feature' if k=='immo' else ''}" href="{f}"><div class="ico">{I[i]}</div><span class="tag">{tag}</span><h3>{t}</h3><p>{d}</p><span class="more">Découvrir {I["arrow"]}</span></a>''' for f,i,t,tag,d,k in EXPERTISES)
cards += f'''<a class="card" href="contact.html"><div class="ico">{I["plus"]}</div><span class="tag">Sur mesure</span><h3>Un dossier atypique ?</h3><p>Viager hypothécaire, vente à réméré, profils refusés ailleurs : chaque situation a sa solution. Parlons-en.</p><span class="more">Nous contacter {I["arrow"]}</span></a>'''

home = f'''
<section class="dark hero">{HEXWM}<div class="wrap hero-grid">
<div><span class="eyebrow">Courtier en financement · Lorient</span>
<h1 style="margin-top:16px">Votre financement,<br><em>une pierre à la fois.</em></h1>
<p class="lead">Prêt immobilier, prêt professionnel, regroupement de crédits, prêt hypothécaire et assurance de prêt. Un seul cabinet, 15 ans de négociation face aux banques, et un expert qui suit votre dossier du premier appel à la signature.</p>
<div class="hero-actions"><a class="btn btn-light" href="#simulateurs">Simuler mon projet {I["arrow"]}</a><a class="btn btn-ghost num" href="tel:{TEL}">{PHONE}</a></div>
{trust_row()}</div>
<div>{lead_wizard()}</div>
</div></section>

<section class="section white" style="padding-block:40px"><div class="wrap">{stats()}</div></section>

<section class="section" id="exp"><div class="wrap">
<div class="section-head"><span class="eyebrow">Nos expertises</span><h2>Un seul expert, <span class="u">tous vos financements</span></h2><p class="lead">Particulier ou chef d'entreprise, nous construisons le montage adapté à votre situation, puis nous le présentons aux banques qui vont l'accepter.</p></div>
<div class="cards">{cards}</div></div></section>

<section class="section white" id="simulateurs"><div class="wrap">
<div class="section-head"><span class="eyebrow">Simulateurs</span><h2>Faites vos calculs en 30 secondes</h2><p class="lead">Un premier ordre de grandeur immédiat. Votre expert l'affine ensuite avec vos vrais chiffres.</p></div>
<div class="sim-tabs" role="tablist" data-tabs>
<button class="sim-tab" role="tab" aria-selected="true" aria-controls="t-cap">Capacité d'emprunt</button>
<button class="sim-tab" role="tab" aria-selected="false" aria-controls="t-rac">Regroupement de crédits</button>
<button class="sim-tab" role="tab" aria-selected="false" aria-controls="t-ass">Assurance de prêt</button>
<button class="sim-tab" role="tab" aria-selected="false" aria-controls="t-hyp">Prêt hypothécaire</button></div>
<div id="t-cap" role="tabpanel">{sim_capacite("hcap")}</div>
<div id="t-rac" role="tabpanel" hidden>{sim_rachat("hrac")}</div>
<div id="t-ass" role="tabpanel" hidden>{sim_assurance("hass")}</div>
<div id="t-hyp" role="tabpanel" hidden>{sim_hypo("hhyp")}</div>
</div></section>

<section class="section dark">{HEXWM}<div class="wrap">
<div class="section-head"><span class="eyebrow">La différence KAIRN</span><h2>Un algorithme calcule.<br>Un expert comprend.</h2><p class="lead">Les plateformes en ligne traitent des formulaires. Nous traitons des dossiers, y compris ceux qui sortent des cases.</p></div>
<div class="versus">
<div class="vs-col vs-them"><h3>Plateforme en ligne</h3><ul>
<li>{I["x"]}Formulaire standard, profil noté automatiquement</li><li>{I["x"]}Un conseiller différent à chaque appel</li><li>{I["x"]}Le taux est comparé, le reste est survolé</li><li>{I["x"]}Indépendants, SCI, profils atypiques souvent écartés</li></ul></div>
<div class="vs-col vs-us"><h3>Expert KAIRN</h3><ul>
<li>{I["check"]}Dossier construit sur mesure et argumenté pour la banque</li><li>{I["check"]}Un seul interlocuteur, de l'étude à la signature</li><li>{I["check"]}Taux, assurance, frais et garanties négociés ensemble</li><li>{I["check"]}Profils complexes bienvenus : c'est notre spécialité</li></ul></div>
</div></div></section>

<section class="section" id="methode"><div class="wrap">
<div class="section-head"><span class="eyebrow">Notre méthode</span><h2>Quatre étapes, un seul interlocuteur</h2></div>
<div class="steps">
<div class="step-card"><div class="n">1</div><h3>Étude gratuite</h3><ul><li>Analyse de votre situation globale</li><li>Faisabilité et budget réel</li><li>Attestation de financement si besoin</li></ul></div>
<div class="step-card"><div class="n">2</div><h3>Dossier solide</h3><ul><li>Espace client sécurisé</li><li>Pièces vérifiées une par une</li><li>Montage financier optimisé</li></ul></div>
<div class="step-card"><div class="n">3</div><h3>Mise en concurrence</h3><ul><li>Plusieurs banques sollicitées en parallèle</li><li>Négociation taux, assurance, frais</li><li>Comparatif clair des offres</li></ul></div>
<div class="step-card"><div class="n">4</div><h3>Signature et suivi</h3><ul><li>Vérification des offres de prêt</li><li>Lien avec notaire et banque</li><li>Suivi jusqu'au déblocage des fonds</li></ul></div>
</div></div></section>

<section class="section white"><div class="wrap">
<div class="section-head" style="max-width:none;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:20px"><div style="display:grid;gap:14px"><span class="eyebrow">Avis clients</span><h2>Ils nous ont confié leur projet</h2></div>
<a class="rating" href="https://www.google.com/maps/search/?api=1&query=KAIRN+8+mail+Jeanne+Villepreux+Lorient" rel="noopener" style="text-decoration:none"><b>5,0</b><div><div class="stars">★★★★★</div><span style="color:var(--muted);font-size:.85rem">204 avis Google · voir tous les avis</span></div></a></div>
{REVIEWS}</div></section>

<section class="section"><div class="wrap split">
<div class="section-head"><span class="eyebrow">Questions fréquentes</span><h2>Ce que l'on nous demande le plus</h2><p class="lead">Une autre question ? Appelez-nous, la réponse prend rarement plus de cinq minutes.</p><div><a class="btn btn-primary" href="contact.html">Poser ma question {I["arrow"]}</a></div></div>
{faq([
 ("Quand paie-t-on un courtier ?","Jamais avant le prêt : la loi interdit de demander le moindre versement avant l'obtention du financement. L'étude de votre dossier est gratuite, nos honoraires ne sont dus qu'en cas de succès, à la signature."),
 ("Pourquoi passer par un courtier plutôt que par sa banque ?","Nous présentons votre dossier à plusieurs banques en même temps et négocions l'ensemble des conditions : taux, assurance, frais de dossier, garanties, modularité. Votre banque, elle, ne vous propose que ses propres offres."),
 ("Combien de temps faut-il pour obtenir un accord ?","Un accord de principe arrive en général en quelques jours, une offre de prêt définitive sous 2 à 4 semaines. Un dossier complet dès le départ fait gagner beaucoup de temps."),
 ("Faut-il un apport ?","Souvent oui, mais pas toujours autant qu'on le croit. Des revenus stables, une épargne régulière et des comptes bien tenus peuvent compenser un apport réduit."),
 ("Intervenez-vous en dehors de la Bretagne ?","Oui. Le cabinet est à Lorient et nos clients sont partout en France. Rendez-vous en agence, en visio ou par téléphone, avec un parcours entièrement digitalisé."),
])}</div></section>
{cta_band()}
'''
page("index.html","KAIRN · Courtier en financement à Lorient","KAIRN, courtier en financement à Lorient : prêt immobilier, prêt professionnel, regroupement de crédits, prêt hypothécaire, assurance de prêt. Étude gratuite, réponse sous 24 h.",home)

# ---------- MÉTIERS ----------
def metier(fname, crumb, eyebrow, title, lead, seo, intro_h, intro_p, situations, sim_title, sim_html, faqs, extra=""):
    body = page_hero(crumb, eyebrow, title, lead) + f'''
<section class="section"><div class="wrap split">
<div class="prose"><span class="eyebrow">{eyebrow}</span><h2 style="color:var(--text)">{intro_h}</h2>{intro_p}</div>
<div class="panel">{ticks(situations)}</div></div></section>
<section class="section white"><div class="wrap"><div class="section-head"><span class="eyebrow">Simulateur</span><h2>{sim_title}</h2></div>{sim_html}</div></section>
{extra}
<section class="section"><div class="wrap split"><div class="section-head"><span class="eyebrow">Questions fréquentes</span><h2>Vos questions</h2></div>{faq(faqs)}</div></section>
{cta_band()}'''
    page(fname, seo[0], seo[1], body)

metier("credit-immobilier.html","Crédit immobilier","Crédit immobilier",
 "Achetez au <span class='u'>bon prix</span>, empruntez aux bonnes conditions",
 "Résidence principale, investissement locatif, prêt relais, renégociation. Nous négocions l'ensemble de votre financement, pas seulement le taux.",
 ("Crédit immobilier à Lorient · Courtier KAIRN","Courtier en crédit immobilier à Lorient et en Bretagne : résidence principale, investissement locatif, prêt relais, renégociation. Étude gratuite sous 24 h."),
 "De l'idée à la remise des clés",
 "<p>Avant même de visiter, nous calculons votre budget réel et vous remettons une <strong>attestation de financement</strong> qui rassure vendeurs et agences. Une fois le compromis signé, nous mettons plusieurs banques en concurrence et négocions le <strong>taux, l'assurance, les frais de dossier et les garanties</strong>.</p><p>Primo-accédant, investisseur, indépendant, achat en SCI : nous savons présenter chaque profil sous son meilleur jour.</p>",
 [("Résidence principale ou secondaire","Achat dans l'ancien, le neuf, VEFA ou construction."),("Investissement locatif","Nom propre ou SCI, LMNP, colocation, immeuble de rapport."),("Prêt relais","Acheter avant d'avoir vendu, sans tension sur votre budget."),("Renégociation et rachat de prêt","Faire baisser le coût d'un crédit en cours.")],
 "Combien pouvez-vous emprunter ?", sim_capacite("ci"),
 [("Quels documents préparer ?","Pièce d'identité, justificatif de domicile, trois derniers bulletins de salaire, deux derniers avis d'imposition, trois derniers relevés de chaque compte, justificatifs d'épargne et tableaux d'amortissement des crédits en cours. Indépendants : deux ou trois derniers bilans."),
  ("Qu'est-ce que la règle des 35 % ?","Les banques limitent vos mensualités de crédit, assurance comprise, à 35 % de vos revenus nets, sur une durée de 25 ans maximum (27 ans dans certains cas de construction). Des dérogations existent pour les dossiers solides."),
  ("Le taux est-il le seul critère ?","Non. L'assurance, les frais de dossier, la garantie, les pénalités de remboursement anticipé et la modularité des échéances pèsent souvent autant que le taux sur le coût réel.")])

metier("pret-professionnel.html","Prêt professionnel","Prêt professionnel",
 "Créer, reprendre, investir : <span class='u'>votre banque n'est pas la seule porte</span>",
 "Création, reprise de fonds ou de parts, locaux, matériel, trésorerie. Un dossier argumenté, présenté aux interlocuteurs qui financent votre secteur.",
 ("Prêt professionnel à Lorient · Courtier KAIRN","Financement professionnel à Lorient et partout en France : création, reprise d'entreprise, achat de locaux, matériel, trésorerie. Dossier préparé et présenté à plusieurs banques."),
 "Ce que la banque regarde dans votre dossier",
 "<p>Un banquier finance d'abord une personne et un projet cohérent. Nous vous aidons à préparer un <strong>prévisionnel réaliste et défendable</strong>, à valoriser votre parcours et à proposer les bonnes garanties : caution, nantissement, organismes de garantie.</p><p>Nous présentons ensuite le dossier à <strong>plusieurs établissements</strong>, y compris ceux que vous n'auriez pas sollicités.</p>",
 [("Création d'entreprise","Financement du démarrage, avec ou sans apport important."),("Reprise","Fonds de commerce, parts sociales, clientèle."),("Locaux professionnels","Achat des murs en direct ou via une SCI."),("Matériel et travaux","Équiper, agrandir, rénover votre outil de travail.")],
 "Estimez votre mensualité", sim_pro(),
 [("Faut-il un apport pour un prêt professionnel ?","Les banques attendent souvent 20 à 30 % d'apport sur une création ou une reprise. Des prêts d'honneur ou des dispositifs de garantie peuvent compléter un apport limité."),
  ("Combien de temps pour obtenir un accord ?","Comptez généralement 3 à 6 semaines selon la taille du projet et la qualité du prévisionnel. Un dossier complet dès le départ réduit nettement ce délai."),
  ("Financez-vous aussi les professions libérales ?","Oui : installation, rachat de patientèle ou de clientèle, achat de cabinet, matériel médical ou paramédical.")])

metier("rachat-de-credits.html","Regroupement de crédits","Regroupement de crédits",
 "Trop de mensualités ? <span class='u'>Retrouvez de l'air</span> chaque mois",
 "Réunissez vos crédits immobiliers et à la consommation en une seule mensualité adaptée à votre budget, avec ou sans garantie sur votre bien.",
 ("Regroupement de crédits à Lorient · Courtier KAIRN","Regroupement et rachat de crédits à Lorient et partout en France : une seule mensualité, adaptée à votre budget. Propriétaires et locataires, étude gratuite."),
 "C'est pour qui, au juste ?",
 "<p>Le regroupement de crédits s'adresse à ceux dont les mensualités pèsent trop lourd : plusieurs crédits en cours, une baisse de revenus, un projet à financer en plus. Nous rassemblons vos prêts en <strong>un seul crédit</strong>, avec <strong>une seule mensualité</strong>, et nous pouvons y intégrer une trésorerie pour un nouveau projet.</p><p>Propriétaire ou locataire, les solutions existent. Notre rôle est aussi de vous dire honnêtement quand ce n'est pas la bonne option.</p>",
 [("Plusieurs crédits en cours","Auto, consommation, renouvelable, immobilier."),("Revenus en baisse","Retraite, séparation, changement d'activité."),("Un projet à financer","Travaux, achat, imprévu, à intégrer au regroupement."),("Besoin de souffler","Un budget lisible et une seule date de prélèvement.")],
 "Votre mensualité avant et après", sim_rachat(),
 [("Le regroupement de crédits coûte-t-il plus cher ?","Il baisse la mensualité en allongeant en général la durée, ce qui peut augmenter le coût total. Nous vous présentons les deux chiffres pour décider en connaissance de cause."),
  ("Peut-on regrouper ses crédits en étant locataire ?","Oui, avec un regroupement sans garantie immobilière. Les montants sont plus limités et les taux un peu plus élevés que pour un propriétaire."),
  ("Faut-il changer de banque ?","Non, vous gardez votre compte courant. Seuls les crédits sont remboursés et remplacés par le nouveau prêt.")],
 extra='<section class="section" style="padding-block:0 8px"><div class="wrap"><p class="warning">Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.</p></div></section>')

metier("pret-hypothecaire.html","Prêt hypothécaire","Prêt hypothécaire",
 "Votre bien peut financer vos projets <span class='u'>sans avoir à le vendre</span>",
 "Propriétaire d'une résidence principale, secondaire ou locative ? Mobilisez la valeur de votre patrimoine pour obtenir des liquidités.",
 ("Prêt hypothécaire à Lorient · Courtier KAIRN","Prêt hypothécaire, viager hypothécaire et vente à réméré à Lorient et partout en France : mobilisez votre patrimoine immobilier. Étude gratuite."),
 "Le prêt hypothécaire en trois points",
 "<p>Le principe est simple : <strong>vous êtes propriétaire</strong>, votre bien sert de <strong>garantie</strong> à la banque, et elle vous prête en s'appuyant sur sa valeur, en général jusqu'à <strong>70 %</strong>. Vous conservez la propriété et l'usage de votre bien.</p><p>C'est une de nos spécialités. Nous savons monter ces dossiers, souvent écartés par les circuits classiques.</p>",
 [("Travaux et projets","Rénovation, agrandissement, achat d'un autre bien."),("Trésorerie","Pour un besoin personnel ou professionnel, sans justification d'usage dans certains cas."),("Rachat de soulte","Garder le logement après une séparation ou une succession."),("Regroupement avec garantie","Des conditions plus favorables grâce au bien.")],
 "Combien pouvez-vous mobiliser ?", sim_hypo(),
 [("Faut-il justifier l'utilisation des fonds ?","Pas toujours : certains prêts hypothécaires sont « sans affectation ». Dans d'autres cas, la banque demande des devis ou des justificatifs."),
  ("Que se passe-t-il si je ne rembourse pas ?","Comme pour tout crédit, des incidents de paiement exposent à des poursuites, et la banque peut faire valoir l'hypothèque. C'est pourquoi nous vérifions avec vous la soutenabilité de chaque mensualité."),
  ("Combien coûtent les frais d'hypothèque ?","Les frais de notaire liés à l'hypothèque représentent en général 1,5 à 2 % du montant emprunté. Nous les intégrons dans la simulation détaillée.")],
 extra=f'''<section class="section" id="seniors"><div class="wrap"><div class="section-head"><span class="eyebrow">Solutions patrimoniales</span><h2>Pour les seniors et les situations délicates</h2></div>
<div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
<div class="card"><div class="ico">{I["home"]}</div><h3>Prêt viager hypothécaire</h3><p>Pour les propriétaires seniors : obtenir des liquidités sans vendre et sans mensualités, le prêt étant remboursé au moment de la vente ou de la succession.</p></div>
<div class="card"><div class="ico">{I["key"]}</div><h3>Vente à réméré</h3><p>Vendre temporairement son bien pour se refinancer, tout en conservant le droit de le racheter dans un délai fixé, en général jusqu'à 5 ans. Une solution encadrée, à étudier avec soin.</p></div>
</div></div></section>''')

metier("assurance-emprunteur.html","Assurance de prêt","Assurance de prêt",
 "Payez-vous trop pour <span class='u'>votre assurance de prêt</span> ?",
 "Mêmes garanties, souvent beaucoup moins cher. Depuis la loi Lemoine, vous pouvez changer d'assurance à tout moment, sans frais.",
 ("Assurance de prêt à Lorient · Calcul d'économie gratuit · KAIRN","Changez d'assurance emprunteur à tout moment grâce à la loi Lemoine. Calcul gratuit de votre économie, garanties équivalentes, démarches prises en charge."),
 "Changer d'assurance, c'est simple et c'est votre droit",
 "<p>L'assurance représente souvent <strong>un tiers du coût total</strong> d'un crédit immobilier. Le contrat groupe proposé par la banque est rarement le moins cher, surtout si vous êtes jeune, non-fumeur ou en bonne santé.</p><p>Depuis la loi Lemoine, vous pouvez <strong>changer d'assurance à tout moment</strong>, sans frais, dès lors que les garanties du nouveau contrat sont équivalentes. Nous comparons, nous montons le dossier et nous gérons les échanges avec votre banque.</p>",
 [("Calcul gratuit de votre économie","À partir de votre offre de prêt et de votre contrat actuel."),("Garanties équivalentes","Nous vérifions la fiche d'information standardisée exigée par la banque."),("Démarches prises en charge","Résiliation, substitution et suivi de l'avenant."),("Pour tous vos prêts","Nouveau crédit ou prêt en cours, quelle que soit la date de signature.")],
 "Estimez votre économie", sim_assurance(),
 [("Ma banque peut-elle refuser le changement ?","Uniquement si les garanties du nouveau contrat ne sont pas équivalentes à celles exigées. Elle doit motiver son refus par écrit sous 10 jours ouvrés."),
  ("Dois-je remplir un questionnaire de santé ?","Pas pour les prêts dont la part assurée est inférieure à 200 000 € par personne et qui se terminent avant vos 60 ans. Au-delà, un questionnaire reste nécessaire."),
  ("Combien de temps prend le changement ?","En général 3 à 6 semaines entre la demande et la prise d'effet du nouveau contrat.")])

# ---------- SIMULATEURS ----------
sims = page_hero("Simulateurs","Simulateurs","Faites vos calculs <span class='u'>en 30 secondes</span>","Cinq outils pour un premier ordre de grandeur. Votre expert affine ensuite chaque chiffre avec votre situation réelle.") + "".join(f'''<section class="section {'white' if n%2 else ''}" id="{sid}"><div class="wrap"><div class="section-head"><span class="eyebrow">{e}</span><h2>{t}</h2></div>{h}</div></section>''' for n,(sid,e,t,h) in enumerate([
 ("capacite","Crédit immobilier","Capacité d'emprunt",sim_capacite("s1")),
 ("regroupement","Regroupement de crédits","Mensualité avant et après",sim_rachat("s2")),
 ("assurance","Assurance de prêt","Économie sur votre assurance",sim_assurance("s3")),
 ("hypothecaire","Prêt hypothécaire","Montant mobilisable",sim_hypo("s4")),
 ("professionnel","Prêt professionnel","Mensualité d'un prêt pro",sim_pro("s5"))])) + cta_band("Un chiffre ne remplace pas une étude","Ces simulateurs donnent un ordre de grandeur. Pour un montant fiable, un expert étudie votre dossier gratuitement et vous rappelle sous 24 h.")
page("simulateurs.html","Simulateurs de crédit · KAIRN","Simulateurs gratuits : capacité d'emprunt, regroupement de crédits, économie d'assurance de prêt, prêt hypothécaire et prêt professionnel.",sims)

# ---------- CABINET ----------
team = [("Brendan Le Roux","Fondateur et dirigeant"),("Aurélie Thouvard","Coordinatrice de financement"),("Valérie Le Barber","Experte immobilier et professionnel"),("Solen Rojouant","Experte en financement"),("Laëtitia Bernard","Experte prêts hypothécaires"),("Tifenn Le Bouëdec","Experte regroupement de crédits"),("Maxime Hellec","Expert en financement"),("Laëtitia Leven","Experte immobilier et professionnel"),("Anaïs Dietrich","Experte en financement")]
def ini(n):
    p=n.replace("-"," ").split(); return (p[0][0]+p[-1][0]).upper()
tm = "".join(f'<div class="member"><div class="avatar">{ini(n)}</div><div><b>{n}</b><span>{r}</span></div></div>' for n,r in team)
cab = page_hero("Le cabinet","Le cabinet","La confiance, <span class='u'>première pierre</span> de tout financement","Un cairn est un empilement de pierres qui guide le marcheur. C'est ce que nous voulons être pour vous : un repère fiable, posé pierre après pierre.") + f'''
<section class="section"><div class="wrap split">
<div class="prose"><span class="eyebrow">Notre histoire</span><h2 style="color:var(--text)">Un cabinet indépendant, exigeant et sur mesure</h2>
<p>Après <strong>15 années dans le courtage</strong>, Brendan Le Roux a créé KAIRN pour bâtir le cabinet qu'il aurait voulu trouver comme client : indépendant, rigoureux, et capable de traiter les dossiers que d'autres laissent de côté.</p>
<p>Aujourd'hui, <strong>9 experts</strong> accompagnent nos clients depuis Lorient, en Bretagne et partout en France. Chaque dossier est étudié avec précision, chaque solution choisie avec rigueur, dans un seul objectif : servir vos intérêts.</p></div>
<div class="panel">{ticks([("Indépendance totale","Aucune banque ne nous dicte ses produits."),("Honoraires au succès","Rien à payer avant l'obtention de votre financement."),("Un interlocuteur dédié","En agence, en visio ou par téléphone."),("Un parcours sécurisé","Espace client et signature électronique.")])}</div>
</div></section>
<section class="section white" style="padding-block:40px"><div class="wrap">{stats()}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">L'équipe</span><h2>9 experts à votre service</h2></div><div class="team">{tm}</div></div></section>
<section class="section white" id="methode"><div class="wrap"><div class="section-head"><span class="eyebrow">Notre méthode</span><h2>Quatre étapes, un seul interlocuteur</h2></div>
<div class="steps">
<div class="step-card"><div class="n">1</div><h3>Mise en place du dossier</h3><ul><li>Ouverture de votre espace client sécurisé</li><li>Collecte des pièces justificatives</li><li>Vérification de chaque document</li></ul></div>
<div class="step-card"><div class="n">2</div><h3>Étude du projet</h3><ul><li>Analyse complète de faisabilité</li><li>Rendez-vous avec votre courtier dédié</li><li>Optimisation du montage financier</li><li>Attestation de financement si nécessaire</li></ul></div>
<div class="step-card"><div class="n">3</div><h3>Recherche de financement</h3><ul><li>Signature du mandat de recherche</li><li>Sollicitation simultanée de nos partenaires</li><li>Analyse comparative des propositions</li><li>Choix de l'établissement le plus adapté</li></ul></div>
<div class="step-card"><div class="n">4</div><h3>Finalisation et suivi</h3><ul><li>Vérification des offres de prêt</li><li>Coordination avec banque et notaire</li><li>Suivi jusqu'au déblocage des fonds</li></ul></div>
</div></div></section>
<section class="section dark" id="recrutement">{HEXWM}<div class="wrap split">
<div><span class="eyebrow">Recrutement</span><h2 style="margin-top:14px">Rejoignez KAIRN</h2><p class="lead" style="margin-top:16px">Courtier confirmé, conseiller bancaire, mandataire ou en reconversion : nous recrutons partout en France pour accompagner notre croissance.</p>
<div style="margin-top:24px">{ticks([("Liberté et structure","Votre autonomie, avec des outils performants et un cadre clair."),("Rémunération à la performance","Un commissionnement attractif, transparent et évolutif."),("Équipe et formation","Un vrai collectif et un accompagnement continu.")]).replace('<b>','<b style="color:#fff">').replace('<span>','<span style="color:#c3d3dc">').replace('class="ticks"','class="ticks" style="--x:0"')}</div></div>
<form class="lead-card" data-form="Candidature" novalidate><div class="form-body"><h2>Candidater</h2><p class="sub-title">Nous étudions chaque candidature avec attention.</p><div style="height:16px"></div>
<div class="row2"><div class="field"><label for="r-nom">Nom et prénom</label><input id="r-nom" name="nom" autocomplete="name" required></div><div class="field"><label for="r-tel">Téléphone</label><input id="r-tel" name="telephone" type="tel" required></div></div>
<div class="row2"><div class="field"><label for="r-mail">E-mail</label><input id="r-mail" name="email" type="email" required></div><div class="field"><label for="r-profil">Votre profil</label><select id="r-profil" name="profil"><option>Courtier expérimenté</option><option>Conseiller bancaire</option><option>Mandataire</option><option>Reconversion</option><option>Autre</option></select></div></div>
<div class="field"><label for="r-msg">Quelques mots sur vous</label><textarea id="r-msg" name="message"></textarea></div>
<input class="hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" id="r-rgpd" required> J'accepte que KAIRN conserve ma candidature pour la durée du recrutement.</label>
<div style="margin-top:16px"><button class="btn btn-primary" type="submit">Envoyer ma candidature {I["arrow"]}</button></div></div>
<div class="done" hidden>{I["done"]}<h3>Candidature reçue</h3><p class="fine">Nous revenons vers vous rapidement.</p></div><div class="fail done" hidden><h3>L'envoi n'a pas abouti</h3><p class="fine">Écrivez-nous à {MAIL}.</p></div></form>
</div></section>
{cta_band()}'''
page("cabinet.html","Le cabinet KAIRN · Courtiers à Lorient","KAIRN, cabinet de courtage en financement fondé par Brendan Le Roux à Lorient : 9 experts, 15 ans d'expérience, une méthode en 4 étapes. Recrutement ouvert.",cab)

# ---------- CONTACT ----------
opts = [("immo","Crédit immobilier"),("pro","Prêt professionnel"),("rachat","Regroupement de crédits"),("hypo","Prêt hypothécaire"),("assurance","Assurance de prêt"),("seniors","Viager hypothécaire ou réméré"),("autre","Autre demande")]
oh = "".join(f'<option data-key="{k}" value="{l}">{l}</option>' for k,l in opts)
contact = page_hero("Contact","Contact","Parlons de <span class='u'>votre projet</span>","Laissez-nous vos coordonnées : un expert vous rappelle sous 24 h ouvrées pour une première analyse gratuite et sans engagement.") + f'''
<section class="section"><div class="wrap split">
<form class="panel" data-form="Contact" novalidate style="box-shadow:var(--shadow)"><div class="form-body"><h2 style="font-size:1.2rem;letter-spacing:.06em">Demande d'étude gratuite</h2><div style="height:18px"></div>
<div class="field"><label for="c-besoin">Votre projet</label><select id="c-besoin" name="besoin">{oh}</select></div>
<div class="row2"><div class="field"><label for="c-nom">Nom et prénom</label><input id="c-nom" name="nom" autocomplete="name" required></div><div class="field"><label for="c-ville">Ville</label><input id="c-ville" name="ville" autocomplete="address-level2"></div></div>
<div class="row2"><div class="field"><label for="c-tel">Téléphone</label><input id="c-tel" name="telephone" type="tel" autocomplete="tel" required></div><div class="field"><label for="c-mail">E-mail</label><input id="c-mail" name="email" type="email" autocomplete="email"></div></div>
<div class="field"><label for="c-creneau">Quand vous rappeler ?</label><select id="c-creneau" name="creneau"><option>Dès que possible</option><option>Le matin (9h–12h)</option><option>L'après-midi (13h30–18h)</option><option>Le samedi</option></select></div>
<div class="field"><label for="c-msg">Votre projet en quelques mots (facultatif)</label><textarea id="c-msg" name="message" placeholder="Montant, type de bien, situation…"></textarea></div>
<input class="hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" id="c-rgpd" required> J'accepte d'être recontacté par KAIRN au sujet de mon projet. <a href="mentions-legales.html#confidentialite">Données personnelles</a></label>
<div style="margin-top:18px"><button class="btn btn-primary" type="submit">Être rappelé sous 24 h {I["arrow"]}</button></div>
<p class="fine">Gratuit et sans engagement. Aucun versement ne peut vous être demandé avant l'obtention de votre prêt.</p></div>
<div class="done" hidden>{I["done"]}<h3>Demande bien reçue</h3><p class="fine">Un expert KAIRN vous rappelle sous 24 h ouvrées.</p></div><div class="fail done" hidden><h3>L'envoi n'a pas abouti</h3><p class="fine">Appelez-nous au <span class="num">{PHONE}</span>.</p></div></form>
<div style="display:grid;gap:18px">
<div class="panel">{ticks([("Par téléphone", PHONE + " · appel non surtaxé"),("Par e-mail", MAIL),("À l'agence", ADDR),("Horaires","Lundi au vendredi 9h–12h / 13h30–18h · samedi sur rendez-vous")])}</div>
<div class="panel" style="background:var(--ink);color:#fff;border-color:var(--ink)"><span class="eyebrow" style="color:#a9c1cf">Nos engagements</span><ul class="ticks" style="margin-top:14px">
<li>{I["clock"]}<div><b style="color:#fff">Réponse sous 24 h ouvrées</b></div></li><li>{I["gift"]}<div><b style="color:#fff">Étude de financement gratuite</b></div></li><li>{I["shield"]}<div><b style="color:#fff">Calcul gratuit de votre économie d'assurance</b></div></li><li>{I["euro"]}<div><b style="color:#fff">Honoraires uniquement en cas de succès</b></div></li></ul></div>
<a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&query=8+mail+Jeanne+Villepreux-Power+56100+Lorient" rel="noopener">Voir l'agence sur la carte {I["arrow"]}</a>
</div></div></section>'''
page("contact.html","Contact · KAIRN, courtier à Lorient","Contactez KAIRN, courtier en financement à Lorient : étude gratuite, rappel sous 24 h ouvrées. 09 84 23 08 44, 8 mail Jeanne Villepreux-Power.",contact)

# ---------- MENTIONS ----------
T = lambda s: f'<span class="todo">{s}</span>'
ml = page_hero("Mentions légales","Informations légales","Mentions légales","Informations réglementaires sur KAIRN, nom commercial de BMB Financement.") .replace('<div class="hero-actions">','<div class="hero-actions" hidden>') + f'''
<section class="section"><div class="wrap legal-doc">
<section><h2>Éditeur du site</h2><p>BMB Financement, exerçant sous le nom commercial KAIRN. {T("forme juridique et capital social")}. Siège social : {ADDR}. RCS Lorient 800 090 607. Téléphone : {PHONE}. E-mail : {MAIL}. Directeur de la publication : Brendan Le Roux.</p></section>
<section><h2>Statut réglementaire</h2><p>BMB Financement est immatriculée au registre unique des intermédiaires en assurance, banque et finance (ORIAS) sous le n° 14003265, en qualité de courtier en opérations de banque et en services de paiement (COBSP). Cette immatriculation est vérifiable sur <a href="https://www.orias.fr" rel="noopener">www.orias.fr</a>. {T("ajouter le statut d'intermédiaire en assurance si le cabinet en dispose, pour l'assurance de prêt")}</p>
<p>Activité placée sous le contrôle de l'Autorité de contrôle prudentiel et de résolution (ACPR), 4 place de Budapest, CS 92459, 75436 Paris Cedex 09.</p>
<p>Responsabilité civile professionnelle et garantie financière : {T("assureur et numéro de contrat")}.</p>
<p>Partenaires bancaires : la liste des établissements avec lesquels le cabinet travaille est communiquée sur simple demande. {T("à confirmer : aucun établissement ne représente plus de 33 % du chiffre d'affaires")}</p>
<p><strong>Aucun versement, de quelque nature que ce soit, ne peut être exigé d'un particulier avant l'obtention d'un ou plusieurs prêts d'argent.</strong></p></section>
<section><h2>Réclamations et médiation</h2><p>Pour toute réclamation, écrivez à {MAIL} ou à l'adresse du siège. Nous accusons réception sous 10 jours ouvrables et répondons sous 2 mois au plus. En cas de désaccord, vous pouvez saisir gratuitement le médiateur : {T("nom et coordonnées du médiateur de la consommation")}.</p></section>
<section><h2>Hébergement</h2><p>{T("nom, adresse et téléphone de l'hébergeur (par exemple OVH SAS, 2 rue Kellermann, 59100 Roubaix)")}</p></section>
<section id="confidentialite"><h2>Données personnelles</h2><p>Les informations transmises via nos formulaires (nom, coordonnées, projet) sont utilisées uniquement pour étudier votre demande et vous recontacter. Elles sont destinées aux équipes de KAIRN et, avec votre accord, aux établissements sollicités pour votre financement. Elles sont conservées 3 ans après le dernier contact, puis supprimées.</p>
<p>Conformément au RGPD, vous disposez d'un droit d'accès, de rectification, d'effacement, d'opposition et de portabilité. Pour l'exercer : {MAIL}. Vous pouvez aussi saisir la CNIL (www.cnil.fr).</p>
<p>Ce site n'utilise pas de cookies publicitaires. {T("à mettre à jour si un outil de mesure d'audience est ajouté")}</p></section>
<section><h2>Propriété intellectuelle</h2><p>Le nom KAIRN, le logo et l'ensemble des contenus de ce site sont la propriété de BMB Financement. Toute reproduction sans autorisation est interdite.</p></section>
<section><h2>Simulateurs</h2><p>Les résultats des simulateurs sont indicatifs et ne constituent ni une offre de prêt ni un engagement. Seule l'étude de votre dossier par un établissement prêteur permet de déterminer les conditions définitives.</p></section>
</div></section>'''
page("mentions-legales.html","Mentions légales · KAIRN","Mentions légales, statut ORIAS, médiation et politique de données personnelles de KAIRN (BMB Financement).",ml)
