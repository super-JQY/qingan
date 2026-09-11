import requests,json,time,pathlib
p=pathlib.Path(__file__).parent
names=['西宁','黑马河乡','都兰县','察尔汗盐湖','大柴旦镇','大柴旦翡翠湖','冷湖镇','敦煌市','嘉峪关市','张掖七彩丹霞','肃南裕固族自治县','祁连县','峨堡镇']
out={}
for name in names:
 r=requests.get('https://nominatim.openstreetmap.org/search',params={'q':name,'format':'json','limit':1,'countrycodes':'cn'},headers={'User-Agent':'PersonalTravelMap/1.0'},timeout=25)
 data=r.json()
 if data: out[name]={'lat':float(data[0]['lat']),'lon':float(data[0]['lon']),'source':data[0]}
 print(name, json.dumps(out.get(name,{}),ensure_ascii=True)[:180],flush=True)
 time.sleep(1.1)
(p/'locations.json').write_text(json.dumps(out,ensure_ascii=False),encoding='utf-8')
