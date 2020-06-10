name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour_count = dict()
hour_list = []
is_test = False

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        time = words[5].split(':')
        hour = time[0]
        if is_test is True:
            print('time:', time, 'hour:', hour)
        hour_count[hour] = hour_count.get(hour, 0) + 1
    else:
        continue

if is_test is True:
    print('hour_count:', hour_count)

for key, val in hour_count.items():
    hour_list.append((key, val))

hour_list.sort()
for key, val in hour_list:
    print(key, val)
