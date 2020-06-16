from bs4 import BeautifulSoup
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags_lst = list()
is_test = False

for x in range(0, count):
    tags = soup('a')
    my_tags = tags[position - 1]
    tag_to_get = my_tags.get('href', None)
    url = str(tag_to_get)
    if is_test is True:
        print('url = ', url)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(my_tags.get('href', None))
