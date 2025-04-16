import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_target_url():
    """Gets the target website URL from the user."""
    url = input("Enter the target website URL: ")
    return url

def fetch_webpage(url):
    """Fetches the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def find_links(html_content, base_url):
    """Finds all the links on a webpage."""
    links = set()
    soup = BeautifulSoup(html_content, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        absolute_link = urllib.parse.urljoin(base_url, link)
        links.add(absolute_link)
    return list(links)

def check_sql_injection_url(url):
    """Checks for potential SQL Injection vulnerabilities in URL parameters."""
    print(f"\n[+] Checking for potential SQL Injection in URL parameters for: {url}")
    payloads = ["'", "--", "OR 1=1", "OR '1'='1"]
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    for param, values in query_params.items():
        original_value = values[0]
        for payload in payloads:
            test_url = url.replace(f"{param}={original_value}", f"{param}={original_value}{payload}")
            try:
                response = requests.get(test_url)
                # Look for specific error messages or changes in response
                if "SQL syntax" in response.text.lower() or "mysql_fetch" in response.text.lower() or "error in your sql" in response.text.lower():
                    print(f"[!] Potential SQL Injection vulnerability found in parameter '{param}' with payload '{payload}'")
                    print(f"    Test URL: {test_url}")
            except requests.exceptions.RequestException as e:
                print(f"    Error testing {test_url}: {e}")

def check_xss_url(url):
    """Checks for potential XSS vulnerabilities in URL parameters."""
    print(f"\n[+] Checking for potential XSS in URL parameters for: {url}")
    payloads = ["<script>alert('XSS')</script>", '"<script>alert(1)</script>"', "'<script>alert(2)</script>'"]
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    for param, values in query_params.items():
        original_value = values[0]
        for payload in payloads:
            test_url = url.replace(f"{param}={original_value}", f"{param}={payload}")
            try:
                response = requests.get(test_url)
                # Look for the payload in the response
                if payload in response.text:
                    print(f"[!] Potential XSS vulnerability found in parameter '{param}' with payload '{payload}'")
                    print(f"    Test URL: {test_url}")
            except requests.exceptions.RequestException as e:
                print(f"    Error testing {test_url}: {e}")

if __name__ == "__main__":
    target_url = get_target_url()
    if target_url:
        print(f"\n[+] Starting vulnerability scan on: {target_url}")

        # Basic URL parameter scanning
        check_sql_injection_url(target_url)
        check_xss_url(target_url)

        # Example of basic link discovery (can be expanded for crawling)
        html_content = fetch_webpage(target_url)
        if html_content:
            links = find_links(html_content, target_url)
            print("\n[+] Found the following links:")
            for link in links:
                print(f"  - {link}")
                # You could apply vulnerability checks to these links as well