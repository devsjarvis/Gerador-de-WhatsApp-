html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Botão WhatsApp</title>
</head>
<body>
    <a href="https://wa.me/595973624338" target="_blank">
        <button>Enviar WhatsApp</button>
    </a>
</body>
</html>
"""

# Salvar o código HTML em um arquivo
with open("pagina.html", "w") as file:
    file.write(html_code)
