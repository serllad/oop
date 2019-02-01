from urllib.request import urlopen
from html.parser import  HTMLParser
def isjob(url):
    try:
        a,b,c,d=url.split('/')
    except ValueError:
        return False
    return a==d=='' and b=='jobs' and c.isdigit()
class scraper(HTMLParser):
    in_link=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        url=attrs.get('href','')
        if tag=='a' and isjob(url):
            self.in_link=True
            self.chunk=[]
            self.url=url
    def handle_data(self, data):
        if self.in_link==True:
            self.chunk.append(data)
            #print(data)
    def handle_endtag(self, tag):
        if self.in_link==True:
            for i in self.chunk:
                print('{0} ({1})'.format(i,self.url))
        self.in_link=False

text=urlopen('http://python.org/jobs').read().decode()

parser=scraper()
parser.feed(text)
parser.close()