#breaking a loop
number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")

for number in range(2, 31, 2):
    print(number)

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1
print("Now!")


upper_limit = int(input("Upper limit: "))

for number in range(1, upper_limit):
    print(number)



  