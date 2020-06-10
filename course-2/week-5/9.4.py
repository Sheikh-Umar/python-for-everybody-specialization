name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

is_test = False
my_dict = dict()

for line in handle:
    if line.startswith('From ') is False:
        continue
    words = line.split()
    if is_test is True:
        print('line:', line)
        print('words:', words)

    key_word = words[1]
    my_dict[key_word] = my_dict.get(key_word, 0) + 1

if is_test is True:
    print('Dictionary:', my_dict)

big_count = None
big_word = None
for word, count in my_dict.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = word
        if is_test is True:
            print('So far: big_count =', big_count, ', big_word =', big_word)

print(big_word, big_count)
