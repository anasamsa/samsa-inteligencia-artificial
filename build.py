"""Landing de servicios de IA de Samsa, en español e inglés.
_base.css + _ia.css + _show.css + _body.html  -> artifact.html (para revisar en Claude) e index.html (GitHub Pages)
_body_en.html                                  -> en/index.html (versión en inglés, usa las mismas imágenes de img/)."""
from pathlib import Path
H = Path(__file__).parent
css = (H/"_base.css").read_text() + "\n" + (H/"_ia.css").read_text() + "\n" + (H/"_show.css").read_text()
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap">\n'

def head(title, desc):
    return (f'<title>{title}</title>\n<meta name="robots" content="noindex">\n<meta name="description" content="{desc}">\n'
            + FONT + f'<style>\n{css}\n</style>\n')

def page(lang, h, body):
    return ('<!DOCTYPE html>\n' f'<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + h + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')

es_body = (H/"_body.html").read_text()
es_head = head("Samsa · IA generativa", "Servicios de inteligencia artificial de Samsa Creative: video, imagen, personajes, avatares, sistemas de contenido y capacitación para empresas.")
(H/"artifact.html").write_text('<meta name="claude:viewport-fit-sides" content="cover">' + es_head + es_body)
(H/"index.html").write_text(page("es", es_head, es_body))

en_body = (H/"_body_en.html").read_text().replace('"img/', '"../img/')
en_head = head("Samsa · Generative AI", "Samsa Creative AI services: video, images, characters, avatars, content systems and training for companies.")
(H/"en").mkdir(exist_ok=True)
(H/"en"/"index.html").write_text(page("en", en_head, en_body))
print("ok")
