"""Landing de servicios de IA de Samsa.
_base.css (línea de landings Samsa) + _ia.css (componentes de ionava + propios) + _body.html
-> artifact.html (para revisar en Claude) e index.html (para GitHub Pages)."""
from pathlib import Path
H = Path(__file__).parent
css = (H/"_base.css").read_text() + "\n" + (H/"_ia.css").read_text() + "\n" + (H/"_show.css").read_text()
body = (H/"_body.html").read_text()
title = "Samsa · IA generativa"
desc = "Servicios de inteligencia artificial de Samsa Creative: video, imagen, personajes, jingles, sistemas de contenido y capacitación para empresas."
head = (f'<title>{title}</title>\n<meta name="robots" content="noindex">\n<meta name="description" content="{desc}">\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap">\n'
        f'<style>\n{css}\n</style>\n')
(H/"artifact.html").write_text('<meta name="claude:viewport-fit-sides" content="cover">' + head + body)
(H/"index.html").write_text('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
print("ok")
