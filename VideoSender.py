import cv2
import numpy as np
import socket
import gzip
import sys
import pickle
import struct ### new code
IP = "localhost"
PORT = 8080

# Not sure why video isn't showing up
print "Starting capture"
cap=cv2.VideoCapture(0)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 4)
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 4)
#print cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#print cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#clientsocket.connect(('localhost',8080))
while True:
##    ret,frame=cap.read()
##    data = pickle.dumps(frame) ### new code
##    clientsocket.send(struct.pack("L", len(data))+data)
##    #clientsocket.sendall(struct.pack("L", len(data))+data) ### new code
    
    # UDP:
    ret,frame=cap.read()
    d = frame.flatten()
    s = d.tostring()
    for i in xrange(20):
        clientsocket.sendto(s[i*46080:(i+1)*46080],(IP, PORT))
    #data = pickle.dumps(frame) ### new code
    #dataSize = sys.getsizeof(data)
    #print dataSize
    #a = clientsocket.sendto(struct.pack("L", len(data))+data, (IP, PORT))
    #clientsocket.sendall(struct.pack("L", len(data))+data) ### new code
    
