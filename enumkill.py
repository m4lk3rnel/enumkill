import requests
import sys
import threading
from queue import Queue

if len(sys.argv) != 2:                                                                                                       
    print("")                                                                                                                
    print("usage: python3 enumkill.py <url>")                                              
    print("example: python3 enumkill.py http://example.com")
    exit()

url = sys.argv[1]

q = Queue()
wordlist = []

threads = 150

with open("/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt", "r") as f:
    wordlist = f.read().splitlines()

for word in wordlist:
    # 'put' the words into the queue
    if word.startswith("#"):
        continue

    q.put(word)

if url[len(url) - 1] != "/":
    url += "/"

def enumerate():
    while not q.empty():
        # 'get' the words from the queue
        word = q.get()

        try:
            r = requests.get(url + word)

            if r.status_code == 200 or r.status_code == 403 or r.status_code == 301:
                print("/"+ word + " " + str(r.status_code))

        finally:
            q.task_done()

print("===============================================================")

# start threads
for _ in range(threads):
    t = threading.Thread(target=enumerate)
    t.daemon = True
    t.start()


q.join() # block the main thread until all worker thread are done

print("===============================================================")



