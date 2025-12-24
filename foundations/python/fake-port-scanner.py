#Day 02 - Fake Port Scanner
#Purpose: Practice Python basics with a security mindset

targets = ["192.168.1.1", "192.168.1.2" ]
ports = [22, 80, 443]

def fake_scan(ip, port):
    if port == 22:
        return "open"
    return "closed"

for ip in targets:
    print(f"\nTarget: {ip}")

    for port in ports:
        status = fake_scan(ip, port)
        print(f" Port {port}: {status}" )