# ---------- PRÊT HYPOTHÉCAIRE PAR GRANDE VILLE (activité nationale, suivi à distance) ----------
# Contenu propre à chaque ville ; aucun chiffre de marché inventé.

HYPO_VILLES = [
 dict(f="pret-hypothecaire-paris.html", ville="Paris", zone="Paris et l'Île-de-France",
  lead="Propriétaire à Paris ou en Île-de-France ? Votre bien a souvent pris beaucoup de valeur. Le prêt hypothécaire permet de mobiliser une partie de cette valeur sans vendre.",
  h="Un patrimoine de valeur, des besoins de financement variés",
  p="<p>En Île-de-France, la valeur d'un appartement ou d'une maison représente souvent l'essentiel du patrimoine d'un ménage. C'est une garantie solide pour la banque, même quand les revenus sont irréguliers : chefs d'entreprise, professions libérales, indépendants ou retraités.</p><p>Nous montons ces dossiers à distance, de l'estimation du bien à la signature chez votre notaire. Rachat de soulte après une séparation, trésorerie pour une entreprise, financement d'un nouvel achat avant la vente : chaque projet est présenté aux banques qui savent l'étudier.</p>",
  cas=[("Rachat de soulte","Garder le logement familial après un divorce ou une succession."),("Trésorerie d'entreprise","Mobiliser son patrimoine personnel pour son activité."),("Achat avant vente","Financer le nouveau bien en attendant de vendre."),("Prêt viager hypothécaire","Pour les seniors : des liquidités sans mensualités.")],
  communes="Paris, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne, Yvelines, Essonne, Val-d'Oise, Seine-et-Marne."),
 dict(f="pret-hypothecaire-lyon.html", ville="Lyon", zone="Lyon et la métropole lyonnaise",
  lead="Propriétaire à Lyon, Villeurbanne ou dans la métropole ? Votre bien peut garantir un prêt pour vos projets personnels ou professionnels, sans avoir à le vendre.",
  h="Entrepreneurs, familles et propriétaires bailleurs",
  p="<p>Lyon compte beaucoup de chefs d'entreprise et d'indépendants dont les revenus varient d'une année à l'autre. Pour eux, un prêt classique est parfois difficile à obtenir, alors que leur patrimoine immobilier est solide. Le prêt hypothécaire s'appuie d'abord sur la valeur du bien.</p><p>Nous l'utilisons aussi pour les propriétaires bailleurs qui veulent financer des travaux ou un nouvel investissement, et pour regrouper des crédits avec une garantie qui améliore les conditions.</p>",
  cas=[("Trésorerie professionnelle","Financer le développement de son entreprise."),("Travaux","Rénover un bien locatif ou sa résidence principale."),("Regroupement avec garantie","Une seule mensualité, de meilleures conditions."),("Nouvel investissement","S'appuyer sur un bien pour en acheter un autre.")],
  communes="Lyon, Villeurbanne, Vénissieux, Caluire-et-Cuire, Bron, Vaulx-en-Velin, Écully, Tassin-la-Demi-Lune, Oullins-Pierre-Bénite, et tout le Rhône."),
 dict(f="pret-hypothecaire-marseille.html", ville="Marseille", zone="Marseille et les Bouches-du-Rhône",
  lead="Propriétaire à Marseille, Aix-en-Provence ou dans les Bouches-du-Rhône ? Le prêt hypothécaire transforme une partie de la valeur de votre bien en financement.",
  h="Mobiliser la valeur de son bien, sans le vendre",
  p="<p>Une maison à rénover, un appartement transmis par succession, une résidence secondaire sur la côte : autour de Marseille, beaucoup de propriétaires ont un patrimoine important mais peu de liquidités. Le prêt hypothécaire permet d'en tirer un financement en gardant le bien.</p><p>Nous étudions la valeur de votre bien, votre capacité de remboursement et le projet, puis nous présentons le dossier aux banques spécialisées. Tout se fait à distance, avec un conseiller dédié.</p>",
  cas=[("Succession","Racheter la part des cohéritiers et garder le bien."),("Travaux","Rénover ou agrandir sans vendre."),("Trésorerie","Un besoin personnel ou professionnel."),("Prêt viager hypothécaire","Pour les seniors : des liquidités sans mensualités.")],
  communes="Marseille, Aix-en-Provence, Aubagne, La Ciotat, Martigues, Marignane, Vitrolles, Salon-de-Provence, Cassis."),
 dict(f="pret-hypothecaire-toulouse.html", ville="Toulouse", zone="Toulouse et la Haute-Garonne",
  lead="Propriétaire à Toulouse ou en Haute-Garonne ? Votre bien peut servir de garantie pour financer vos projets, regrouper vos crédits ou soutenir votre activité.",
  h="Quand le patrimoine compte plus que la fiche de paie",
  p="<p>Une banque classique regarde d'abord les revenus. Le prêt hypothécaire regarde d'abord le bien. C'est une solution pour les indépendants, les créateurs d'entreprise ou les ménages dont les revenus ont baissé, mais qui sont propriétaires d'un bien de valeur.</p><p>Nous montons le dossier complet, de l'estimation à l'offre de prêt, et nous vérifions avec vous que la mensualité reste supportable. Le suivi se fait par téléphone, en visio et via notre espace client sécurisé.</p>",
  cas=[("Regroupement de crédits","Alléger les mensualités grâce à la garantie."),("Création d'entreprise","Financer un projet avec son patrimoine."),("Rachat de soulte","Garder le logement après une séparation."),("Travaux","Rénover, agrandir, mettre aux normes.")],
  communes="Toulouse, Colomiers, Tournefeuille, Blagnac, Muret, Balma, L'Union, Saint-Orens-de-Gameville, Castanet-Tolosan, et toute la Haute-Garonne."),
 dict(f="pret-hypothecaire-nice.html", ville="Nice", zone="Nice et la Côte d'Azur",
  lead="Propriétaire à Nice, Cannes, Antibes ou sur la Côte d'Azur ? Le prêt hypothécaire et le viager hypothécaire permettent de profiter de la valeur de votre bien sans le vendre.",
  h="Seniors, résidences secondaires et patrimoine de valeur",
  p="<p>Sur la Côte d'Azur, beaucoup de propriétaires sont des retraités dont le logement vaut bien plus que leurs revenus ne le laissent penser. Le <a href='guide-pret-viager-hypothecaire.html'>prêt viager hypothécaire</a> leur permet d'obtenir des liquidités sans mensualités, le prêt étant remboursé à la vente ou à la succession.</p><p>Pour les plus jeunes, le prêt hypothécaire classique finance des travaux, une trésorerie ou un nouvel achat. Nous comparons les deux solutions avec vous, et avec vos proches si vous le souhaitez.</p>",
  cas=[("Prêt viager hypothécaire","Des liquidités sans mensualités, pour les seniors."),("Résidence secondaire","Mobiliser sa valeur pour un autre projet."),("Aider ses enfants","Financer un apport ou une donation."),("Travaux","Adapter son logement, rénover.")],
  communes="Nice, Cannes, Antibes, Cagnes-sur-Mer, Grasse, Menton, Saint-Laurent-du-Var, Vence, Mandelieu-la-Napoule, et tout le littoral des Alpes-Maritimes."),
 dict(f="pret-hypothecaire-nantes.html", ville="Nantes", zone="Nantes et la Loire-Atlantique",
  lead="Propriétaire à Nantes, Saint-Nazaire ou en Loire-Atlantique ? Votre bien peut garantir un prêt pour vos projets. Nous sommes à Lorient, à deux heures, et tout se fait à distance.",
  h="Un courtier breton pour les propriétaires nantais",
  p="<p>Nantes est la grande ville la plus proche de notre agence, en dehors de la Bretagne. Rachat de soulte, financement de travaux, trésorerie pour une entreprise ou regroupement de crédits : le prêt hypothécaire répond à des situations très différentes.</p><p>Nous estimons avec vous la valeur de votre bien, calculons le montant mobilisable et présentons le dossier aux banques spécialisées, jusqu'à la signature chez votre notaire.</p>",
  cas=[("Rachat de soulte","Garder le logement après une séparation."),("Trésorerie","Un besoin personnel ou professionnel."),("Travaux","Rénovation énergétique, extension."),("Regroupement avec garantie","Une seule mensualité, de meilleures conditions.")],
  communes="Nantes, Saint-Herblain, Rezé, Saint-Sébastien-sur-Loire, Orvault, Vertou, Carquefou, Saint-Nazaire, La Baule-Escoublac, Guérande."),
 dict(f="pret-hypothecaire-bordeaux.html", ville="Bordeaux", zone="Bordeaux et la Gironde",
  lead="Propriétaire à Bordeaux, Mérignac ou sur le bassin d'Arcachon ? Le prêt hypothécaire vous permet de financer vos projets en vous appuyant sur votre bien.",
  h="Investisseurs, familles et propriétaires du bassin",
  p="<p>Autour de Bordeaux, beaucoup de propriétaires ont vu la valeur de leur bien progresser, en ville comme sur le bassin d'Arcachon. Ce patrimoine peut garantir un prêt pour un nouvel investissement locatif, des travaux ou une aide à ses enfants.</p><p>Nous étudions votre situation globale, comparons prêt hypothécaire, prêt relais et regroupement de crédits, et vous recommandons la solution la plus adaptée. Tout le suivi se fait à distance.</p>",
  cas=[("Investissement locatif","S'appuyer sur un bien pour en acheter un autre."),("Aider ses enfants","Financer un apport sans vendre."),("Prêt relais hypothécaire","Acheter avant d'avoir vendu."),("Travaux","Rénover ou agrandir.")],
  communes="Bordeaux, Mérignac, Pessac, Talence, Bègles, Villenave-d'Ornon, Le Bouscat, Arcachon, La Teste-de-Buch, Libourne."),
 dict(f="pret-hypothecaire-lille.html", ville="Lille", zone="Lille et la métropole lilloise",
  lead="Propriétaire à Lille, Roubaix, Tourcoing ou dans la métropole ? Votre bien peut garantir un prêt pour regrouper vos crédits, financer des travaux ou votre activité.",
  h="Retrouver de la marge grâce à son bien",
  p="<p>Quand les crédits s'accumulent, regrouper ses prêts avec une garantie hypothécaire permet souvent d'obtenir une mensualité plus légère et de meilleures conditions qu'un regroupement sans garantie. C'est l'une des utilisations les plus fréquentes du prêt hypothécaire.</p><p>Il sert aussi à financer des travaux dans les maisons anciennes de la métropole, ou à soutenir une activité professionnelle. Nous montons le dossier à distance et vérifions avec vous que chaque mensualité reste supportable.</p>",
  cas=[("Regroupement avec garantie","Une seule mensualité, plus légère."),("Travaux","Rénover une maison ancienne."),("Trésorerie professionnelle","Soutenir son activité."),("Rachat de soulte","Garder le logement familial.")],
  communes="Lille, Roubaix, Tourcoing, Villeneuve-d'Ascq, Marcq-en-Barœul, Lambersart, La Madeleine, Croix, Wasquehal, et tout le Nord."),
 dict(f="pret-hypothecaire-montpellier.html", ville="Montpellier", zone="Montpellier et l'Hérault",
  lead="Propriétaire à Montpellier ou dans l'Hérault ? Le prêt hypothécaire et le viager hypothécaire permettent de mobiliser la valeur de votre bien.",
  h="Des solutions pour chaque étape de la vie",
  p="<p>Montpellier attire à la fois des actifs, des étudiants et des retraités. Pour un actif, le prêt hypothécaire finance un projet ou regroupe des crédits. Pour un senior, le <a href='guide-pret-viager-hypothecaire.html'>prêt viager hypothécaire</a> apporte des liquidités sans mensualités.</p><p>Nous comparons les solutions avec vous, montons le dossier complet et vous accompagnons jusqu'à la signature, à distance et avec un conseiller dédié.</p>",
  cas=[("Prêt viager hypothécaire","Pour les seniors : des liquidités sans mensualités."),("Regroupement de crédits","Alléger les mensualités."),("Investissement locatif","Logement étudiant, location meublée."),("Trésorerie","Un besoin personnel ou professionnel.")],
  communes="Montpellier, Castelnau-le-Lez, Lattes, Pérols, Mauguio, Saint-Jean-de-Védas, Juvignac, Sète, Béziers, et tout l'Hérault."),
 dict(f="pret-hypothecaire-strasbourg.html", ville="Strasbourg", zone="Strasbourg et l'Alsace",
  lead="Propriétaire à Strasbourg ou en Alsace ? Votre bien peut garantir un prêt pour vos projets, sans avoir à le vendre. Nous vous accompagnons entièrement à distance.",
  h="Un financement adossé à votre patrimoine",
  p="<p>Le prêt hypothécaire s'adresse à tous les propriétaires qui ont besoin de financement et dont le bien a de la valeur : travaux, rachat de soulte, trésorerie, regroupement de crédits ou nouvel achat. La banque s'appuie sur la valeur du bien, en général jusqu'à 70 %.</p><p>Nous estimons avec vous le montant mobilisable, préparons le dossier et le présentons aux banques qui maîtrisent ce type de financement. Votre notaire reste celui de votre choix.</p>",
  cas=[("Travaux","Rénover, agrandir, adapter son logement."),("Rachat de soulte","Garder le bien après une séparation."),("Trésorerie","Un besoin personnel ou professionnel."),("Regroupement avec garantie","Une seule mensualité, de meilleures conditions.")],
  communes="Strasbourg, Schiltigheim, Illkirch-Graffenstaden, Lingolsheim, Bischheim, Haguenau, Sélestat, Colmar, Mulhouse."),
]


