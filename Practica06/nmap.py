import os, socket, nmap
from datetime import datetime

def scan_ports(ip, start_port, end_port):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open('logs.info', 'a') as log_file:
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            scanner = nmap.PortScanner()

            if ip.upper() == 'LOCAL':
                log_file.write(f'[{date} NMAP]: Obtaining IP\n')
                target = socket.gethostbyname(socket.gethostname()) + '/24'
                scanner.scan(target)
                log_file.write(f'[{date} NMAP]: Writing results to {base_path}\\resultados.csv\n')
                with open(f'{base_path}\\resultados.csv', 'w+') as result_file:
                    result_file.write(scanner.csv())
            else:
                for port in range(start_port, end_port + 1):
                    log_file.write(f'[{date} NMAP]: Scanning port {port}\n')
                    res = scanner.scan(ip, str(port))
                    res = res['scan'][ip]['tcp'][port]['state']
                    print(f'The port {port} is {res}.')
        except Exception as e:
            log_file.write(f'[{date} NMAP ERROR]: {e}\n')
            print('Error:', e)

while True:
    try:
        ip = input('Enter the IP to investigate: ')
        if ip == '0':
            break
        start_port = int(input('Enter the starting port: '))
        if start_port == 0:
            break
        end_port = int(input('Enter the ending port: '))
        if end_port == 0:
            break
        scan_ports(ip, start_port, end_port)
        break
    except Exception as e:
        print('Error:', e)
        print('Please enter the data correctly.\n')

