from urllib.request import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
COMMENT_CHARS = '#:'
drawing = Drawing(400,200)
data=[]
pre=[]
max=[]
min=[]
times=[]
for line in urlopen(URL).readlines():
    l=line.decode()
    if not l.isspace() and l[0] not in COMMENT_CHARS:
        #d=l.split()
        data.append([float(d) for d in l.split()])
times=[d[0] + d[1] / 12.0 for d in data]
pre=[d[2] for d in data]
max=[d[3] for d in data]
min=[d[4] for d in data]
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data=[list(zip(times,pre)),list(zip(times,max)),list(zip(times,min))]
lp.lines[0].strokeColor=colors.red
lp.lines[1].strokeColor=colors.blue
lp.lines[2].strokeColor=colors.yellow
drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots',
fontSize=14, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')
