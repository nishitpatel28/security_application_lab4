#Nishit Patel
#0946768
#LAB04

import socket

local_address = '0.0.0.0'
local_port = 80

#TCP/IP socket
npsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind ip address
npsocket.bind((local_address,local_port))
#print("Server listening on IP Address : "+ local_address +"\nPort "+ "80")
print("Server starting up on Address: {0} \nPort: {1}".format(local_address,local_port))

#listen to clients
npsocket.listen(5)

while True:
    print("waiting for connection")
    connection,client_address = npsocket.accept()
    try:
        print("Connection from: " + client_address[0])
        while True:
            client_data = connection.recv(16)
            print("Data from client: "+ client_data.decode('UTF-8'))
            if client_data:
                print("Data is sent back to client.")
                connection.sendall(client_data)
            else:
                print("No data received from client: "+ client_address[0])            
    
    except Exception as ex:
        pass
    finally:
        connection.close()
    
    