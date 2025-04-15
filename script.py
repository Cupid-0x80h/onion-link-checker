import requests
from docx import Document

# Tor proxy settings
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def read_onion_links_from_docx(file_path):
    doc = Document(file_path)
    links = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if ".onion" in text:
            links.append(text)
    return links

def check_onion_link_status(link):
    try:
        response = requests.get(link, proxies=proxies, timeout=15, allow_redirects=True)
        return response.status_code
    except requests.RequestException:
        return None

def main():
    input_file = 'onion-links.docx'
    working_file = 'working-links.txt'
    redirect_file = 'redirect-links.txt'
    not_working_file = 'notworking-links.txt'

    links = read_onion_links_from_docx(input_file)
    
    with open(working_file, 'w') as wf, open(redirect_file, 'w') as rf, open(not_working_file, 'w') as nwf:
        for link in links:
            print(f"Checking: {link}")
            status = check_onion_link_status(link)
            if status == 200:
                wf.write(f"{link} - Status: 200 OK\n")
                print(f"[+] Working: {link}")
            elif status in (301, 302):
                rf.write(f"{link} - Status: {status} Redirect\n")
                print(f"[~] Redirect: {link}")
            else:
                reason = f"Status: {status}" if status else "No Response"
                nwf.write(f"{link} - {reason}\n")
                print(f"[-] Not Working: {link} - {reason}")

if __name__ == "__main__":
    main()
