import json
import urllib.request
'''data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

js = json.dumps(data,sort_keys=True,indent=4) data-->str,indent:缩进
print(js)
jsonData = '{"employees": [{ "firstName":"Bill" , "lastName":"Gates" },{ "firstName":"George" , "lastName":"Bush" },{ "firstName":"Thomas" , "lastName":"Carter" }]}'

text = json.loads(jsonData) str-->dict
print(text.get('employees')[0])
'''
url='https://api.douban.com/v2/book/1220562'
reponse=urllib.request.urlopen(url)
html=reponse.read()
jsondata=html.decode('utf-8')
text=json.loads(jsondata,encoding='utf-8')
print(text)
with open('test.json',mode='a') as f:
    json.dump(jsondata,f)#dump将转换的字符串写入文件
with open('test.json',mode='r') as f:
    print(json.load(f))
