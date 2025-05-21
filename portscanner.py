import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

#------------------------------
# Port Scanning Function
#------------------------------
def port_scan(ip, port):
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(1)
      if s.connect_ex((ip, port))==0:
        print(f"Port {port} is open")
  except socket.timeout:
    print(f"Timeout on {ip}:{port}")
  except ConnectionRefusedError:
    pass
  except Exception as e:
    print(f"Error: {e}")

#------------------------------
# Main Execution
#------------------------------
def main():
  # Set up the Command Line
  parser = argparse.ArgumentParser(description='Basic Port Scanner')
  parser.add_argument('-t', '--targets', nargs='+', help='target IPs or Domain names', required='True')
  args = parser.parse_args()
  
  
  ports = range(1,1025) # Scan common ports
  with ThreadPoolExecutor(max_workers=100) as executor:
    for port in ports:
      executor.submit(port_scan, target, port)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Scanning interrupted by user")
  except:
    print("An error occurred while scanning ports")
