import dns
import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        # Attempt to perform a reverse DNS lookup using the given IP address
        result = socket.gethostbyaddr(ip)
    except:
        # If an exception occurs (e.g., no reverse DNS entry found), return an empty list
        return []
    # Return a list containing the primary domain name and aliases obtained from the reverse DNS lookup
    return [result[0]] + result[1]

def DNSRequest(domain):
    try:
        # Attempt to resolve the 'A' record for the given domain using DNS resolution
        result = dns.resolver.resolve(domain, 'A')
        if result:
            # If resolution is successful, print the domain and its associated IP addresses
            print(domain)
            for answer in result:
                print(answer)
            # Print the associated domain names obtained from reverse DNS lookup for each IP address
            print("Domain Names: %s" % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        # Handle DNS resolution exceptions (NXDOMAIN: Non-Existent Domain, Timeout)
        return

def SubdomainSearch(domain, dictionary, nums):
    for word in dictionary:
        # Generate subdomains by combining words from a dictionary with the target domain
        subdomain = word + "." + domain
        # Perform DNS resolution for the generated subdomain
        DNSRequest(subdomain)
        if nums:
            # If specified, also try numeric variations of the subdomain (e.g., subdomain0, subdomain1, etc.)
            for i in range(0, 10):
                s = word + str(i) + "," + domain
                DNSRequest(s)

if __name__ == "__main__":
    # Target domain for subdomain enumeration
    target_domain = "google.com"
    # File containing a dictionary of words for subdomain generation
    subdomains_file = "subdomains.txt"
    dictionary = []

    # Read the dictionary file and store the words in the 'dictionary' list
    with open(subdomains_file, "r") as f:
        dictionary = f.read().splitlines()

    # Perform subdomain enumeration for the target domain using the generated subdomains
    SubdomainSearch(target_domain, dictionary, True)
