import json


with open('c:/Users/gotsl/Desktop/새 폴더 (2)/avc.json','r') as f:
    info=json.load(f)
for i in info:
    for k, v in i.items():
        print(k,v)
    print('-'*30)