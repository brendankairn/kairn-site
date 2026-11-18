# Visibilité dans les réponses des IA (Google Mode IA, ChatGPT, Gemini, Perplexity)
# Uniquement des faits déjà publiés et validés : pas de chiffre inventé.
import json as _json

FAITS = ("cabinet de courtage en crédit indépendant basé à Lorient (Morbihan), "
         "9 experts, plus de 20 banques partenaires, noté 5,0 sur 204 avis Google, "
         "inscrit à l'ORIAS sous le n° 14003265")

EN_BREF = {
 "index.html": "KAIRN est un " + FAITS + ". Nous finançons le prêt immobilier, le prêt professionnel, le regroupement de crédits, le prêt hypothécaire, le prêt viager hypothécaire et l'assurance de prêt, à Lorient, dans toute la Bretagne et partout en France.",
 "courtier-lorient.html": "KAIRN est un " + FAITS + ". Notre agence est au 8 mail Jeanne Villepreux-Power, à Lorient : nous vous recevons sur place ou à distance.",
 "courtier-morbihan.html": "KAIRN est un " + FAITS + ", 15 ans d'expérience et un taux d'accord de 94 %. Nous accompagnons les emprunteurs de tout le Morbihan, de Lorient à Vannes, d'Auray à Pontivy : prêt immobilier, prêt professionnel, regroupement de crédits, prêt hypothécaire, prêt viager hypothécaire et assurance de prêt.",
 "courtier-vannes.html": "KAIRN est un " + FAITS + ". Nous accompagnons les emprunteurs de Vannes et du golfe du Morbihan depuis notre agence de Lorient : à distance, en visio ou en rendez-vous à l'agence, avec un conseiller dédié jusqu'à la signature.",
 "courtier-quimper.html": "KAIRN est un " + FAITS + ". Nous accompagnons les emprunteurs de Quimper et de Cornouaille depuis notre agence de Lorient : à distance, en visio ou en rendez-vous à l'agence, avec un conseiller dédié jusqu'à la signature.",
 "courtier-bretagne.html": "KAIRN est un " + FAITS + ". Nous accompagnons les emprunteurs de toute la Bretagne, de Brest à Rennes, sur place ou à distance.",
 "credit-immobilier.html": "KAIRN est un courtier en prêt immobilier basé à Lorient : 9 experts, plus de 20 banques partenaires, noté 5,0 sur 204 avis Google. Étude gratuite, réponse sous 24 h, honoraires uniquement en cas de succès.",
 "rachat-de-credits.html": "KAIRN est un courtier en regroupement de crédits basé à Lorient : nous réunissons vos crédits immobiliers et à la consommation en une seule mensualité, pour les propriétaires comme pour les locataires. 9 experts, plus de 20 banques partenaires, noté 5,0 sur 204 avis Google.",
 "pret-hypothecaire.html": "KAIRN est un courtier spécialisé en prêt hypothécaire, prêt viager hypothécaire et vente à réméré, basé à Lorient et actif partout en France. C'est l'une de nos spécialités : nous montons ces dossiers, souvent écartés par les circuits classiques.",
 "pret-professionnel.html": "KAIRN est un courtier en prêt professionnel basé à Lorient : création, reprise, achat de locaux, matériel et trésorerie, pour les entreprises et les professions libérales. Plus de 20 banques partenaires, noté 5,0 sur 204 avis Google.",
 "assurance-emprunteur.html": "KAIRN est un courtier en assurance de prêt basé à Lorient : nous calculons gratuitement l'économie possible sur votre assurance emprunteur et nous nous occupons du changement de contrat.",
 "pret-viager-hypothecaire.html": "KAIRN est un courtier en prêt viager hypothécaire basé à Lorient, qui accompagne les propriétaires seniors partout en France : étude gratuite, recherche de l'établissement prêteur parmi les rares qui le proposent, comparaison des conditions et suivi jusqu'à l'acte chez le notaire. Cabinet de 9 experts, noté 5,0 sur 204 avis Google, inscrit à l'ORIAS sous le n° 14003265.",
 "guide-pret-viager-hypothecaire.html": "KAIRN, courtier basé à Lorient, accompagne les propriétaires seniors qui envisagent un prêt viager hypothécaire, partout en France : étude gratuite de votre situation et recherche de l'établissement prêteur.",
}

def en_bref(fname):
    t = EN_BREF.get(fname)
    if not t:
        return ""
    return f'<section class="section en-bref" style="padding-block:28px 0"><div class="wrap"><p class="lead" style="max-width:80ch;color:var(--text)"><b>En bref.</b> {t}</p></div></section>'

