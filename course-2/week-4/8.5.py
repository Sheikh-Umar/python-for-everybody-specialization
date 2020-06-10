fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
for data in fh:
    sentence = data.split()
    print(sentence)

print("There were", count, "lines in the file with From as the first word")
