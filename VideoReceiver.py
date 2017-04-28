import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new

HOST='localhost'
PORT=8080

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

sock.bind((HOST,PORT))
print 'Socket bind complete'
##s.listen(10)
##print 'Socket now listening'
##
##conn,addr=s.accept()
##
##### new
##data = ""
##payload_size = struct.calcsize("L")
##data = conn.recv(4096)
##count = 0
##while True:
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        cap.release()
##        cv2.destroyAllWindows()
##        sys.exit(0)
##    while len(data) < payload_size:
##        data += conn.recv(4096)
##    #count += 1
##    #print "Recieved packet "+str(count)
##    packed_msg_size = data[:payload_size]
##    data = data[payload_size:]
##    msg_size = struct.unpack("L", packed_msg_size)[0]
##    while len(data) < msg_size:
##        data += conn.recv(4096)
##    frame_data = data[:msg_size]
##    data = data[msg_size:]
##    ###
##
##    frame=pickle.loads(frame_data)
##
##    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##
##    # Display the resulting frame
##    #cv2.imshow('frame',gray)
##    #print frame
##    cv2.imshow('frame',frame)
##
##
##



# UDP:
print 'Socket bind complete'
### new
data = ""

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)
    s = ""

##    while len(data) < payload_size:
##        data += conn.recv(4096)
##    #count += 1
##    #print "Recieved packet "+str(count)
##    packed_msg_size = data[:payload_size]
##    data = data[payload_size:]
    data, addr = sock.recvfrom(48000)
    s += data
    if len(s) == (48000*20):
        frame = np.fromstring(s, dtype=np.uint8)
        print frame
       # frame = frame.reshape(480,640,3)
        s = ""
        cv2.imshow('frame',frame)

   # msg_size = struct.unpack("L", packed_msg_size)[0]
    


