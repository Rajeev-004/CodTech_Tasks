import requests

def http_dir_brute(target_url, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            print(f"\n[~] Starting directory brute force on {target_url}...\n")
            for line in file:
                directory = line.strip()
                full_url = f"{target_url}/{directory}"
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f"[+] Found: {full_url}")
    except FileNotFoundError:
        print("[!] Wordlist not found.")
    except Exception as e:
        print(f"[!] Error: {e}")

