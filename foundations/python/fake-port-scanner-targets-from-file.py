
ports = [22, 80, 443]

def load_targets(filename):
    targets = []

    with open(filename, "r") as f:
        for line in f:
            targets.append(line.split())

    return targets

def fake_scan(ip, port)
    if port == 22:
        return "open"
    return "closed"

targets = load_targets("foundations/python/targets.txt")

for ip in targets:
    print(f"\nTarget: {ip}")

    for port in ports:
        status = fake_scan(ip, port)
        print(f" Port {port}: {status}")

        