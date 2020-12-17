import socket
import sys
import ipaddress
import logging


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def scan_host(ip_addr, start_port, end_port):
    status_check = check_arguments(ip_addr, start_port, end_port)
    if status_check == False:
        return
    logging.info('[*] Starting TCP port scan on host %s' % ip_addr)
    # Begin TCP scan on host
    tcp_scan(ip_addr, start_port, end_port)
    logging.info('[+] TCP scan on host %s complete' % ip_addr)


def scan_range(network, start_port, end_port):
    status_check = check_arguments(network + ".1", start_port, end_port)
    if status_check == False:
        return
    logging.info('[*] Starting TCP port scan on network %s.0' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, start_port, end_port)
    logging.info('[+] TCP scan on network %s.0 complete' % network)


def tcp_scan(ip_addr, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip_addr, port)):
                logging.info('[+] %s:%d/TCP Open' % (ip_addr, port))
                tcp.close()
        except Exception as e:
            logging.error(e)


def check_arguments(ip_addr, start_port, end_port):
    try:
        ipaddress.ip_address(ip_addr)
    except ValueError:
        logging.error("Did not supply a valid IP address.")
        return False

    try:
        x = int(start_port)
    except ValueError:
        logging.error("Did not supply a valid start port.")
        return False

    try:
        y = int(end_port)
    except ValueError:
        logging.error("Did not supply a valid end port.")
        return False
        
    logging.info("Star-Scan arguments valid, starting scan.")
    return True
