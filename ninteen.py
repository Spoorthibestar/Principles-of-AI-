# Function to find the nth Fibonacci number using dynamic programming
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Input a number
n = int(input("Enter the position of the Fibonacci number: "))

# Display the nth Fibonacci number
print(f"The {n}th Fibonacci number is {fibonacci(n)}")
