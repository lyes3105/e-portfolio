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
    
    // IMPORTANT : Le "From" doit être ton adresse @e-portfolyes.fr
    $headers = "From: contact@e-portfolyes.fr\r\n"; 
    $headers .= "Reply-To: " . $email . "\r\n"; // C'est ici qu'on met le mail du client pour lui répondre
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    if (mail($to, $subject, $body, $headers)) {
        // Si ça marche, on retourne à l'index
        header('Location: index.html?success=1#contact');
        exit;
    } else {
        echo "Erreur lors de l'envoi du message.";
    }
}
?>