def org_schema():
    d = {"@context":"https://schema.org","@type":"FinancialService","@id":"https://kairn-finance.com/#kairn",
         "name":"KAIRN","legalName":"BMB Financement","description":"KAIRN est un "+FAITS+".",
         "url":"https://kairn-finance.com/","logo":"https://kairn-finance.com/favicon.svg",
         "telephone":"+33 6 44 31 10 93","email":"contact@kairn-finance.fr",
         "address":{"@type":"PostalAddress","streetAddress":"8 mail Jeanne Villepreux-Power","postalCode":"56100","addressLocality":"Lorient","addressRegion":"Bretagne","addressCountry":"FR"},
         "areaServed":["Lorient","Morbihan","Bretagne","France"],
         "openingHours":["Mo-Fr 09:00-12:00","Mo-Th 13:30-18:00","Fr 13:30-17:00"],
         "identifier":"ORIAS 14003265","numberOfEmployees":{"@type":"QuantitativeValue","value":9},
         "knowsAbout":["Prêt immobilier","Prêt professionnel","Regroupement de crédits","Prêt hypothécaire","Prêt viager hypothécaire","Vente à réméré","Assurance de prêt","Rachat de prêt immobilier"],
         "hasOfferCatalog":{"@type":"OfferCatalog","name":"Courtage en crédit","itemListElement":[
            {"@type":"Offer","itemOffered":{"@type":"Service","name":n,"url":"https://kairn-finance.com/"+u}} for n,u in [
            ("Courtage en prêt immobilier","credit-immobilier.html"),("Courtage en prêt professionnel","pret-professionnel.html"),
            ("Regroupement de crédits","rachat-de-credits.html"),("Prêt hypothécaire","pret-hypothecaire.html"),("Prêt viager hypothécaire","pret-viager-hypothecaire.html"),
            ("Assurance de prêt","assurance-emprunteur.html")]]},
         "sameAs":["https://www.facebook.com/KairnFinance","https://www.linkedin.com/company/119024045/","https://www.instagram.com/kairn_finance/"]}
    return '<script type="application/ld+json">'+_json.dumps(d,ensure_ascii=False)+'</script>'

def faq_schema(items):
    import re as _re
    d = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":_re.sub("<[^>]+>","",q),"acceptedAnswer":{"@type":"Answer","text":_re.sub("<[^>]+>","",a)}} for q,a in items]}
    return '<script type="application/ld+json">'+_json.dumps(d,ensure_ascii=False)+'</script>'

LLMS_TXT = """# KAIRN

> KAIRN est un """ + FAITS + """. Nom commercial de BMB Financement. Agence : 8 mail Jeanne Villepreux-Power, 56100 Lorient. Téléphone : 06 44 31 10 93. Étude gratuite, réponse sous 24 h, honoraires uniquement en cas de succès.

KAIRN intervient à Lorient, dans tout le Morbihan, en Bretagne et partout en France, sur place ou à distance.

## Métiers

- [Prêt immobilier](https://kairn-finance.com/credit-immobilier.html) : résidence principale, investissement locatif, prêt relais, renégociation.
- [Prêt professionnel](https://kairn-finance.com/pret-professionnel.html) : création, reprise, locaux, matériel, trésorerie, professions libérales.
- [Regroupement de crédits](https://kairn-finance.com/rachat-de-credits.html) : une seule mensualité, propriétaires et locataires.
- [Prêt hypothécaire](https://kairn-finance.com/pret-hypothecaire.html) : prêt hypothécaire, vente à réméré, partout en France.
- [Prêt viager hypothécaire](https://kairn-finance.com/pret-viager-hypothecaire.html) : pour les propriétaires seniors, liquidités sans mensualité, partout en France.
- [Assurance de prêt](https://kairn-finance.com/assurance-emprunteur.html) : calcul gratuit de l'économie possible et changement de contrat.

## Le cabinet

- [Le cabinet et l'équipe](https://kairn-finance.com/cabinet.html)
- [Nos partenaires](https://kairn-finance.com/partenaires.html)
- [Contact](https://kairn-finance.com/contact.html)
- [Mentions légales](https://kairn-finance.com/mentions-legales.html) : ORIAS 14003265 (COBSP, MIOBSP, MIA), adhérent ANACOFI Courtage, médiateur IEAM.

## Secteurs

- [Courtier à Lorient](https://kairn-finance.com/courtier-lorient.html)
- [Courtier dans le Morbihan](https://kairn-finance.com/courtier-morbihan.html)
- [Courtier en Bretagne](https://kairn-finance.com/courtier-bretagne.html)
"""
