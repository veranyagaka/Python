num1 = int(input('Enter number: '))
def fac(num1):
    if(num1 ==0 | num1 ==0):
        return 1
    else:
        return num1 * fac(num1-1)
    
answer = fac(num1)
print(f'Factorial of: {num1} is: {answer}')