def fibo(n):
    sequence =[]
    a,b =0,1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a+b
    return sequence
numbers = int(input('Enter the number of terms: '))
sequence =fibo(numbers)
print('Fibonacci sequence', sequence)