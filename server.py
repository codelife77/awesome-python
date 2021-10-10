import socket
 
# bind socket 
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

# wait client
s.listen(5)

while True:
    # accept client
    c,addr = s.accept()
    c.send('hello world')
    c.close()
    
