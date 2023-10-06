num_of_nums = int(input("How many numbers do you want to average? "))

sum = 0.0
#for count in range (num_of_nums):
for count in range (num_of_nums, 0, -1):
    value = int(input("Enter value: "))
    sum = sum + value

average = sum / num_of_nums
print("The average is:", average)
