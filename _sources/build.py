import os, sys, shutil
OUT = sys.argv[1]; MODE = sys.argv[2]  # MODE: "site" (fichiers complets) ou "artifact" (index sans squelette)
os.makedirs(OUT, exist_ok=True)

PHONE = "09 84 23 08 44"; TEL = "+33984230844"; MAIL = "contact@kairn-finance.fr"
ADDR = "8 mail Jeanne Villepreux-Power, 56100 Lorient"

def ic(path, w=1.8):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
I = {
 "home": ic('<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>'),
 "pro": ic('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2"/><path d="M3 13h18"/>'),
 "merge": ic('<path d="M6 3v6a6 6 0 006 6h0a6 6 0 006-6V3"/><path d="M12 15v6"/>'),
 "key": ic('<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9"/><path d="M17 6l3 3"/>'),
 "shield": ic('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>'),
 "plus": ic('<circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/>'),
 "check": ic('<path d="M5 12l5 5L20 7"/>', 2.4),
 "x": ic('<path d="M7 7l10 10M17 7L7 17"/>', 2),
 "clock": ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "gift": ic('<path d="M4 11h16v9H4z"/><path d="M2 7h20v4H2zM12 7v13"/><path d="M12 7c-2-4-6-3-5 0M12 7c2-4 6-3 5 0"/>'),
 "pin": ic('<path d="M12 21s-7-6.5-7-12a7 7 0 0114 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>'),
 "phone": ic('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>'),
 "euro": ic('<path d="M17 6a7 7 0 100 12"/><path d="M4 10h9M4 14h9"/>'),
 "done": ic('<circle cx="12" cy="12" r="10"/><path d="M7 12l3.5 3.5L17 9"/>', 2),
 "arrow": '<span class="arrow" aria-hidden="true">→</span>',
}
LOGO = '''<svg viewBox="0 0 100 112" aria-hidden="true"><path d="M50 4l42 24v56L50 108 8 84V28z" fill="none" stroke="currentColor" stroke-width="7"/><path d="M33 34v44" stroke="currentColor" stroke-width="8"/><path d="M33 58l19-22" stroke="currentColor" stroke-width="8"/><path d="M41 60l15 20" stroke="#7091a6" stroke-width="8"/><circle cx="64" cy="48" r="5" fill="currentColor"/></svg>'''
HEXWM = '<svg class="hexwatermark" viewBox="0 0 100 112" aria-hidden="true"><path d="M50 4l42 24v56L50 108 8 84V28z" fill="none" stroke="#fff" stroke-width="3"/><path d="M33 34v44M33 58l19-22M41 60l15 20" stroke="#fff" stroke-width="4"/></svg>'

EXPERTISES = [
 ("credit-immobilier.html","home","Crédit immobilier","Particuliers","Résidence principale, investissement locatif, prêt relais, renégociation. Nous présentons votre dossier à plusieurs banques et négocions taux, assurance et frais.","immo"),
 ("pret-professionnel.html","pro","Prêt professionnel","Professionnels","Création, reprise, locaux, matériel, trésorerie. Un prévisionnel défendable et un dossier présenté aux bons interlocuteurs.","pro"),
 ("rachat-de-credits.html","merge","Regroupement de crédits","Particuliers et pros","Plusieurs crédits réunis en une seule mensualité, adaptée à votre budget. Avec ou sans garantie immobilière.","rachat"),
 ("pret-hypothecaire.html","key","Prêt hypothécaire","Propriétaires","Votre bien finance vos projets sans le vendre : travaux, trésorerie, rachat de soulte, besoin patrimonial.","hypo"),
 ("assurance-emprunteur.html","shield","Assurance de prêt","Tous les emprunteurs","Mêmes garanties, souvent beaucoup moins cher. Changement possible à tout moment depuis la loi Lemoine.","assurance"),
]

NAV = [("index.html","Accueil"),("#exp","Expertises"),("simulateurs.html","Simulateurs"),("cabinet.html","Le cabinet"),("contact.html","Contact")]

