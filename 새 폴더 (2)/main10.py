import json
li = [{'name': '홍길동', 'kor': 77, 'eng': 90, 'math': 80},
      {'name': '김철수', 'kor': 57, 'eng': 60, 'math': 30},
      {'name': '조성무', 'kor': 87, 'eng': 80, 'math': 40}]

with open('c:/Users/gotsl/Desktop/새 폴더 (2)/avc.json','w') as f:
    json.dump(li,f,ensure_ascii=False)