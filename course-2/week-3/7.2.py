# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
string = fh.read()

count = 0
total = 0
ans = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
        
    # Count number of lines that starts with 'X-DSPAM-Confidence'
    count = count + 1
    
    # Extract value from line that starts with 'X-DSPAM-Confidence'
    number = float(line[20:])
    
    total = total + number

ans = total / count
print("Average spam confidence:", ans)