def header(active):
    sub = "".join(f'<li><a href="{f}">{t}<small>{tag}</small></a></li>' for f,_,t,tag,_,_ in EXPERTISES)
    sub += '<li><a href="pret-hypothecaire.html#seniors">Viager hypothécaire et réméré<small>Solutions patrimoniales</small></a></li>'
    def a(href,label):
        cur = ' aria-current="page"' if href==active else ''
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f'''<header class="site-header"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="KAIRN, accueil">{LOGO}<span><span class="brand-name">KAIRN</span><span class="brand-tag">EXPERTS EN FINANCEMENTS</span></span></a>
<ul class="menu" id="menu">
<li class="has-sub"><button type="button" aria-expanded="false" aria-haspopup="true">Nos expertises ▾</button><ul class="sub">{sub}</ul></li>
{a("simulateurs.html","Simulateurs")}{a("cabinet.html","Le cabinet")}{a("cabinet.html#recrutement","Recrutement")}{a("contact.html","Contact")}
</ul>
<div class="nav-cta"><a class="nav-phone num" href="tel:{TEL}">{PHONE}</a><a class="btn btn-light btn-sm" href="contact.html">Étude gratuite</a>
<button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div>
</div></header>'''

def footer():
    exp = "".join(f'<li><a href="{f}">{t}</a></li>' for f,_,t,_,_,_ in EXPERTISES)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html" aria-label="KAIRN, accueil">{LOGO}<span><span class="brand-name">KAIRN</span><span class="brand-tag">EXPERTS EN FINANCEMENTS</span></span></a>
<p style="margin-top:18px;max-width:34ch">Courtier en financement à Lorient. Nous accompagnons particuliers et professionnels en Bretagne et partout en France.</p></div>
<div><h4>Expertises</h4><ul>{exp}<li><a href="pret-hypothecaire.html#seniors">Viager hypothécaire et réméré</a></li></ul></div>
<div><h4>Le cabinet</h4><ul><li><a href="cabinet.html">Qui sommes-nous</a></li><li><a href="cabinet.html#methode">Notre méthode</a></li><li><a href="simulateurs.html">Simulateurs</a></li><li><a href="cabinet.html#recrutement">Recrutement</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h4>Nous joindre</h4><ul><li><a class="num" href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>{ADDR}</li><li>Lun–ven 9h–12h / 13h30–18h<br>Samedi sur rendez-vous</li>
<li><a href="https://www.linkedin.com/" data-todo="lien LinkedIn KAIRN">LinkedIn</a> · <a href="https://www.facebook.com/" data-todo="lien Facebook KAIRN">Facebook</a> · <a href="https://www.instagram.com/" data-todo="lien Instagram KAIRN">Instagram</a></li></ul></div>
</div>
<div class="legal">
<p>KAIRN est le nom commercial de BMB Financement, RCS Lorient 800 090 607. Courtier en opérations de banque et en services de paiement (COBSP) immatriculé à l'ORIAS sous le n° 14003265, vérifiable sur <a href="https://www.orias.fr" rel="noopener">orias.fr</a>.</p>
<p><strong>Aucun versement, de quelque nature que ce soit, ne peut être exigé d'un particulier avant l'obtention d'un ou plusieurs prêts d'argent.</strong> Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager. L'emprunteur dispose d'un délai de réflexion de 10 jours pour un crédit immobilier ; la vente est subordonnée à l'obtention du prêt, et si celui-ci n'est pas obtenu, le vendeur doit rembourser les sommes versées.</p>
<p>© 2026 KAIRN — BMB Financement · <a href="mentions-legales.html">Mentions légales</a> · <a href="mentions-legales.html#confidentialite">Confidentialité</a></p>
</div></div></footer>
<div class="mobile-bar"><a class="btn btn-outline" href="tel:{TEL}">{I["phone"].replace('<svg','<svg width="18" height="18"')} Appeler</a><a class="btn btn-primary" href="contact.html">Étude gratuite</a></div>'''

def lead_wizard():
    projets = [("immo","home","Achat immobilier"),("rachat","merge","Regrouper mes crédits"),("pro","pro","Projet professionnel"),("hypo","key","Prêt hypothécaire"),("assurance","shield","Assurance de prêt"),("autre","plus","Autre projet")]
    ch = "".join(f'<button type="button" class="choice" data-value="{l}" aria-pressed="false">{I[i]}{l}</button>' for k,i,l in projets)
    montants = ["Moins de 50 000 €","50 000 à 150 000 €","150 000 à 300 000 €","Plus de 300 000 €"]
    mh = "".join(f'<button type="button" class="choice" data-value="{m}" aria-pressed="false">{I["euro"]}{m}</button>' for m in montants)
    return f'''<form class="lead-card" data-wizard novalidate aria-labelledby="lw-t">
