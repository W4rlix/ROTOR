import socket			

s = socket.socket()		
print ("Socket successfully created")

port = 12345			
s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")

while True:
    c, addr = s.accept()
    dataFromClient = c.recv(1024).decode()
    
    if(dataFromClient == "Lewo"):
        print (dataFromClient)
        c.send("Przyjeto komende Lewo".encode())
    else:
        print (dataFromClient)
        c.send("Przyjeto komende Prawo".encode())

c.close()
        

    
    

    

