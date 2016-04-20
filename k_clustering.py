from math import *

p = [[5],[8],[1],[21],[30],[14],[7],[40]]

center = [0.0,0.0]

#1-4=1  5-8=2

for i in range(len(p)/2):
    p[i].append(1)
    p[i+len(p)/2].append(2)
print p

for j in range(0,100):
    for i in p:
        if i[1] == 1:
            center[0] += float(i[0]) / float(len(p)/len(center))
        elif i[1] == 2:
            center[1] += float(i[0]) / float(len(p)/len(center))
        i.pop()
    print "center1=%f center2=%f" % (center[0],center[1])
    for i in p:
        if abs(center[0] - i[0]) <= abs(center[1] - i[0]):
            i.append(1)
        else:
            i.append(2)
    print p
    center = [0.0,0.0]




