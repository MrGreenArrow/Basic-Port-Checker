import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

#------------------------------
# Port Scanning Function
#------------------------------
class ScanPort:
    def __init__(self, target, port, timeout, scan_type):
        super().__init__()
        self.target = target
        self.port = port
        self.timeout = timeout
        self.scan_type = scan_type
        self.result = None
        
    def run(self):
        try:
            client = socket.socket(socket.AF_INET, self.scan_type)
            client.settimeout(self.timeout)
            client.connect((self.target, self.port))
            print(colored(f"[+] Port {self.port} is open.", "green"))
            try:
                banner = client.recv(1024).decode().strip()  
                print(f"Banner for Port {self.port}: {banner}")
                if "ftp" in banner.lower() and "2.2.0" in banner: 
                    print(colored("[!] CVE-2011-2523: vsFTPd 2.2.0 backdoor detected.", "yellow"))
            except Exception as e:
                print(colored(f"Unable to get banner for port {self.port}: {e}", "blue"))
        except Exception as e:
            print(colored(f"[-] Port {self.port} is closed: {e}", "red"))

#------------------------------
# Main Execution
#------------------------------
def main():
    parser = argparse.ArgumentParser(description='Basic Port Scanner')
    parser.add_argument('-t', '--targets', nargs='+', help='Target IPs/Domains', required=True) 
    parser.add_argument('-p', '--port-range', default='1-100', help='Port range (e.g., 1-100 or "all")')
    parser.add_argument('-T', '--timeout', default=1.0, type=float, help='Timeout in seconds (default: 1.0)')
    args = parser.parse_args()

    # Parse port range
    start_port, end_port = parse_port_range(args.port_range) 
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for target in args.targets:
            for port in range(start_port, end_port + 1):
                scanner = ScanPort(target, port, args.timeout, socket.SOCK_STREAM) 
                executor.submit(scanner.run)

def parse_port_range(port_range):
    if port_range.lower() == 'all':
        return (1, 65535)
    else:
        start, end = map(int, port_range.split('-'))
        return (start, end)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.") 
    except Exception as e:
        print(f"[!] Critical error: {e}")
    print("An error occurred while scanning ports")
