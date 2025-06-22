#breaking a loop
number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")

for number in range(2, 31, 2):
    print(number)
