import argparse
import threading
from cfgparser import parse_json_file
from attacker import Attacker
import time
import random

def main():
    parser = argparse.ArgumentParser(description='!EDUCATIONAL PURPOSE ONLY! Automatic Malicious Traffic Generator made for UTMN VKR 2024. Have fun! !EDUCATIONAL PURPOSE ONLY!')
    
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-c', '--config', type=str, help="use config file")
    args = parser.parse_args()

    try:
        ips, ports = parse_json_file(args.config)
        print(f"Parsed IPs: {ips}")
        print(f"Parsed Ports: {ports}")
        print("Starting recon and attack NOW!")
        while True:
            thread_list:list[threading.Thread] = []
            time.sleep(random.randint(5,15))
            for ip in ips:
                thread_list.append(threading.Thread(target=Attacker(ip, ports).attack))
            for pr in thread_list:
                pr.start()
                pr.join()
    except FileNotFoundError:
        print(f"File {args.config} not found")
    except Exception:
        print("Read error")

    

if __name__ == '__main__':
    main()
