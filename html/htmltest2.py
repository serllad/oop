from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story joy">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,'html.parser')
with open('html_doc.txt',mode='w') as f:
    f.write(repr(soup))
print(soup.prettify())
tags=soup.currentTag()#返回所有的tag

p_title=soup.p
print(p_title)
print(p_title.string)#p_title.string为NavigableString实例
print('-----------------------------------------------------------')
p_story=soup.find('p',{'class':'story'})
print('p_story=',p_story)
print('-------------------------------------------------------')
print(soup.a.attrs)
print('---------------------------------------')
for i in soup.find_all('a'):
    print(i['href'])
last_a_tag=soup.find('a',{'id':'link3'})
for i in last_a_tag.next_elements:
    print(i)
print('--------------------------------------------------')
html=last_a_tag.find_parent('html')
print(html)
print('------------------------------------------------------')

print(soup.select('a[href^=http://example.com/elsie]'))
