number = 1

#while loop
while number <= 5:
    print (number)
    number = number + 1
print ("Bye!")

#conditional loop
number = 1
answer = 'y'
while answer == 'y':
    print (number)
    number = number +1
    answer = input("Do you want the next number? ")

#for loop
number = 1
for number in range(1, 6):
    print (number)

#for loop w/ passing number of iterations
number = 0
for number in range (6):
    print (number)

#for loop w/ increment
number = 1
for number in range (1, 10, 2):
    print (number)

#for loop w/ decrement
for number in range (5, 0, -1):
    print (number)
    
#nesting loops
for i in range (0, 10):
    print ("~~~", i, "~~~")
    for j in range (0, 10):
        print (i * j)
    print()

#compound conditions
#while answer == 'y' or answer == 'Y':

#break, continue, else statements
for number in range(1, 11):
    if number == 4:
        break
        #continue
    print (number)
#print("Thanks!")
else:
    print("Exited normally")


