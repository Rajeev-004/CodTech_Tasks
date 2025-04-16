PENETRATION TESTING TOOLKIT IN LINUX

Step 1:-
        Create a Project Directory
            mkdir PenTestToolkit
            cd PenTestToolkit

Step 2:-
        start with 2-3 essential modules:
        1. Port Scanner
        2. Brute Force Login
        3. HTTP Directory Brute Forcer

Step 3:-
        Module 1 - Port Scanner
        Create a port_scanner.py file using command 
            nano port_scanner.py
Step 4:-
        Module 2 - Brute Forcer(SSH)
            First install Required Librarys
                pip install paramiko
            Create a file ssh_brute using command
                nano ssh_brute.py
            we need to create a password file which will store some password
                nano password.txt

Step 5:-
        Module 3 - HTTP directory Brute Forcer
            Check for the server file using command
                python3 -m http.server PORTNUMBER(80,8000,22, etc)
            Create a file http_brute using command
                nano http_brute.py
            Also create a common text file which contain some test paths
                nano common.txt

Step 6:-
        Create a main file using command
            nano main.py 

Step 7:- 
        Now we need to Zip our project folder using the command
            zip -r PenTestToolkit.zip PenTestToolkit/
Step 8:-
        Run the main.py file
            python3 main.py

Step 9:-
        For Module 1 output 
        Enter 1
        we need to enter the target IP address and the ports we need to scan like 80,22,433,8000 etc

Step 10:-
        For Module 2 output 
        Enter 2
        we need to enter the target IP address and username and the path to password list is password.txt

Step 11:-
        For Module 3 output
        Enter 3
        we need to enter the target URL like http://IP ADDRESS: PORT NUMBER
        and path to worldlist file is common.txt

Step 12:-
        Enter 4 to exit this process


