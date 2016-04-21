from math import *

p = []
center = [0.0,0.0]

file = open("data/tmp")
line = file.readlines()

#read data
for i in line:
    try:
        p.append([int(i)])
    except ValueError:
        pass
#random clustering
for i in range(0,len(p)/2):
    p[i].append(1)
    p[i+len(p)/2].append(2)
for i in p:
    try:
        i[1]
    except IndexError:
        i.append(2)
    
#k-means
for j in range(0,100):
    for i in p:
        if i[1] == 1:
            center[0] += float(i[0]) / float(len(p)/len(center))
        elif i[1] == 2:
            center[1] += float(i[0]) / float(len(p)/len(center))
        i.pop()
    for i in p:
        if abs(center[0] - i[0]) <= abs(center[1] - i[0]):
            i.append(1)
        else:
            i.append(2)
    center = [0.0,0.0]

print p


