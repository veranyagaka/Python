base = int(input('Enter the base:'))
exponent = int(input('Enter the exponent:'))

def largePower(base, exponent):
    answer = base ** exponent
    print(answer)
    if(answer >5000):
        return True
    
    else:
        return False
largePower(base, exponent)