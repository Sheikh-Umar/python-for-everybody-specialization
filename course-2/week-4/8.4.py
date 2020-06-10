fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    # sentence is a string containing words and spaces before the new line token
    # so we have to extract eah word in sentence, and add it to lst if it is not in lst
    sentence = line.split()
    for i in sentence:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
