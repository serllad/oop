import urllib.request
import urllib.parse
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

data={'i':'hi','from':'AUTO','to':'AUTO','client':'fanyideskweb',
'salt':'15475595191400',
'sign':'580feaea70c5f56c9ea38d44fcad0c5f',
'ts':'1547559519140',
'bv':'1de9313c44872e4c200c577f99d4c09e',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTIME',
'typoResult':'false'}
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)
html = response.read()
print(html.decode('utf-8'))