<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

if($_SERVER['REQUEST_METHOD'] == 'POST'){
    $mail = new PHPMailer(true);

    try {
        // Paramètres serveur
        $mail->isSMTP();
        $mail->Host       = 'ssl0.ovh.net';
        $mail->SMTPAuth   = true;
        $mail->Username   = 'contact@e-portfolyes.fr'; // ton email OVH
        $mail->Password   = 'Thecontact3105.';       // mot de passe OVH
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; 
        $mail->Port       = 587; // ou 465 si SSL

        // Destinataire
        $mail->setFrom($_POST['email'], $_POST['name']);
        $mail->addAddress('contact@e-portfolyes.fr'); // où tu reçois les mails

        $mail->Body = "Nom : " . $_POST['name'] . "\n";
$mail->Body .= "Email : " . $_POST['email'] . "\n";
$mail->Body .= "Message : " . $_POST['message'];

$mail->send();
echo "<p style='color:green;'>Merci, votre message a été envoyé avec succès ! Je prends bien note et vous répondrai dès que possible.</p>";

} catch (Exception $e) {
    echo "<p style='color:red;'>Erreur lors de l'envoi : {$mail->ErrorInfo}</p>";
}
}
