import argparse
import socket
from concurrent.futures import ThreadPoolExecutor


#------------------------------
# User inputs
#------------------------------
print("What is the IP you want to scan?")
target = input()

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
  ports = range(1,1025) # Scan common ports
  with ThreadPoolExecutor(max_workers=100) as executor:
    for port in ports:
      executor.submit(port_scan, target, port)

if __name__ == "__main__":
  main()
