#!/usr/bin/python
import socket

HOST = '192.168.1.66'    # The remote host
PORT = 8082              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print 'Received', repr(data)

#1,2,3,4,5,6,7,8,9,0,av,enter,v+,p+,v-,p-,ok,menu,back,screen,guia,video,i,switchscreen,gravacao,stop,play,pause,up,down,left,right,prev,rev,forw,next    ,red,green,yellow,blue,mute,song,riscas,tv
meo_key = [
        49,50,51,52,53,54,55,56,57,48,#0
        0,0,
        233,#poweroff
        175,#v+
        33,#p+
        174,#v-
        34,#p-
        13,#ok
        36,#menu
        8,#back
        27,#screen
        112,#guia
        114,#video
        159,#gravacao
        156,115,123,119,225,38,40,37,39,117,118,121,122,140,141,142,143,173,0,111,0];
meo_1_x = [24,135,242,24,139,234,22,135,242,135,26,240,242,24,242,22,242,118,112,22,99,178,260,22,133,240,22,133,240,105,103,35,230,22,101,180,225,22,    99,180,257,24,99,176,257];
meo_1_y = [102,102,102,188,188,188,272,272,272,358,358,358,15,481,481,698,698,557,778,838,838,838,838,933,933,933,1016,1019,1019,491,686,561,560,1120,    1124,1121,1127,1207,1204,1204,1207,1283,1285,1285,1289];
meo_2_x = [88,201,308,88,201,308,90,201,308,197,88,307,309,90,309,90,309,212,217,73,151,228,307,86,197,304,90,198,317,227,230,106,305,71,148,225,305,7    1,148,227,302,69,146,227,300];
meo_2_y = [170,170,170,254,254,254,343,343,343,426,426,426,84,549,549,768,771,673,820,889,889,889,889,999,999,999,1083,1083,1085,567,764,686,688,1175,    1178,1179,1179,1256,1256,1258,1259,1340,1337,1337,1341];
#s.send("key=112\n")#guia
s.send("key=233\n")#power
#s.send("key=36\n")#menu
#s.send("key=8\n")#back
#s.send("key=114\n")#video
#s.send("key=159\n")#gravacao
#s.send("key=115\n")#play
#s.send("key=111\n")#wide-smart
#s.send("key=173\n")#mute
#s.send("key=143\n")#mute

s.close()