import socket
import urllib.request, urllib.error
from html.parser import HTMLParser

# Using socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.settimeout(5)

try:
    mysock.connect(("data.pr4e.org", 80))
    cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
    mysock.send(cmd)

    char_count_socket = 0
    word_count_socket = 0

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        char_count_socket += len(data)
        words = data.decode().split()
        word_count_socket += len(words)
        print(data.decode())
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    mysock.close()

# Using urllib
url = "http://data.pr4e.org/romeo.txt"

try:
    with urllib.request.urlopen(url, timeout=5) as fhand:
        char_count_urllib = 0
        word_count_urllib = 0
        for line in fhand:
            char_count_urllib += len(line)
            words = line.decode().split()
            word_count_urllib += len(words)
            print(line.decode().strip())
except urllib.error.URLError as e:
    print(f"URL error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


print(f"Total characters using socket: {char_count_socket}")
print(f"Total characters using urllib: {char_count_urllib}")

print(f"Total words using socket: {word_count_socket}")
print(f"Total words using urllib: {word_count_urllib}")

avg_word_length_urllib = 0 if word_count_urllib == 0 else char_count_urllib / word_count_urllib
print(f"Average word length using urllib: {avg_word_length_urllib}")

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    print(f"Found hyperlink: {attr[1]}")

html_url = "http://www.example.com"
try:
    with urllib.request.urlopen(html_url, timeout=5) as html_fhand:
        html_content = html_fhand.read().decode()
        parser = MyHTMLParser()
        parser.feed(html_content)
except urllib.error.URLError as e:
    print(f"URL error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
