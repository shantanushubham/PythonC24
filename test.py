# a = 5 # Creating a variable
# b = 10
# sum = a + b
# print(sum)

# # let the permiter of the square be x
# # x = 4 * edge
# # since edge = 10
# # therefore, x = 4 * 10 = 40

# Conditional Programming in Python:


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))

# if a < 0:
#     print("a is negative")
# if b < 0:
#     print("b is negative")
# else:
#     print(a + b)


# match_result = input("Enter the match result: ")

# if match_result == "win":
#     print("You won the match")
# elif match_result == "lose":
#     print("You lost the match")
# elif match_result == "draw":
#     print("The match was a draw")
# else:
#     print("Invalid match result")

# match match_result:
#     case "win":
#         print("You won the match")
#     case "lose":
#         print("You lost the match")
#     case "draw":
#         print("The match was a draw")
#     case _:
#         print("Invalid match result")


# Functions aka Methods in Python: 
# y = f(x)
# y = depedent variable
# f = function or the name of the function
# x = independent variable

# Area of Rectangle
# y = area(length, breadth)
# y = dependent variable
# area = function
# length, breadth = independent variables

# area(length, breadth) = length * breadth
# y = area(10, 20)
# y = 200 sq m

# Creating a function
def area(length, breadth):
    result = length * breadth
    return result
    raise ValueError("Length and breadth must be positive") # Self-Created Error


output = area(10, 20) # calling the function or using the function
print(output)

output_1 = area(20, 30)
print(output_1)