# Questions propres à chaque ville (mécanismes généraux, aucun chiffre de marché)
FAQ_VILLE = {
 "pret-hypothecaire-paris.html": [
  ("Peut-on financer un rachat de soulte à Paris avec un prêt hypothécaire ?","Oui. Après un divorce ou une succession, la banque finance la part due à l'autre propriétaire et prend une garantie sur le logement que vous conservez. Le notaire rédige l'acte de partage et inscrit la garantie le même jour."),
  ("Un dirigeant aux revenus irréguliers peut-il emprunter sur son bien ?","Oui, c'est l'un des cas les plus fréquents. La banque regarde d'abord la valeur du bien et le patrimoine, puis vérifie que la mensualité reste supportable sur la durée. Nous présentons vos bilans et votre situation de façon claire pour que le dossier soit compris.")],
 "pret-hypothecaire-lyon.html": [
  ("Un chef d'entreprise lyonnais peut-il garantir un prêt avec son bien personnel ?","Oui. Le prêt hypothécaire peut financer un besoin professionnel tout en étant garanti par un bien privé, résidence principale ou bien locatif. Nous vérifions avec vous la répartition des risques entre votre patrimoine et votre société avant de déposer le dossier."),
  ("Un bien locatif peut-il servir de garantie ?","Oui. Un appartement loué, même encore en partie financé, peut garantir un nouveau prêt. Le montant mobilisable dépend de sa valeur, du crédit restant dû et des loyers perçus.")],
 "pret-hypothecaire-marseille.html": [
  ("Comment racheter la part de ses cohéritiers ?","Le prêt hypothécaire finance la soulte versée aux cohéritiers, et le bien hérité sert de garantie. Le notaire chargé de la succession signe en même temps le partage et le prêt."),
  ("Une résidence secondaire peut-elle garantir un prêt ?","Oui. Tout bien dont vous êtes propriétaire peut servir de garantie, y compris une maison de vacances. Cela permet de financer un projet sans toucher à votre résidence principale.")],
 "pret-hypothecaire-toulouse.html": [
  ("Peut-on regrouper ses crédits avec une garantie hypothécaire ?","Oui. Quand vous êtes propriétaire, la garantie sur votre bien rassure la banque et permet souvent d'obtenir une durée plus longue et un taux plus doux qu'un regroupement sans garantie. Nous comparons toujours les deux options."),
  ("Je viens de créer mon entreprise, puis-je emprunter ?","Les banques demandent en général plusieurs bilans pour un prêt classique. Avec une garantie sur un bien de valeur, certaines acceptent d'étudier un dossier plus tôt, à condition que le remboursement reste réaliste.")],
 "pret-hypothecaire-nice.html": [
  ("Comment fonctionne le prêt viager hypothécaire ?","Vous recevez un capital ou des versements sans rembourser de mensualités. Le prêt et les intérêts sont remboursés à la vente du bien ou lors de la succession, et la dette ne peut jamais dépasser la valeur du bien au moment du remboursement."),
  ("Mes enfants doivent-ils être informés ?","Rien ne l'impose, mais nous le conseillons. Le prêt sera remboursé sur la valeur du bien au moment de la succession : en parler en amont évite les mauvaises surprises. Vos proches peuvent participer aux rendez-vous si vous le souhaitez.")],
 "pret-hypothecaire-nantes.html": [
  ("Peut-on vous rencontrer en agence depuis Nantes ?","Oui. Notre agence est à Lorient, à environ deux heures de route. La plupart des clients nantais préfèrent tout faire à distance, mais nous vous recevons volontiers si vous le souhaitez."),
  ("Combien de temps faut-il pour obtenir les fonds ?","Il faut compter l'étude du dossier, l'estimation du bien, l'offre de la banque puis le délai de réflexion légal avant la signature chez le notaire. Nous vous donnons un calendrier précis dès l'étude.")],
 "pret-hypothecaire-bordeaux.html": [
  ("Peut-on aider ses enfants à acheter grâce à son bien ?","Oui. Le prêt hypothécaire permet de financer un apport ou une donation sans vendre. Nous vérifions avec vous que la mensualité reste compatible avec vos revenus, et nous vous conseillons de faire le point avec votre notaire sur la donation."),
  ("Quelle différence entre prêt relais et prêt hypothécaire ?","Le prêt relais finance un achat en attendant la vente d'un bien précis, sur une durée courte. Le prêt hypothécaire s'appuie sur un bien que vous gardez, sur une durée plus longue. Nous comparons les deux selon votre projet.")],
 "pret-hypothecaire-lille.html": [
  ("Le regroupement avec garantie est-il réservé aux gros patrimoines ?","Non. Il suffit d'être propriétaire d'un bien dont la valeur couvre le montant regroupé. C'est souvent la solution pour réunir crédits immobiliers, prêts personnels et crédits renouvelables en une seule mensualité."),
  ("Peut-on financer des travaux dans une maison ancienne ?","Oui. Le prêt hypothécaire finance la rénovation, l'isolation ou l'extension, et la maison sert elle-même de garantie. Les travaux peuvent aussi augmenter sa valeur.")],
 "pret-hypothecaire-montpellier.html": [
  ("Prêt hypothécaire ou viager hypothécaire : comment choisir ?","Le prêt hypothécaire se rembourse par mensualités, il convient si vos revenus le permettent. Le viager hypothécaire ne demande aucune mensualité et se rembourse à la vente ou à la succession : il s'adresse surtout aux seniors. Nous étudions les deux avec vous."),
  ("Un logement étudiant peut-il garantir un nouveau prêt ?","Oui, comme tout bien locatif. Sa valeur, le crédit restant dû et les loyers perçus déterminent le montant que vous pouvez mobiliser.")],
 "pret-hypothecaire-strasbourg.html": [
  ("Le prêt hypothécaire fonctionne-t-il autrement en Alsace ?","Le principe est le même, mais l'Alsace et la Moselle ont leur propre publicité foncière : l'hypothèque est inscrite au Livre foncier et non au service de la publicité foncière. Votre notaire s'en charge, nous en tenons compte dans le calendrier."),
  ("Peut-on emprunter sans vendre pour racheter une soulte ?","Oui. La banque finance la part due à votre ex-conjoint ou à vos cohéritiers, et le bien que vous conservez sert de garantie.")],
}

