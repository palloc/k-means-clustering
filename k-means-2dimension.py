from math import *

p = []
center = [[0.0,0.0],[0.0,0.0]]
file = open("data/tmp")
line = file.readlines()

#read data
for i in line:
    try:
        p.append(map(int,i.split(",")))
    except ValueError:
        pass

#random clustering
for i in range(len(p)/2):
    p[i].append(1)
    p[i+len(p)/2].append(2)
for i in p:
    try:
        i[2]
    except IndexError:
        i.append(2)

#k-means
print p
for j in range(0,100):

    count1 = 0
    count2 = 0
    for i in p:
        if i[2] == 1:
            center[0][0] += float(i[0])
            center[0][1] += float(i[1])
            count1 += 1
        else:
            center[1][0] += float(i[0])
            center[1][1] += float(i[1])
            count2 += 1
        i.pop()
    center[0][0] /= float(count1)
    center[0][1] /= float(count1)
    center[1][0] /= float(count2)
    center[1][1] /= float(count2)

    for i in p:
        if abs(sqrt((center[0][0]-i[0])**2 + (center[0][1]-i[1])**2)) <= abs(sqrt((center[1][0]-i[0])**2 + (center[1][1]-i[1])**2)):
            i.append(1)
        else:
            i.append(2)
    center = [[0.0,0.0],[0.0,0.0]]

