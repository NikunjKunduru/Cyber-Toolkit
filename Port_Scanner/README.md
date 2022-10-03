# Port Scanner for Windows, Linux and Mac OS
A port scanner is an application designed to probe a server or host for open ports. This application can be used by administrators to verify security policies of their networks and by attackers to identify network services running on a host and exploit vulnerabilities. 

&nbsp;
## What is this project about?
Implementing a port scanner in Python using sockets, a threaded version of a port scanner that is reliable for use.

&nbsp;
## How to run this project?
**Step 1:** 
This project requires Python3 to run. You can download it from [HERE](https://www.python.org/downloads/). Also make sure you have pip installed or run this command in your terminal to install pip:
    
    apt install python3-pip

**Step 2:**
Install the keyboard library using pip:
    
    pip install colorama

**Step 3:**
Clone this repository:
    
    git clone https://github.com/NikunjKunduru/Cyber-Toolkit.git

**Step 4:**
Go to the cloned directory and run the keylogger.py file:
    
    cd Cyber-Toolkit/Port_Scanner
    python3 portscanner.py <Host's IP address> --ports <Port range (inclusive of both ports)> 

&nbsp;
## Conclusion
If the scanner is freezing on a single port, that's a sign you need to decrease your number of threads. If the server you're probing has a high ping, you should reduce `N_THREADS` to 100, 50, or even lower, try to experiment with this parameter.

&nbsp;
## DISCLAIMER 
Note that use this code only on a computer you have permission to. Use it at your own risk!

<br />

🤖**References:** https://www.thepythoncode.com