def hypo_schema(v, faqs):
    import json as _j, re as _r
    url="https://kairn-finance.com/"+v["f"]
    d={"@context":"https://schema.org","@graph":[
      {"@type":"Service","@id":url+"#service","name":"Prêt hypothécaire à "+v["ville"],"serviceType":"Courtage en prêt hypothécaire","url":url,
       "provider":{"@id":"https://kairn-finance.com/#kairn"},
       "areaServed":[c.strip().rstrip(".") for c in v["communes"].split(",") if "tout" not in c][:12]},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://kairn-finance.com/"},{"@type":"ListItem","position":2,"name":"Prêt hypothécaire","item":"https://kairn-finance.com/pret-hypothecaire.html"},{"@type":"ListItem","position":3,"name":v["ville"],"item":url}]},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":_r.sub("<[^>]+>","",q),"acceptedAnswer":{"@type":"Answer","text":_r.sub("<[^>]+>","",a)}} for q,a in faqs]}]}
    return '<script type="application/ld+json">'+_j.dumps(d,ensure_ascii=False)+'</script>'

def hypo_ville_links(exclude=None):
    return "".join(f'<a class="chip" href="{v["f"]}">{v["ville"]}</a>' for v in HYPO_VILLES if v["f"]!=exclude)

for v in HYPO_VILLES:
    faqs=[(f"Peut-on faire un prêt hypothécaire à {v['ville']} avec un courtier basé à Lorient ?",f"Oui. Le prêt hypothécaire est l'une de nos spécialités et nous l'accompagnons partout en France. Tout se fait par téléphone, en visio et via notre espace client sécurisé, et la signature a lieu chez le notaire de votre choix, à {v['ville']} ou ailleurs."),
          *FAQ_VILLE[v["f"]],
          ("Combien peut-on emprunter ?","En général jusqu'à 70 % de la valeur du bien, moins les crédits qui pèsent déjà dessus. Le montant final dépend aussi de votre capacité de remboursement et de la nature du bien."),
          ("Quels sont vos honoraires ?","L'étude est gratuite. Nos honoraires ne sont dus qu'une fois votre financement obtenu, et ils sont annoncés dès le départ. Aucun versement ne peut être exigé avant.")]
    body = page_hero(f'<a href="pret-hypothecaire.html">Prêt hypothécaire</a> / {v["ville"]}', f'Prêt hypothécaire · {v["ville"]}', f"Prêt hypothécaire <span class='u'>à {v['ville']}</span>", v["lead"]) + f'''
<section class="section"><div class="wrap split">
<div class="prose"><span class="eyebrow">{v["zone"]}</span><h2 style="color:var(--text)">{v["h"]}</h2>{v["p"]}</div>
<div class="panel">{ticks(v["cas"])}</div></div></section>
<section class="section white"><div class="wrap">
<div class="section-head"><span class="eyebrow">Simulateur</span><h2>Combien pouvez-vous mobiliser ?</h2></div>{sim_hypo("h"+v["f"][18:22])}</div></section>
<section class="section"><div class="wrap split">
<div class="section-head"><span class="eyebrow">Notre méthode</span><h2>Un dossier monté de A à Z, à distance</h2><p class="lead">Estimation du bien, étude de faisabilité, mise en concurrence des banques spécialisées, puis suivi jusqu'à la signature chez votre notaire.</p>
<div><a class="btn btn-outline" href="guide-pret-hypothecaire.html">Lire notre guide du prêt hypothécaire {I["arrow"]}</a></div></div>
<div class="panel"><h3 style="font-size:1rem;letter-spacing:.06em">Secteur couvert</h3><p style="margin-top:10px;color:var(--muted)">{v["communes"]}</p>
<h3 style="font-size:1rem;letter-spacing:.06em;margin-top:22px">Ailleurs en France</h3><div class="chips" style="margin-top:10px">{hypo_ville_links(v["f"])}</div></div>
</div></section>
<section class="section white"><div class="wrap split"><div class="section-head"><span class="eyebrow">Questions fréquentes</span><h2>Vos questions à {v["ville"]}</h2></div>{faq(faqs)}</div></section>
<section class="section" style="padding-block:0 8px"><div class="wrap"><p class="warning">Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.</p></div></section>
{cta_band(f"Un projet de prêt hypothécaire à {v['ville']} ?")}'''
    page(v["f"], f"Prêt hypothécaire à {v['ville']} · Courtier KAIRN", f"Prêt hypothécaire à {v['ville']} : mobilisez la valeur de votre bien sans le vendre. Courtier spécialisé, étude gratuite, dossier suivi à distance jusqu'à la signature.", body, extra_head=hypo_schema(v, faqs))
