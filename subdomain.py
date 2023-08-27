import requests
import time
import urllib3
import sys

version = 1.0

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--domain",required=True,help="Target Domain")
    parser.add_argument("-o", "--output", required=False, help="Output to file")
    return parser.parse_args()

def banner():
    global version
    print("Name: Subdomain Scanner")
    print(f"version: {version}")
    print("Author: Ashwanth Balaji")
    time.sleep(2)

def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print("[+] Invalid url, please try again")
        sys.exit(1)
    return host

def write_to_files(subdomain,output_file):
    with open(output_file,"a") as fp:
        fp.write(subdomain + "\n")
        fp.close()

def main():
    banner()
    subdomains = []
    args = parse_args()
    target = parse_url(args.domain)
    output = args.output

    req = requests.get(f"https://crt.sh/?q=%.{target}&output=json")

    if req.status_code != 200:
        print("[*] Inforamtion is not available")
        sys.exit(1)
    for (key,value) in enumerate(req.json()):
        subdomains.append(value["name_value"])

    print(f"\n[!] ***********TARGET: {target}***************[!]\n")
    subs = sorted(set(subdomains))

    for s in subs:
        print(f"[*] {s}")
    print("Program has been completed")

main()
+