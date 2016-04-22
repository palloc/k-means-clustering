from math import *
import matplotlib.pyplot as plt
from scapy.all import *

#show all packets
def show_all(packet):
    for i in packet:
        print packet.show()

#export arrived time    
def export_time(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            s += str(i.time) + '\n'
        except AttributeError:
            s += "No time" + '\n'
    file.write(s)
    file.close()

#export source mac address
def export_mac_src(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        s += i.src + '\n'
    file.write(s)
    file.close()

#export destination mac address
def export_mac_dst(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        s += i.dst + '\n'
    file.write(s)
    file.close()

#export source ip address
def export_ip_src(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            s += i[IP].src + '\n'
        except IndexError:
            s += "No IPLayer\n"
    file.write(s)
    file.close()

#export destination ip address
def export_ip_dst(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            s += i[IP].dst + '\n'
        except IndexError:
            s += "No IPLayer\n"
    file.write(s)
    file.close()

#export ttl
def export_ttl(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            s += str(i[IP].ttl) + '\n'
        except IndexError:
            s += "No IPLayer\n"
    file.write(s)
    file.close()
    
#export protocol number
def export_protocol(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            s += str(i.proto) + '\n'
        except AttributeError:
            s += "No IPLayer\n"
    file.write(s)
    file.close()

#export destination port
def export_dport(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            #UDP
            if i[IP].proto == 17:
                s += str(i[UDP].dport) + ','
                s += str(i[UDP].sport) + '\n'
            else:
                s += str(i[TCP].dport) + ','
                s += str(i[TCP].sport) + '\n'
        except IndexError:
            s += "No IPLayer\n"
    file.write(s)
    file.close()

#export source port
def export_sport(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            #UDP
            if i[IP].proto == 17:
                s += str(i[UDP].sport) + '\n'
            else:
                s += str(i[TCP].sport) + '\n'
        except IndexError:
            s += "No IPLayer\n"
    file.write(s)
    file.close()
    
#export packet's data    
def export_data(packet,output):
    file = open(output,'w')
    s = ""
    for i in packet:
        try:
            s += i.load + '\n'
        except AttributeError:
            s += "NoData" + '\n'
    file.write(s)

    file.close()

f_name = "data/" + raw_input("enter pcap file name:")
output_name = "data/" + raw_input("enter output file name:")
pcap = rdpcap(f_name)
export_dport(pcap,output_name)
print "export complete!"
    





p = []
center = [[0.0,0.0],[0.0,0.0]]
file = open(output_name)
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


