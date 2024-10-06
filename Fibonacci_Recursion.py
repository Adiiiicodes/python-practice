def fibonacci(n):

    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n):

    for i in range(n):
        print(fibonacci(i), end=" ")


terms = int(input("Enter the number of terms: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    print_fibonacci_series(terms)
