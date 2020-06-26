import json
import urllib.request

counts = list()

is_test = False

while True:
        address = input('Enter location:')
        print('Retrieving', address)

        connection = urllib.request.urlopen(address)
        data = connection.read()
        if is_test is True:
            pritn('data:', data)
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        comments = js['comments']
        for comment in comments :
            counts.append(comment['count'])

        print('Count', len(comments))
        print('Sum', sum(counts))
