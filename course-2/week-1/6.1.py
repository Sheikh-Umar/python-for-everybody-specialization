text = "X-DSPAM-Confidence:    0.8475";
isTest = False

# Remove space in middle of text
text = text.replace("    ", "")

# find index of colon. All characters after : is the number
pos = text.find(":")
if(isTest is True):
    print(pos)

# Obtain string of number
number_string = text[pos + 1 : len(text)]
if(isTest is True):
    print(number_string)

# Obtain float value of number_string
float_number_string = float(number_string)

print(float_number_string)
