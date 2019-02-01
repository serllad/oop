from urllib.request import urlopen
import re
p = re.compile(r'<a href="(/jobs/\d+)/">(.*?)</a>')#.*是贪婪的，如果不匹配再回溯?
text = urlopen('http://python.org/jobs').read().decode()

for url, name in p.findall(text):
    print('{} ({})'.format(name, url))
