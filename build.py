from pathlib import Path
p=Path(__file__).parent
s=(p/'map-template.html').read_text(encoding='utf-8')
for token,name in [('LEAFLET_CSS','leaflet.css'),('LEAFLET_JS','leaflet.js'),('LOCATION_DATA','locations.json')]:s=s.replace(token,(p/name).read_text(encoding='utf-8'))
(p/'qinggan-map.html').write_text(s,encoding='utf-8')
(p/'index.html').write_text(s,encoding='utf-8')
