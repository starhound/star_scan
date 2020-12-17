# Star Scan
Module form of the 'Port Scan' utility

You can find the original utilities (Python file and CLI version) from [here](https://github.com/starhound/PortScan).

To utilize this package, do: *pip3 install star_scan*

```python3
import star_scan.scanner as scanner

ip_address = '127.0.0.1'
start_port = 1
end_port = 1000
scanner.scan_host(ip_address, start_port, end_port)
```

To scan a network:
```python3
import star_scan.scanner as scanner 

#remove the last octet for scan_range()
ip_address = '192.168.1'
start_port = 1
end_port = 1000

#scans ports on all addresses from 192.168.1.1 to 192.168.1.255
scanner.scan_range(ip_address, start_port, end_port)
