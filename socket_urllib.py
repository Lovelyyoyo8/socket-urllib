import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.settimeout(5)
try:
    mysock.connect(("data.pr4e.org", 80))
    cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode())
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    mysock.close()

import urllib.request, urllib.error

url = "http://data.pr4e.org/romeo.txt"
try:
    with urllib.request.urlopen(url, timeout=5) as fhand:
        for line in fhand:
            print(line.decode().strip())
except urllib.error.URLError as e:
    print(f"URL error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e}")

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