<h2 id="lw-t">Étude de financement gratuite</h2>
<p class="sub-title">3 questions, 1 minute. Un expert vous rappelle sous 24 h.</p>
<div class="progress" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="steps-wrap">
<input type="hidden" name="projet"><input type="hidden" name="montant">
<div class="step" data-group="projet"><p class="step-q">Quel est votre projet ?</p><div class="choice-grid">{ch}</div></div>
<div class="step" data-group="montant" hidden><p class="step-q">Quel montant environ ?</p><div class="choice-grid">{mh}</div>
<div class="form-nav"><button type="button" class="linkbtn" data-back>← Retour</button></div></div>
<div class="step" hidden><p class="step-q">Où pouvons-nous vous rappeler ?</p>
<div class="row2"><div class="field"><label for="w-nom">Nom et prénom</label><input id="w-nom" name="nom" autocomplete="name" required></div>
<div class="field"><label for="w-tel">Téléphone</label><input id="w-tel" name="telephone" type="tel" autocomplete="tel" required></div></div>
<div class="field"><label for="w-mail">E-mail</label><input id="w-mail" name="email" type="email" autocomplete="email"></div>
<input class="hp" name="site_web" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="check"><input type="checkbox" id="w-rgpd" required> J'accepte d'être recontacté par KAIRN au sujet de mon projet. <a href="mentions-legales.html#confidentialite">Données personnelles</a></label>
<div class="form-nav"><button type="button" class="linkbtn" data-back>← Retour</button><button class="btn btn-primary" type="submit">Être rappelé {I["arrow"]}</button></div></div>
</div>
<div class="done" hidden>{I["done"]}<h3>Demande bien reçue</h3><p class="fine">Un expert KAIRN vous rappelle sous 24 h ouvrées.</p></div>
<div class="fail done" hidden><h3>L'envoi n'a pas abouti</h3><p class="fine">Appelez-nous au <span class="num">{PHONE}</span> ou écrivez à {MAIL}.</p></div>
<p class="fine">Gratuit et sans engagement. Aucun frais avant l'obtention de votre financement.</p>
</form>'''

def trust_row():
    return f'''<div class="trust"><span>{I["clock"]}Réponse sous 24 h</span><span>{I["gift"]}Étude gratuite</span><span>{I["pin"]}Lorient · Bretagne · France</span><span>{I["shield"]}ORIAS n° 14003265</span></div>'''

def rng(sim,name,label,mn,mx,step,val,fmt="eur"):
    i=f"{sim}-{name}"
    return f'<div class="range"><div class="range-top"><label for="{i}">{label}</label><output for="{i}"></output></div><input type="range" id="{i}" name="{name}" min="{mn}" max="{mx}" step="{step}" value="{val}" data-fmt="{fmt}"></div>'

def sim_capacite(p="cap"):
    return f'''<div class="sim" data-sim="capacite"><div class="sim-inputs">
{rng(p,"revenus","Revenus nets du foyer / mois",1500,15000,100,4500)}
{rng(p,"charges","Crédits en cours / mois",0,3000,50,300)}
{rng(p,"apport","Apport personnel",0,200000,1000,30000)}
{rng(p,"duree","Durée du prêt",10,25,1,25,"ans")}
{rng(p,"taux","Taux indicatif (hors assurance)",2,5,0.05,3.3,"pct2")}
</div><div class="sim-out"><span class="out-label">Budget total estimé</span><span class="big" data-out="projet">–</span>
<div class="out-lines"><div>Montant empruntable<b data-out="capital">–</b></div><div>Mensualité maximale<b data-out="mensualite" data-fmt="eurm">–</b></div><div>Taux d'endettement<b data-out="endettement" data-fmt="pct1">–</b></div></div>
<p class="fine">Calcul indicatif sur la règle des 35 % d'endettement, hors assurance et frais. Votre étude personnalisée tient compte du reste à vivre, de votre profil et des conditions de chaque banque.</p>
<a class="btn btn-light" href="contact.html#immo">Faire valider mon budget {I["arrow"]}</a></div></div>'''

def sim_rachat(p="rac"):
    return f'''<div class="sim" data-sim="rachat"><div class="sim-inputs">
{rng(p,"avant","Total de vos mensualités actuelles",200,5000,10,1480,"eurm")}
{rng(p,"crd","Capital restant dû, tous crédits",5000,300000,1000,62000)}
{rng(p,"treso","Trésorerie ou projet à ajouter",0,50000,1000,0)}
{rng(p,"duree","Nouvelle durée",3,25,1,10,"ans")}
{rng(p,"taux","Taux indicatif",3,9,0.1,5.5,"pct1")}
</div><div class="sim-out"><span class="out-label">Exemple de regroupement</span>
<div class="ba"><div class="ba-box"><small>Avant</small><b data-out="avant" data-fmt="eurm">–</b><span>plusieurs crédits</span></div><span class="ba-arrow" aria-hidden="true">→</span><div class="ba-box after"><small>Après</small><b data-out="apres" data-fmt="eurm">–</b><span>une seule mensualité</span></div></div>
<span class="delta">Budget libéré : <span data-out="gain" data-fmt="eurm">–</span></span>
<div class="out-lines"><div>Baisse de mensualité<b data-out="baisse" data-fmt="pct1">–</b></div><div>Montant regroupé<b data-out="total">–</b></div></div>
<p class="fine">Simulation indicative, hors assurance et frais. Allonger la durée réduit la mensualité mais peut augmenter le coût total du crédit. Un crédit vous engage et doit être remboursé.</p>
<a class="btn btn-light" href="contact.html#rachat">Étudier mon regroupement {I["arrow"]}</a></div></div>'''

def sim_assurance(p="ass"):
    return f'''<div class="sim" data-sim="assurance"><div class="sim-inputs">
{rng(p,"capital","Capital emprunté",50000,800000,5000,250000)}
{rng(p,"duree","Durée restante",5,25,1,20,"ans")}
{rng(p,"tauxActuel","Taux de votre assurance actuelle",0.1,0.6,0.01,0.34,"pct2")}
{rng(p,"tauxDelegation","Taux d'un contrat délégué",0.05,0.4,0.01,0.12,"pct2")}
</div><div class="sim-out"><span class="out-label">Économie estimée</span><span class="big" data-out="total">–</span>
<div class="out-lines"><div>Soit par mois<b data-out="mois" data-fmt="eurm">–</b></div><div>Coût avec le contrat actuel<b data-out="actuel">–</b></div><div>Coût avec délégation<b data-out="delegation">–</b></div></div>
<p class="fine">Estimation sur capital initial, indicative. Le taux d'un contrat délégué dépend de votre âge, de votre santé et des garanties exigées par votre banque, qui doivent rester équivalentes.</p>
<a class="btn btn-light" href="contact.html#assurance">Recevoir mon calcul gratuit {I["arrow"]}</a></div></div>'''

def sim_hypo(p="hyp"):
    return f'''<div class="sim" data-sim="hypothecaire"><div class="sim-inputs">
{rng(p,"valeur","Valeur de votre bien",80000,1500000,10000,320000)}
{rng(p,"crd","Crédit restant sur ce bien",0,500000,5000,40000)}
{rng(p,"duree","Durée souhaitée",5,25,1,15,"ans")}
{rng(p,"taux","Taux indicatif",3,8,0.1,4.8,"pct1")}
</div><div class="sim-out"><span class="out-label">Montant mobilisable estimé</span><span class="big" data-out="mobilisable">–</span>
<div class="out-lines"><div>Mensualité correspondante<b data-out="mensualite" data-fmt="eurm">–</b></div><div>Quotité retenue<b>70 % de la valeur</b></div></div>
<p class="fine">Estimation indicative : la valeur retenue par la banque, votre capacité de remboursement et la nature du bien déterminent le montant final.</p>
<a class="btn btn-light" href="contact.html#hypo">Étudier mon prêt hypothécaire {I["arrow"]}</a></div></div>'''

def sim_pro(p="pro"):
    return f'''<div class="sim" data-sim="pro"><div class="sim-inputs">
{rng(p,"montant","Montant à financer",10000,1500000,5000,150000)}
{rng(p,"duree","Durée",2,20,1,7,"ans")}
{rng(p,"taux","Taux indicatif",3,8,0.1,4.6,"pct1")}
</div><div class="sim-out"><span class="out-label">Mensualité estimée</span><span class="big" data-out="mensualite" data-fmt="eurm">–</span>
<div class="out-lines"><div>Coût des intérêts<b data-out="cout">–</b></div></div>
<p class="fine">Calcul indicatif hors assurance, garanties et frais de dossier. Le taux dépend du projet, de l'apport et des garanties proposées.</p>
<a class="btn btn-light" href="contact.html#pro">Présenter mon projet {I["arrow"]}</a></div></div>'''

def stats():
    return '''<div class="stats"><div class="stat"><b>2 200</b><span>dossiers financés</span></div><div class="stat"><b>94 %</b><span>de taux d'accord</span></div><div class="stat"><b>+30</b><span>partenaires bancaires</span></div><div class="stat"><b>15 ans</b><span>d'expertise du courtage</span></div></div>'''

def cta_band(title="Votre projet mérite une vraie étude", text="Un expert analyse votre situation et vous rappelle sous 24 h. C'est gratuit, et vous ne payez nos honoraires qu'une fois votre financement obtenu."):
    return f'''<section class="section"><div class="wrap"><div class="cta-band dark">{HEXWM}<div style="position:relative"><h2>{title}</h2><p class="lead" style="margin-top:12px">{text}</p></div>
