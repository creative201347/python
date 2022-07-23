def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))


num = int(input("Enter any number "))
print("The factorial of", num, "is", fact(num))


def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m-1) + fib(m-2)


num = int(input("Enter any number "))
print("The fibonacci of", num, "is", fib(num))
