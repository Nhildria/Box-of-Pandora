import pyfiglet 
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.pyfiglet_format("Dark  Dante ' s Cave")
print(ascii_banner)

# Defining a Target

if len(sys.args) == 2:

    #Host name  to a IPv4
    target = socket.gethostname(sys.argv[1])

else :
    print("Invalid Amount of Argument ") 


print(" - " * 50)
print(" Scanning Target "  +target)
print(" Scanning Started at: "  +str(datetime.now()))
print(" - " * 50)

#Scan ports between 1 to 65,535

try :
    for port in range(1,100):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)


        #returns an error indicator 

        result = s.connect_ex((target,port))
        if  result == 0:
            print("Port {} is open ".format(port))
        s.close()

except KeyboardInterrupt:
    
    print(" \n Exitting Program ! ! ! ")
    sys.exit()

except socket.gaierror:

    print(" \n Hostname Could Not Be Resolved ! ! ! ")
    sys.exit()

except socket.error:

    print(" \n Server not Responding ! ! ! ")
    sys.exit()