<div class="actions" style="position:relative"><a class="btn btn-light" href="contact.html">Demander mon étude {I["arrow"]}</a><a class="btn btn-ghost num" href="tel:{TEL}">{PHONE}</a></div></div></div></section>'''

def faq(items):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items) + '</div>'

def ticks(items):
    return '<ul class="ticks">' + "".join(f'<li>{I["check"]}<div><b>{b}</b><span>{s}</span></div></li>' for b,s in items) + '</ul>'

def page_hero(crumb, eyebrow, title, lead, extra=""):
    return f'''<section class="dark page-hero">{HEXWM}<div class="wrap"><p class="crumbs"><a href="index.html">Accueil</a> / {crumb}</p>
<span class="eyebrow">{eyebrow}</span><h1 style="margin-top:14px;max-width:20ch">{title}</h1><p class="lead" style="margin-top:18px">{lead}</p>
<div class="hero-actions"><a class="btn btn-light" href="contact.html">Demander mon étude gratuite {I["arrow"]}</a><a class="btn btn-ghost num" href="tel:{TEL}">{PHONE}</a></div>{trust_row()}{extra}</div></section>'''

REVIEWS = '''<div class="reviews">
<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>J’ai fait appel à Kairn pour financer mon projet immobilier et je ne peux que saluer la qualité de leur travail. En plus d'un grand professionnalisme et d'une rigueur rassurante dans le montage du dossier, j'ai particulièrement apprécié la disponibilité et l'extrême réactivité dans les échanges. Un vrai suivi personnalisé qui fait toute la différence dans un projet de vie.</p><footer><b>Benjamin T.</b>Projet immobilier · septembre 2026 · Avis Google</footer></article>
<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>J'ai refait appel au cabinet 9 ans après pour un autre achat immobilier ! J'ai pu retrouver une seconde fois Valérie Le Barber, je lui suis très reconnaissante pour la qualité de l'accompagnement qu'elle a pu m'apporter tout au long du projet. L'équipe reste très disponible, je ne peux que recommander de passer par eux.</p><footer><b>Emmanuelle J.</b>Achat immobilier · avril 2026 · Avis Google</footer></article>
<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>Un immense merci à Solen pour son accompagnement tout au long de mon premier achat immobilier. Toujours disponible, réactive et à l'écoute, elle a su me guider et me conseiller à chaque étape avec professionnalisme et bienveillance. Je recommande les yeux fermés !</p><footer><b>Loann C.</b>Premier achat · juin 2026 · Avis Google</footer></article>
<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>Pour un premier achat immobilier, je suis vraiment contente d’avoir pu compter sur Maxime Hellec. Il a été présent du début à la fin, toujours joignable quand j’avais une question ou un doute, et surtout très investi dans mon dossier. Il a su rendre les choses beaucoup plus simples et moins stressantes.</p><footer><b>Chloé L.</b>Premier achat · avril 2026 · Avis Google</footer></article>
<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>Moi et mon mari nous sommes plus que satisfaits d'avoir mis notre projet immobilier entre les mains de Solen Rojouant de l'agence Kairn ! Elle est d'une efficacité inégalable avec une grande écoute et des conseils qui nous ont amené à concrétiser ce projet de famille sans complication.</p><footer><b>Delphine D.</b>Projet immobilier · juillet 2026 · Avis Google</footer></article>
<article class="review"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><p>Merci beaucoup à Maxime Hellec qui nous a accompagnés dans notre acquisition malgré un dossier difficile. Très professionnel et à l'écoute. Nous n'hésiterons pas à le rappeler pour un prochain projet immobilier et le recommandons !</p><footer><b>Charlotte G.</b>Acquisition · juillet 2026 · Avis Google</footer></article>
</div>'''

def schema():
    return '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"FinancialService","name":"KAIRN","legalName":"BMB Financement","url":"https://kairn-finance.com/","telephone":"+33 9 84 23 08 44","email":"contact@kairn-finance.fr","address":{"@type":"PostalAddress","streetAddress":"8 mail Jeanne Villepreux-Power","postalCode":"56100","addressLocality":"Lorient","addressCountry":"FR"},"areaServed":["Lorient","Morbihan","Bretagne","France"],"openingHours":["Mo-Fr 09:00-12:00","Mo-Fr 13:30-18:00"],"identifier":"ORIAS 14003265"}</script>'''

