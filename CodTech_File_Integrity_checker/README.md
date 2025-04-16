FILE INTEGRITY CHECKER

Step 1:-
    1.  First Install Python 3 on your System

    2.  Save the Script in a file
            eg... integrity_Checker.py

Step 2:-    RUN THE SCRIPT
    1.  Open the terminal or command prompt

    2.  Navigate to the folder where integrity_checker.py is saved using th cd command:
    >> cd path/to/your/script

    3.  Run the Script:
        >> python integrity_checker.py

Step 3:-    GENERATE BASELINE (OPTION 1)
    1.  When prompted:
        1. Generate baseline
        2. Check file integrity
        Select option (1/2):

        Type 1 and press Enter.

    2.  Enter the full path to the folder you want to monitor, for example:

        Enter full folder path to scan: "C:\Users\Rajeev\Documents\important"

    3.  The script will calculate the hash of each file and save them:
     >> baseline_hashes.txt

Step 4:-    CHECK FILE INTEGRITY (OPTION 2)
    1.  Run the script again:
        >> python integrity_checker.py

    2.  Select option 2:
        1. Generate baseline
        2. Check file integrity
        Select option (1/2): 2

    3.  Enter the path to the baseline file(created in Step 3):

        >> Enter path to baseline hash file: "baseline_hashes.txt"

    4. The script will now:
        > compare the current file hashes with the saved onces

        > Tell us which file are unchanged, changed, or missing

OUTPUT:-

![Image](https://github.com/user-attachments/assets/9ddbfe85-3423-4af9-90e9-3b33c429b733)