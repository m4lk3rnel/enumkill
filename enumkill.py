import requests
import sys


if len(sys.argv) != 2:                                                                                                       
    print("")                                                                                                                
    print("usage: python3 dirkill.py <url>")                                              
    print("example: python3 dirkill.py http://example.com")
    exit()

url = sys.argv[1]

r = requests.get(url)
print(r.status_code)
