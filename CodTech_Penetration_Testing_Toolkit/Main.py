import port_scanner
import ssh_brute
import http_brute

def menu():
    print("\n--- Penetration Testing Toolkit ---")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    print("3. HTTP Directory Brute Forcer")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Select option: ")
        if choice == '1':
            target_ip = input("Enter Target IP: ")
            ports = input("Enter ports (comma-separated, e.g., 22,80,443): ")
            ports = [int(p.strip()) for p in ports.split(",")]
            port_scanner.port_scan(target_ip, ports)
        elif choice == '2':
            ip = input("Target IP: ")
            user = input("Username: ")
            wordlist = input("Path to password list: ")
            ssh_brute.ssh_brute(ip, user, wordlist)
        elif choice == '3':
            url = input("Enter target URL: ")
            wordlist = input("Path to wordlist file: ")
            http_brute.http_dir_brute(url, wordlist)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
