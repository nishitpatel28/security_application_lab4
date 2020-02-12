import socket
import platform
import random

try:
    target_server = 'localhost'
    target_port = 80
    npsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Connecting to LocalHost.\nIP Address: "+target_server+" \nPort: 80")
    
    #initiate connection
    npsocket.connect((target_server,target_port))
    
    #message to send
    npmessage = "n_patel is using device " + socket.gethostname()+" " + platform.system()+" " + platform.release()+" version " + platform.version()+" "
    
    times = random.randint(3,5)
    print("Sending {0}: times {1}".format(npmessage,times))
    npmessage *= times
    npsocket.sendall(npmessage.encode('UTF-8'))
    
    amount_received = 0
    
    amount_expected = len(npmessage)
    
    while amount_received < amount_expected:
        data = npsocket.recv(16)
        amount_received += len(data)
        print("Amount of data received: {0}".format(amount_received))
        print("recived data: {0}".format(data))
except Exception as ex:
    pass
finally:
    input("Press enter to close connection")
    npsocket.close()
    
        
        