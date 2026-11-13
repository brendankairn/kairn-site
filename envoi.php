<?php
// KAIRN — réception des formulaires du site (hébergement mutualisé OVH ou équivalent).
// Envoie chaque demande par e-mail à l'adresse ci-dessous.
$destinataire = 'contact@kairn-finance.fr';
$expediteur   = 'site@kairn-finance.com'; // adresse du domaine, pour éviter le classement en spam

header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
if (!empty($_POST['site_web'])) { echo '{"ok":true}'; exit; } // robot

$champs = ['formulaire','projet','montant','nom','prenom','telephone','email','ville','besoin','message','profil','creneau'];
$lignes = [];
foreach ($champs as $c) {
  if (isset($_POST[$c]) && trim($_POST[$c]) !== '') {
    $v = trim(strip_tags($_POST[$c]));
    $v = str_replace(["\r","\n"], ' ', mb_substr($v, 0, 2000));
    $lignes[] = ucfirst($c) . ' : ' . $v;
  }
}
if (empty($_POST['telephone']) && empty($_POST['email'])) { http_response_code(400); echo '{"ok":false}'; exit; }

$sujet = 'Nouvelle demande site — ' . (isset($_POST['formulaire']) ? strip_tags($_POST['formulaire']) : 'Contact');
$corps = implode("\n", $lignes) . "\n\nEnvoyé le " . date('d/m/Y H:i') . " depuis le site.";
$entetes = "From: KAIRN site <{$expediteur}>\r\nContent-Type: text/plain; charset=utf-8\r\n";
if (!empty($_POST['email']) && filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) $entetes .= "Reply-To: {$_POST['email']}\r\n";

$ok = mail($destinataire, '=?UTF-8?B?' . base64_encode($sujet) . '?=', $corps, $entetes);
echo json_encode(['ok' => $ok]);
