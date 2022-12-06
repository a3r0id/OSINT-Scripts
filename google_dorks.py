# Author: 
#   github.com/a3r0id 

# File:   
#   google_dorks.py

# Usage:  
#   python3 google_dorks.py

# Description:
#   This script will help you build a "google dorking" query.

# Requirements:
#   None

from urllib.parse import quote_plus

operators = [
["site", "site:example.com - searches for results within the specified website"],
["inurl", "inurl:keyword - searches for results with the specified keyword in the URL"],
["intext", "intext:keyword - searches for results with the specified keyword in the text of the page"],
["filetype", "filetype:pdf - searches for results with the specified file type"],
["related", "related:example.com - searches for websites related to the specified website"],
["intitle", "intitle:keyword - searches for results with the specified keyword in the title of the page"],
["allintitle", "allintitle:keywords - searches for results with all the specified keywords in the title of the page"],
["cache", "cache:example.com - shows the cached version of the specified website"],
["define", "define:keyword - shows the definition of the specified keyword"],
["stocks", "stocks:GOOG - shows information about the specified stock symbol"],
]

while True:
    
    print ("\r\n[+] *Google Dorks Generator - Select Operators*\r\n")
    
    for i, op in enumerate(operators):
        print (f"[{i}] {op[1]}")
    
    url   = "https://www.google.com/search?q="
    query = []
    while True:
        try:
            op    = operators[int(input("\r\n[+] Enter corresponding number for the next operator or 100 to exit: ").strip())]
            value = input(f"[+] Enter value for {op[0]}: ").strip()
            query.append(f"{op[0]}:{value}")
        except:
            print ("\r\n[->] *Continuing...*")
            break
        
    print ("\r\n[+] *Query*")
    print (url + quote_plus(" ".join(query)))        
        