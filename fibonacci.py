def fibonacci_s(n):
    if n <= 1:
        return n
    else:
        return fibonacci_s(n-1) + fibonacci_s(n-2)


def fib_range(term):
    nterms = term

    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print ("Fibonacci Sequence")
        for i in range(nterms):
            print(fibonacci_s(i))

while True:
    print ('Enter a number\n')
    user_term = int(input())
    fib_range(user_term)

