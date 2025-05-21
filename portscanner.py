import argparse
import socket
from concurrent.futures import ThreadPoolExecutor

#------------------------------
# Terminal Commands (IN PROGRESS)
#------------------------------
def parse_arg():
  parser = argparse.ArgumentParser(description="Basic Port Scanner")

  # Required inputs
  parser.add_argument('-t', '--target',)


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
  args = parse_arg()
  ports = range(1,1025) # Scan common ports
  with ThreadPoolExecutor(max_workers=100) as executor:
    for port in ports:
      executor.submit(port_scan, target, port)

if __name__ == "__main__":
  main()
