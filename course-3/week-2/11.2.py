import re

try:
    file = open('actual_sum_42.txt', 'r')
except:
    print('File cannot be opened.')
    exit()

is_test = False
sum = 0

for line in file:
    # Obtain numbers from each line
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        # Extract each number from list of numbers and add it to sum
        for number in numbers:
            sum += int(number)
            if is_test is True:
                print('Number = ', number, ', Sum =', sum)

print(sum)
