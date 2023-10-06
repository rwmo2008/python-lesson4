sum = 0.0
num = 0
entry = 1
while entry != -1:
    entry = int(input("Enter a number: "))
    if entry != -1:
        num = num + 1
        sum = sum + entry
    else:
        break

average = sum / num
print("The average is:", average)
