from scapy.all import *

ports = [5, 80, 53, 443, 445, 8080, 8443]

def SynScan(host):
    ans, unans = sr(IP(dst=host)/TCP(sport=5555, dport=ports, flags="S"), timeout=2, verbose=0)
    print("Open ports at {}: ".format(host))
    for s, t in ans:
        if s[TCP].dport == s[TCP].sport:
            print(s[TCP].dport)

def DNSScan(host):
    ans, unans = sr(IP(dst=host)/UDP(sport=5555, dport=53)/DNS(rd=1, qd=DNSQR(qname="google.com")), timeout=2, verbose=0)
    if ans:
        print("DNS Server at {}".format(host))

host = "8.8.8.8"
SynScan(host)
DNSScan(host)
