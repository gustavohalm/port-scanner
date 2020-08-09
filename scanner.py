import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u",'--url', required=True, help='Target url')
parser.add_argument("-t", '--timeout', required=False, help='Timeout for port scan, default is 0.5 (in s)', default=0.5, type=float)
args = parser.parse_args()

with open('ports', 'r') as ports_file:
    ports = [int(p.strip('\n'))for p in ports_file.readlines()]
    timeout = args.timeout
    print(f'Scanning ports for {args.url}')
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        code = client.connect_ex((args.url, port))
        if code == 0:
            print(f'{args.url}:{port}')
        client.close()
