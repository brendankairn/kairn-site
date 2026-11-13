/* KAIRN — interactions du site */
(function(){
  "use strict";
  // Adresse du script d'envoi des formulaires sur l'hébergement (voir envoi.php).
  // Laisser vide dans l'aperçu : le formulaire affiche alors la confirmation sans rien envoyer.
  var FORM_ENDPOINT = window.KAIRN_FORM_ENDPOINT || "";

  var eur = new Intl.NumberFormat("fr-FR",{style:"currency",currency:"EUR",maximumFractionDigits:0});
  var pct = function(v,d){return v.toLocaleString("fr-FR",{minimumFractionDigits:d,maximumFractionDigits:d})+" %";};

  /* Menu mobile */
  var burger=document.querySelector(".burger"), menu=document.querySelector(".menu");
  if(burger&&menu){burger.addEventListener("click",function(){var o=menu.classList.toggle("open");burger.setAttribute("aria-expanded",o);});}
  document.querySelectorAll(".has-sub>button").forEach(function(b){b.addEventListener("click",function(){var li=b.parentElement;var o=li.classList.toggle("open");b.setAttribute("aria-expanded",o);});});

  /* Calculs de crédit */
  function mensualite(capital,tauxAnnuel,annees){var t=tauxAnnuel/100/12,n=annees*12;if(t===0)return capital/n;return capital*t/(1-Math.pow(1+t,-n));}
  function capitalPour(mens,tauxAnnuel,annees){var t=tauxAnnuel/100/12,n=annees*12;if(t===0)return mens*n;return mens*(1-Math.pow(1+t,-n))/t;}

  var FORMATS={
    eur:function(v){return eur.format(v);},
    eurm:function(v){return eur.format(v)+"/mois";},
    ans:function(v){return v+" ans";},
    pct1:function(v){return pct(v,1);},
    pct2:function(v){return pct(v,2);}
  };

  var SIMS={
    capacite:function(v){
      var mmax=Math.max(0,v.revenus*0.35-v.charges);
      var cap=capitalPour(mmax,v.taux,v.duree);
      return {capital:cap,projet:cap+v.apport,mensualite:mmax,endettement:v.revenus?((v.charges+mmax)/v.revenus*100):0};
    },
    rachat:function(v){
      var total=v.crd+v.treso;
      var apres=mensualite(total,v.taux,v.duree);
      var baisse=v.avant>0?Math.max(0,(v.avant-apres)/v.avant*100):0;
      return {apres:apres,avant:v.avant,gain:Math.max(0,v.avant-apres),baisse:baisse,total:total};
    },
    assurance:function(v){
      var an=v.capital*(v.tauxActuel-v.tauxDelegation)/100;
      var tot=Math.max(0,an*v.duree);
      return {total:tot,mois:Math.max(0,an/12),actuel:v.capital*v.tauxActuel/100*v.duree,delegation:v.capital*v.tauxDelegation/100*v.duree};
    },
    hypothecaire:function(v){
      var mob=Math.max(0,v.valeur*0.7-v.crd);
      return {mobilisable:mob,mensualite:mensualite(mob,v.taux,v.duree)};
    },
    pro:function(v){
      var m=mensualite(v.montant,v.taux,v.duree);
      return {mensualite:m,cout:m*v.duree*12-v.montant};
    }
  };

  function paintRange(r){var p=(r.value-r.min)/(r.max-r.min)*100;r.style.setProperty("--p",p+"%");}

  document.querySelectorAll("[data-sim]").forEach(function(box){
    var name=box.getAttribute("data-sim");
    var inputs=box.querySelectorAll("input[type=range]");
    function run(){
      var v={};
      inputs.forEach(function(r){v[r.name]=parseFloat(r.value);paintRange(r);
        var o=box.querySelector('output[for="'+r.id+'"]');if(o)o.textContent=FORMATS[r.dataset.fmt||"eur"](parseFloat(r.value));});
      var res=SIMS[name](v);
      box.querySelectorAll("[data-out]").forEach(function(el){var k=el.dataset.out;var f=el.dataset.fmt||"eur";if(res[k]!==undefined)el.textContent=FORMATS[f](res[k]);});
    }
    inputs.forEach(function(r){r.addEventListener("input",run);});
    run();
  });

  /* Onglets simulateurs */
  document.querySelectorAll("[data-tabs]").forEach(function(group){
    var tabs=group.querySelectorAll("[role=tab]");
    tabs.forEach(function(t){t.addEventListener("click",function(){
      tabs.forEach(function(x){x.setAttribute("aria-selected",x===t);var p=document.getElementById(x.getAttribute("aria-controls"));if(p)p.hidden=(x!==t);});
    });});
  });

  /* Envoi des formulaires */
  function send(form,extra){
    var data=new FormData(form);
    if(extra)Object.keys(extra).forEach(function(k){data.append(k,extra[k]);});
    if(data.get("site_web"))return Promise.resolve(true); // piège à robots
    if(!FORM_ENDPOINT)return Promise.resolve(true);
    return fetch(FORM_ENDPOINT,{method:"POST",body:data}).then(function(r){return r.ok;}).catch(function(){return false;});
  }
  function valid(form){
    var ok=true;form.querySelectorAll("[required]").forEach(function(el){
      var bad=el.type==="checkbox"?!el.checked:!el.value.trim();
      if(el.type==="email"&&el.value&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value))bad=true;
      if(el.type==="tel"&&el.value&&el.value.replace(/\D/g,"").length<9)bad=true;
      el.setAttribute("aria-invalid",bad);if(bad){ok=false;el.style.borderColor="#a23b3b";}else el.style.borderColor="";
    });return ok;
  }

  /* Étude express en 3 étapes */
  document.querySelectorAll("[data-wizard]").forEach(function(form){
    var steps=form.querySelectorAll(".step"),bars=form.querySelectorAll(".progress i"),i=0,choice={};
    function show(n){i=n;steps.forEach(function(s,k){s.hidden=k!==n;});bars.forEach(function(b,k){b.classList.toggle("on",k<=n);});}
    form.querySelectorAll(".choice").forEach(function(c){c.addEventListener("click",function(){
      var g=c.closest("[data-group]");g.querySelectorAll(".choice").forEach(function(x){x.setAttribute("aria-pressed",x===c);});
      choice[g.dataset.group]=c.dataset.value;var h=form.querySelector('input[name="'+g.dataset.group+'"]');if(h)h.value=c.dataset.value;
      setTimeout(function(){show(i+1);},180);
    });});
    form.querySelectorAll("[data-back]").forEach(function(b){b.addEventListener("click",function(){show(Math.max(0,i-1));});});
    form.addEventListener("submit",function(e){e.preventDefault();if(!valid(form))return;
      var btn=form.querySelector("[type=submit]");btn.disabled=true;
      send(form,{formulaire:"Étude express"}).then(function(ok){
        form.querySelector(".steps-wrap").hidden=true;var d=form.querySelector(ok?".done":".fail");if(d)d.hidden=false;});
    });
    show(0);
  });

  /* Formulaires simples */
  document.querySelectorAll("form[data-form]").forEach(function(form){
    form.addEventListener("submit",function(e){e.preventDefault();if(!valid(form))return;
      var btn=form.querySelector("[type=submit]");btn.disabled=true;
      send(form,{formulaire:form.dataset.form}).then(function(ok){
        form.querySelector(".form-body").hidden=true;var d=form.querySelector(ok?".done":".fail");if(d)d.hidden=false;});
    });
  });

  /* Pré-remplir le besoin depuis un lien (ex. contact.html#rachat) */
  var sel=document.getElementById("c-besoin");
  if(sel&&location.hash){var h=location.hash.slice(1);Array.prototype.forEach.call(sel.options,function(o){if(o.dataset.key===h)sel.value=o.value;});}
})();
