import re
import numpy as np
from pylab import *
import pdb
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'

lines = open("g1.txt").readlines()
result = np.empty((0,4), float)
cx = 0.0
cy = 0.0
cz = 0.0
ce = 0.0
maxX=0
minX=0
maxY=0
minY=0
for line in lines:
    if(re.search(r"X[-\d\.]+",line)):
        cx = float(re.search(r"X[-\d\.]+",line).group(0).split('X')[1])
        maxX=max(maxX,cx)
        minX=min(minX,cx)
    if(re.search(r"Y[-\d\.]+",line)):
        cy = float(re.search(r"Y[-\d\.]+",line).group(0).split('Y')[1])
        maxY=max(maxY,cy)
        minY=min(minY,cy)
    if(re.search(r"Z[-\d\.]+",line)):
        cz = float(re.search(r"Z[-\d\.]+",line).group(0).split('Z')[1])
    if(re.search(r"E[-\d\.]+",line)):
        ce = float(re.search(r"E[-\d\.]+",line).group(0).split('E')[1])
    result = np.append(result, np.array([[cx,cy,cz,ce]]), axis=0)

#print(result)

print("hey")
figure(figsize=(12,10))
gcf().patch.set_facecolor('white')
gcf().canvas.set_window_title('result')
print("wey")
hold(True)
data = result.tolist()
#print(data)
#col_width = max(len(word) for row in data for word in row) + 2  # padding
cx = 0
cy = 0
cz = 0
ce = 0
counter = 0
t = []
ds = []
deltaEs = []
divided = []
T = []
X = []
Y = []
E = []
D = []
R = []
for row in data:
    if(counter==50 or counter==100 or counter==120):
        T.append(counter)
    t.append(counter)
    subplot(2,2,1)
    nx = row[0]
    ny = row[1]
    nz = row[2]
    if(cz!=nz):
        print("")
        print("")
        print("")
        print("Z shift: ",row[2])
        print("")
        print("")
        print("")
        cla()
    ne = row[3]
    deltaE = ne - ce
    plot(nx,ny,'ro')
    print("delta E:",deltaE)
    if(counter==50 or counter==100 or counter==120):
        X.append(nx)
        Y.append(ny)
        plot(X,Y,'ro',markersize=15)
    else:
        if(deltaE>0):
            plot([cx,nx],[cy,ny],'b-')
        
    axis('equal')
    xlim([minX,maxX])
    ylim([minY,maxY])
    title("Runnning Z "+str(cz))
    pause(0.01)
    print(nx,ny,nz,e)

    subplot(2,2,2)
    title("distance |x|")
    d = sqrt((cx-nx)**2-(cy-ny)**2)
    ds.append(d)
    if(counter==50 or counter==100 or counter==120):
        D.append(d)
        plot(T,D,'ro')
    else:
        plot(t,ds,'b-')

    subplot(2,2,3)
    title("delta E")
    deltaEs.append(deltaE)
    if(counter==50 or counter==100 or counter==120):
        E.append(deltaE)
        plot(T,E,'ro')
    else:
        plot(t,deltaEs,'b-')

    subplot(2,2,4)
    title("delta E / distance")
    divided.append(deltaE/d)
    if(counter==50 or counter==100 or counter==120):
        R.append(deltaE/d) 
        plot(T,R,'ro')
    else:
        plot(t,divided,'b-')

    cx = nx
    cy = ny
    cz = nz
    ce = ne
    counter = counter + 1
    #print("".join(word.ljust(col_width) for word in row))

