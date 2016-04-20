import numpy

p = [5,8,1,21,30,14,7,40]

center = [0.0,0.0]

#1-4=1  5-8=2

for i in range(len(p)/2):
    p[i].append(1)
    p[i+len(p)/2].append(2)

    
for i in p:
    if i[1] == 1:
        center[0] += double(i[0]) / double(len(p)/len(center))
    else i[1] == 2:
        center[1] += double(i[0]) / double(len(p)/len(center))



