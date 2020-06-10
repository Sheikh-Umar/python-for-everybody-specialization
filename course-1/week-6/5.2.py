largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        value = int(num)
        if smallest is None or value < smallest:
            smallest = value
        if largest is None or value > largest:
            largest = value
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
