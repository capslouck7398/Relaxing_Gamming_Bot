import json

with open('123.json', 'r', encoding='utf8') as j:
    jdata = json.load(j)
print(jdata['qqq'])
jdata['qqq'] = input('www:')
with open('123.json', 'w+') as f:
    json.dump(jdata, f, indent=5)
