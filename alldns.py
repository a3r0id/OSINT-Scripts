# Author: 
#   github.com/a3r0id 

# File:   
#   alldns.py

# Usage:  
#   python3 alldns.py

# Description:
#   This script will take any domain and search for all (common) dns records associated with it.

# Requirements:
#   pip3 install dnspython

import dns.resolver as Resolver
from   re import search, compile

# Thanks ChatGPT for the list of query types :)
query_types = [
    ['A', 'Address Record'],
    ['AAAA', 'IPv6 Address Record'],
    ['AFSDB', 'AFS Database Record'],
    ['CNAME', 'Canonical Name Record'],
    ['CERT', 'Certificate Record'],
    ['DHCID', 'DHCP Identifier Record'],
    ['DNAME', 'Delegation Name Record'],
    ['DS', 'Delegation Signer Record'],
    ['KEY', 'Key Record'],
    ['LOC', 'Location Record'],
    ['MX', 'Mail Exchange Record'],
    ['NAPTR', 'Naming Authority Pointer Record'],
    ['NS', 'Name Server Record'],
    ['PTR', 'Pointer Record'],
    ['RP', 'Responsible Person Record'],
    ['SOA', 'Start of Authority Record'],
    ['SSHFP', 'SSH Public Key Fingerprint Record'],
    ['SRV', 'Service Record'],
    ['TLSA', 'Transport Layer Security Authenticator Record'],
    ['TXT', 'Text Record']
]

while True:
    
    domain = input("[+] Enter domain: ")
    
    if not search(compile(r'(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))'), domain):
        print ("[-] *Invalid domain - format is invalid*\n")
        continue
    
    for query_type in query_types:
        try:
            print (f"[+] *{query_type[0]} - {query_type[1]}*")
            
            answers = Resolver.resolve(domain, query_type[0])
            
            for rdata in answers:
                print ("\t[+] " + str(rdata))
        except:
            continue


    
    
    
