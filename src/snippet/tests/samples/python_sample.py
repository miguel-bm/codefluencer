# Define a function that calculates the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Call the factorial function and print the result
result = factorial(num)
print("The factorial of", num, "is", result)
