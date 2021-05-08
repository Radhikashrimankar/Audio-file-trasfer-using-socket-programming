import socket
import logging

port = 
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('Server Listening.... ')

while True:
        conn, addr = s.accept()
        print('Got connection from ', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))

        filename = "a123.mp3"
        f = open(filename, 'rb')
        rec = f.read(1024)
        print("file open")
        while       (rec):
            conn.send(rec)
            print('Sent', repr(rec))
            rec = f.read(1024)
        f.close()

        
        print('Done sending ')    
        conn.send(b" Thank u for connecting ")
        conn.close()