def page(fname, title, desc, body, active=None):
    head = f'''<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="canonical" href="https://kairn-finance.com/{'' if fname=='index.html' else fname}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:locale" content="fr_FR">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Montserrat:wght@600;700;800&display=swap">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">{schema() if fname=="index.html" else ""}'''
    content = f'{header(active or fname)}<main>{body}</main>{footer()}{'<script>window.KAIRN_FORM_ENDPOINT="envoi.php";</script>' if MODE=='site' else ''}<script src="main.js"></script>'
    if MODE=="artifact" and fname=="index.html":
        html = head + "\n" + content
    else:
        html = f'<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{head}\n</head>\n<body>\n{content}\n</body>\n</html>\n'
    import re
    html = re.sub(r' ([?!])(?=[\s<])', r'&nbsp;\1', html)
    open(os.path.join(OUT,fname),"w").write(html)

exec(open(os.path.join(os.path.dirname(__file__) or ".","pages.py")).read())
for f in ["style.css","main.js"] + (["envoi.php"] if MODE=="site" else []):
    shutil.copy(f, OUT)

if MODE=="site":
    import datetime
    today=datetime.date.today().isoformat()
    pages=["index.html","credit-immobilier.html","pret-professionnel.html","rachat-de-credits.html","pret-hypothecaire.html","assurance-emprunteur.html","simulateurs.html","cabinet.html","contact.html","mentions-legales.html"]
    urls="".join(f"  <url><loc>https://kairn-finance.com/{'' if p=='index.html' else p}</loc><lastmod>{today}</lastmod></url>\n" for p in pages)
    open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\nDisallow: /_sources/\nDisallow: /envoi.php\n\nSitemap: https://kairn-finance.com/sitemap.xml\n")
shutil.copy("favicon.svg", OUT)
