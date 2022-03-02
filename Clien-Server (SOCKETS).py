import socket
import threading
# for error98 change the port number
HEADER = 64 # every bit sent is of the size of header-64 needed for decoding
PORT = 5051 # checking the port of your router on what it's working on

SERVER = socket.gethostbyname(socket.gethostname()) # getting the IP address of using
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECTED_msg = "!Disconnect"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # creating a socket AF_Inet is the family stream is for streaming data
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr}connected.\t")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED_msg:
                connected = False
            print(f"{addr}->{msg}")
            if connected == False:
                print(f"{addr} is Disconnected")
            conn.send("RECEIVED".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args= (conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS--> [{threading.active_count()-1}]")
print("Server is Starting...")
start()

