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


limit = int(input("Upper limit: "))
number = 1

while number <= limit:
    print(number)
    number *= 2

limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1

while number <= limit:
    print(number)
    number *= base

limit = int(input("Limit: "))
total = 0
number = 1

while total < limit:
    total += number
    number += 1

print(total)
# Ask the user for a string
text = input("Please type in a string: ")

# Ask the user for an amount and convert it to an integer
amount = int(input("Please type in an amount: "))

# Print the string multiplied by the amount, all on one line
print(text * amount)

# Ask the user for two strings
string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

# Compare their lengths
if len(string1) > len(string2):
    print(f"{string1} is longer")
elif len(string2) > len(string1):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

# Ask the user for a string
user_input = input("Please type in a string: ")

# Loop through the string in reverse order
for char in reversed(user_input):
    print(char)
