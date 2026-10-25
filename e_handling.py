"""
Error/Exception Handling

In Generalised Programming, we have two types of problems that can occur: [Not talking about Python]
1. Errors: These are the problems that cannot be predicted and are not handled by the program. - Unsolvable
2. Exceptions: These are the problems that are predicted and are handled by the program. - Solvable

Syntax:
try:
    # Code that may cause an exception
except:
    # Code that will be executed if an exception occurs
"""

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# # Handling the exception [Bad Practice]
# if b == 0:
#     print("Error: Division by zero")
# else:
#     result = a / b # Line that will cause an exception
#     print(result)


# Handling the exception [Good Practice]
try:
    result = a / b # Line that will cause an exception
    print(result)
except Exception as e:
    print("Some error occurred")
    print(e)

print("Program ended")