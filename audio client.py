import socket
s = socket.socket()
host = socket.gethostname()
port = 

s.connect((host,port))
s.send(b" Hello Server !!")

with open('rec.mp3','wb') as f:
    print('file opened ')
    while True:
        print('receiving data. ... ')
        data = s.recv(1024)
        print('data=%s',(data))
        if not data:
            break
        # write data to a filename
        f.write(data)

f.close()
print(' Succesfully get the file ')
s.close()
print(' Connection closed ')