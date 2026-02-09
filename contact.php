<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    
    $to = 'contact@e-portfolyes.fr';
    $subject = 'Nouveau message portfolio - ' . $name;
    
    $body = "Nom : " . $name . "\n";
    $body .= "Email : " . $email . "\n\n";
    $body .= "Message :\n" . $message;
    
    $headers = "From: contact@e-portfolyes.fr\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    if (mail($to, $subject, $body, $headers)) {
        header('Location: index.html?success=1#contact');
        exit;
    } else {
        echo "Erreur lors de l'envoi du message.";
    }
}
?>
