from math import *
import matplotlib.pyplot as plt

p = []
center = [[0.0,0.0],[0.0,0.0]]
file = open("data/out1")
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

x1 = []
y1 = []
x2 = []
y2 = []

for i in p:
    if i[2] == 1:
        x1.append(i[0])
        y1.append(i[1])
    else:
        x2.append(i[0])
        y2.append(i[1])

fig=plt.figure()
subplot = fig.add_subplot(1,1,1)
subplot.scatter(x1,y1,marker='x',color="red")
subplot.scatter(x2,y2,marker='o',color="blue")
subplot.set_xlim(0,65535)
subplot.set_ylim(0,65535)
fig.show()
raw_input()


