from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all tags of span tags
tag = soup("span")

is_test = False
count = 0
sum = 0

for value in tag:
    number = int(value.text)
    count = count + 1
    sum = sum + number
    if is_test is True:
        print("So far: count = ", count, "sum = ", sum)

print(count)
print(sum)
