import dns
import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1]

def DNSRequest(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
            print("Domain Names: %s" % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

def SubdomainSearch(domain, dictionary, nums):
    for word in dictionary:
        subdomain = word + "." + domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0, 10):
                s = word + str(i) + "," + domain
                DNSRequest(s)

if __name__ == "__main__":
    target_domain = "google.com"
    subdomains_file = "subdomains.txt"
    dictionary = []

    with open(subdomains_file, "r") as f:
        dictionary = f.read().splitlines()

    SubdomainSearch(target_domain, dictionary, True)
