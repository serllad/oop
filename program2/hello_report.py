from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors
data = [
    #year mon pre    max     low
    (2018,7,  4.5,   5.5,    3.5),
    (2018,8,  4.7,   6.7,    2.7),
    (2018,9,  5.1,   8.1,    2.1),
    (2018,10,  5.4,   10.4,   0.4),
    (2018,11,  5.5,   10.5,   0.5),
    (2018,12,  5.3,   11.3,   0.0),
    (2019,1,  5.4,   12.4,   0.0),
    (2019,2,  5.6,   12.6,   0.0),
    (2019,3,  5.7,   13.7,   0.0)]

drawing = Drawing(200, 200)
pred = [row[2]*3 for row in data]
high = [row[3]*3 for row in data]
low = [row[4]*3 for row in data]
times = [200*((row[0] + row[1]/12.0) - 2018)-110 for row in data]
drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')