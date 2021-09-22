import  socket
import sys

def Send_Commands(s,conn):
    print("Ctrl + C to Kill the Connection")
    print("Browse the System as usual")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(1024)
                print(data.decode("UTF - 8"))
        except KeyboardInterrupt:
             print("\n Goodbye")
             conn.close()
             s.close()
             sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            sys.exit()






def  server (address):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Initilazed , I m listening  ")
    except Exception as e :
        print("\n It seems like somethings went wrong. ")
        print(e)
        restart = input("\n Do you Want  me to re-initialize the server? y / n")
        if restart.lower() == "y" or restart.lower() == "yes":
            print("\n Roger That  Re Initializing the  server ... \n" )
            server(address)
        else:
            print("\n So Long .and Thanks for all the fish \n")
            sys.exit()
    conn,client_addr = s.accept()
    print(f"Connection Extablished :{client_addr}")
    Send_Commands(s, conn)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 52547
    server((host,port))



