import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)

response = urllib.request.urlopen(url)
data = response.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count:', len(lst))

num = 0
for item in lst:
    x = item.find('count').text
    num = num + int(x)
print('Sum:', num)
