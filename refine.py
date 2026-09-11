import requests,json,time,pathlib
p=pathlib.Path(__file__).parent
out=json.loads((p/'locations.json').read_text(encoding='utf-8'))
for name,q in [('都兰县','察汗乌苏镇'),('祁连县','八宝镇 祁连'),('肃南裕固族自治县','红湾寺镇'),('青海湖南岸','江西沟乡'),('莫高窟','莫高窟数字展示中心')]:
 r=requests.get('https://nominatim.openstreetmap.org/search',params={'q':q,'format':'json','limit':1,'countrycodes':'cn'},headers={'User-Agent':'PersonalTravelMap/1.0'},timeout=25)
 data=r.json()
 if data: out[name]={'lat':float(data[0]['lat']),'lon':float(data[0]['lon']),'source':data[0]}
 print(name,json.dumps(out.get(name,{}),ensure_ascii=True)[:150],flush=True)
 time.sleep(1.1)
out['察尔汗盐湖']={'lat':36.8268,'lon':95.21567,'source':'https://mapcarta.com/N8899901117 — 游览区域代表点，不是驾车入口'}
out['黑独山']={'lat':38.867451,'lon':93.449686,'source':'https://nightchina.net/wp-content/plugins/leaflet-maps-marker/leaflet-fullscreen.php?marker=1178 — 景观区域代表点'}
(p/'locations.json').write_text(json.dumps(out,ensure_ascii=False),encoding='utf-8')
for name,url in [('leaflet.js','https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'),('leaflet.css','https://unpkg.com/leaflet@1.9.4/dist/leaflet.css')]:
 r=requests.get(url,timeout=25);r.raise_for_status();(p/name).write_text(r.text,encoding='utf-8')
