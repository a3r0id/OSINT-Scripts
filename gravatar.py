# Author: 
#   github.com/a3r0id

# File:   
#   gravatar.py

# Usage:  
#   python3 gravatar.py

# Description:
#   This script will take any email address and search for a gravatar associated with it.

# Requirements:
#   pip3 install requests hashlib

from requests import get
from hashlib  import md5
from re       import fullmatch

while True:
        
    email = input("[+] Enter email: ")
    
    if not fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        print ("[-] *Invalid email - format is invalid*\n")
        continue
    
    email_hash = str(md5(email.encode('utf-8')).hexdigest())
    
    r = get("https://www.gravatar.com/" + email_hash + ".json")
    
    if "User not found" in r.text:
        print ("[-] *No gravatar found*\n")
        continue
    
    try:
        json = r.json()
    except: 
        print ("[-] *No gravatar found*\n")
        continue
        
    print ("[+] *Gravatar found*")
    print ("[+] Entries Found: " + str(len(json['entry'])))
    
    for entry in json['entry']:
        print ("[+] Preferred Username: " + entry['preferredUsername'])
        print ("[+] Legal Name: " + entry['name']['formatted'])
        print ("[+] Display Name: " + entry['displayName'])
        print ("[+] Profile URL: " + entry['profileUrl'])
        print ("[+] Thumbnail URL: " + entry['thumbnailUrl'])
        print ("[+] Hash: " + entry['hash'])
        print ("[+] Photos: ")
        for photo in entry['photos']:
            print ("    [+] " + photo['value'])
        print ("[+] URLs: ")
        for url in entry['urls']:
            print ("    [+] " + url['value'])
        print("\n")
        
        
        
    