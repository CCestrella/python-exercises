# from math import sqrt

# # number of characters
# word = input("Please type in a word: ")

# if len(word) > 1:
#     print(f"There are {len(word)} letters in the word {word}")

# print("thank you!")

# # Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

# number = float(input("Please type in a number: "))

# print("The integer part is", int(number))

# decimal_part = number - int(number)
# print("The decimal part is", round(decimal_part, 2))

# # The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.

# number = int(input("Please type in a number: "))

# if number > 100:
#     print("The number was greater than one hundred")
#     new_number = number - 100
#     print("Now its value has decreased by one hundred")
# else: 
#     new_number = number

# print("Its value is now", int(new_number))
# print(int(new_number), " must be my lucky number!")
# print("Have a nice day!")

# # This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. 

# while True:
#     print("hi!")
#     answer = input("Shall we continue? ")
#     if answer == "no":
#         break
# print("Ok then")

# # Please write a program which asks the user for integer numbers.
# # If the number is below zero, the program should print out the message "Invalid number".
# # If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
# # In either case, the program should then ask for another number.
# # If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

# while True:
#     number = int(input("Please enter a number:"))
#     if number == 0:
#         break
#     elif number < 0:
#         print("Invalid number.")
#     else:
#         print(sqrt(number))
# print("Exiting....")

# # This program should print out a countdown. The code is as follows:

# number = 5
# print("Countdown!")
# while True:
#     print(number)
#     number = number - 1
#     if number > 0:
#         break

# print("Now!")


# Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

# while True:
#     password = input("Create a password: ")
#     confirm_password = input("Confirm password: ")

#     if password == confirm_password:
#         break
#     print("Incorrect Password. Please try again!")

# print("User Account Created!")

# Three attempts for pin

# attempts = 0 

# while True:
#     code = input("Please type in your pin: ")
#     attempts += 1

#     if code == "1234":
#         success = True
#         break

#     if attempts == 3:
#         success = False
#         break

#     print("Incorrect... Try again!")

# if success:
#     print("Correct pin entered!")

# else:
#     print("Too many attempts!")

#modulo

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd.")

# Add password check program that compares user input to a preset password and prints success or failure message

# correct = "kittycat"
# password = input("Please type in the password: ")

# if password == correct:
#     print("You have entered the correct password!")  
# else:
#     print("You have entered an incorrect password!")
    

# Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

# age = int(input("Please type your age: "))

# if age < 18:
#     print("You are not of age!")
# else:
#     print("You are of age!")


#  Add program to compare home and away goals and print match result

# goals_home = int(input("Home goals scored: "))
# goals_away = int(input("Away goald scored:)"))

# if goals_home > goals_away:
#     print("The home team won!")
# elif goals_away > goals_home:
#     print("The away team won!")
# else:
#     print("It's a tie!")

# Add holiday calendar program that prints holiday name based on user input date
# print("Holiday calendar")
# date = input("What is the date today? ")

# if date == "Dec 26":
#     print("It's Boxing Day")
# elif date == "Dec 31":
#     print("It's Hogmanay")
# elif date == "Jan 1":
#     print("It's New Year's Day")

# print("Thanks and bye.")

# Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

# number_1 = int(input("Please enter a number: "))
# number_2 = int(input("Please enter another number: "))

# if number_1 > number_2:
#     print(number_1)
# elif number_2 > number_1:
#     print(number_2)
# else:
#     print("They're both equal!")


print("Person 1:")
name1 = input("Name: ")
age1 = int(input("Age: "))


print("Person 2:")
name2 = input("Name: ")
age2 = int(input("Age: "))


if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")


# Ask for two words
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

# Compare and print the word that comes alphabetically last
if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")
