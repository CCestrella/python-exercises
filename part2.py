#number of characters
word = input("Please type in a word: ")

if len(word) > 1:
    print(f"There are {len(word)} letters in the word {word}")

print("thank you!")

# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function. /

number = float(input("Please type in a number: "))

print("The integer part is", int(number))

decimal_part = number -int(number)
print("The decimal part is", round(decimal_part, 2))