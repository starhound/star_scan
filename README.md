# star_scan
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
