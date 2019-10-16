<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contáctanos</title>
</head>
<body>

<h2>Formulario de contacto:</h2>

<form action="/contact.post" method="post">
    <textarea name="message"></textarea>
    <input type="submit" value="Enviar">
</form>

%if sent is True:
<div>Sent!</div>
%end

</body>
</html>