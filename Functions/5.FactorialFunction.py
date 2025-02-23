#  Recursive function to calculate the factorial of a number.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(2))
print(factorial(6))

# ---------Output-------- #
# 2
# 720