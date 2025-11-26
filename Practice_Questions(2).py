# # 1. Check if number is positive
# a = eval(input("Enter the number :"))

# if a > 0:
#     print(f"{a} is a positive number")
# else:
#     print(f"{a} is not a positive number")


# # 2. Check if number is divisible by 2
# b = eval(input("Enter a number :"))

# if b / 2 == 0:
#     print(f"{b} is divisible by 2")
# else:
#     print(f"{b} is not divisible by 2")


# # 3. Print message if age greater than 18
# Candidate = eval(input("Enter the number :"))

# if Candidate > 18:
#     print(f"{Candidate} age is greater than 18")
# else:
#     print(f"{Candidate} age is smaller than 18")


# # 4. Check if a string length is greater than 5
# str = "Python Development"

# if len(str) > 5:
#     print(f"{str} string length is greater than 5")
# else:
#     print(f"{str} string length is smaller than 5")


# # 5. Check if a number is negative
# c = eval(input("Enter the number :"))

# if c < 0:
#     print(f"{c} is a negative number")
# else:
#     print(f"{c} is not a negative number")


# # 6. Check if a char is vowel
# char = input("Enter the letter :")

# if (char == 'a' or char == 'e' or char == 'i' or
#     char == 'o' or char == 'u' or char == 'A' or 
#     char == 'E' or char == 'I' or char == 'O' or 
#     char == 'U'):
#     print(f"{char} is a vowel")
# else:
#     print(f"{char} is not a vowel")


# # 7. Print message if number is multiply of 10
# m = eval(input("Enter a number :"))

# if m % 10 == 0:
#     print(f"{m} is multiple of 10")
# else:
#     print(f"{m} is not multiple of 10")


# # 8. Check if list is not empty
# list = [12, 34, 56, 12, "Python"]

# if len(list) == 0:
#     print(f"{list} is empty")
# else:
#     print(f"{list} is not empty")


# # 9. Print message if number is greater than 100
# num = eval(input("Enter the number :"))

# if num > 100:
#     print(f"{num} is greater than 100")
# else:
#     print(f"{num} is not greater than 100")


# # 10. Check if a word contains letter 'a'
# word = input("Enter the word :")

# if 'a' in word or 'A' in word:
#     print(f"{word} contains letter 'a'")
# else:
#     print(f"{word} does not contains letter 'a'")


# # 11. Check the given number is even or odd
# n = eval(input("Enter the number :"))

# if n % 2 == 0:
#     print(f"{n} is a even number")
# else:
#     print(f"{n} is a odd number")


# # 12. Check eligibility for voting
# age = eval(input("Enter the age :"))

# if age >= 18:
#     print(f"{age} is eligible for voting")
# else:
#     print(f"{age} is not eligible for voting")


# # 13. Check if a number is positive or negative
# number = eval(input("Enter the number :"))

# if number > 0:
#     print(f"{number} is a positive number")
# else:
#     print(f"{number} is negative number")


# # 14. Check password length
# password = input("Enter the password :")
# print(len(password))


# # 15. Check if temp is hot or cool
# temp = eval(input("Enter the temperature :"))

# if temp > 20:
#     print(f"{temp} is hot temperature")
# else:
#     print(f"{temp} is cool temperature")


# # 16. Check if number is divisible by 3
# v = eval(input("Enter the number :"))

# if v % 3 == 0:
#     print(f"{v} is divisible by 3")
# else:
#     print(f"{v} is not divisible by 3")


# # 17. Check multiple of 3 & 4
# t = eval(input("Enter the number :"))

# if t % 3 == 0 and t % 4 == 0:
#     print(f"{t} is a multiple of 3 & 4")
# else:
#     print(f"{t} is not a multiple of 3 & 4")


# # 18. Give a bonus to employee according to its salary
# sal = eval(input("Enter the salary :"))
# bonus = 0.10

# if sal >= 25000:
#     bonus_sal = sal + (sal * bonus)
#     print(f"{bonus_sal} is the bonus salary of employee")
# else:
#     print(f"{sal} employee is not eligible for bonus salary")


# # 19. Classify the temperature
# heat = eval(input("Enter the temperature :"))

# if heat > 40:
#     print(f"{heat} is hot temperature")
# elif heat > 20 and heat <= 40:
#     print(f"{heat} is warm temperature")
# elif heat >= 0 and heat <= 20:
#     print(f"{heat} is cool temperature")
# else:
#     print(f"{heat} is cold temperature")


# # 20. Determine a category based on age
# epoch = eval(input("Enter the age :"))

# if epoch > 0 and epoch < 13:
#     print(f"The category of {epoch} age is child")
# elif epoch >= 13 and epoch < 18:
#     print(f"The category of {epoch} age is teenager")
# elif epoch >= 18 and epoch < 60:
#     print(f"The category of {epoch} age is adult")
# else:
#     print(f"The category of {epoch} age is senior citizen")


# # 21. Month numbers to month name
# int = int(input("Enter the month number :"))

# if int == 1:
#     print(f"{int} is January")
# elif int == 2:
#     print(f"{int} is February")
# elif int == 3:
#     print(f"{int} is March")
# elif int == 4:
#     print(f"{int} is April")
# elif int == 5:
#     print(f"{int} is May")
# elif int == 6:
#     print(f"{int} is June")
# elif int == 7:
#     print(f"{int} is July")
# elif int == 8:
#     print(f"{int} is August")
# elif int == 9:
#     print(f"{int} is September")
# elif int == 10:
#     print(f"{int} is October")
# elif int == 11:
#     print(f"{int} is November")
# elif int == 12:
#     print(f"{int} is December")
# else:
#     print("Enter valid month number")


# # 22. Check type of triangle
# side_a = int(input("Enter the number :"))
# side_b = int(input("Enter the number :"))
# side_c = int(input("Enter the number :"))

# if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
#     print(f"Invalid {side_a}, {side_b}, {side_c} sides do not form a triangle")
# elif side_a == side_b and side_b == side_c:
#     print(f"Equilateral triangle , {side_a}, {side_b}, {side_c} all 3 sides are equal")
# elif side_a == side_b or side_a == side_c or side_b == side_c:
#     print(f"Isoceles triangle {side_a}, {side_b}, {side_c} only 2 sides are equal")
# else:
#     print(f"Scalene triangle {side_a}, {side_b}, {side_c} no sides are equal")


# # 23. Traffic light system
# col = input("Enter the colour :")

# if col == "red" or col == "Red":
#     print(f"The colour is {col}, STOP!")
# elif col == "yellow" or col == "Yellow":
#     print(f"The colour is {col}, SLOW DOWN!")
# elif col == "green" or col == "Green":
#     print(f"The colour is {col}, GO!")
# else:
#     print(f"{col} is a invalid input")


# 24. Determine the largest of three numbers
dig1 = eval(input("Enter the first number :"))
dig2 = eval(input("Enter the second number :"))
dig3 = eval(input("Enter the third number :"))

if dig1 > dig2 and dig1 > dig3:
    print(f"{dig1} is largest than the {dig2} & {dig3}")
elif dig2 > dig1 and dig2 > dig3:
    print(f"{dig2} is largest than the {dig1} & {dig3}")
else:
    print(f"{dig3} is largest than the {dig1} & {dig2}")