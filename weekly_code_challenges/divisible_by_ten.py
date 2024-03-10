num = int(input('Enter a number: '))
def divisible_by_ten(num):
    if(num % 10 ==0):
        print('Divisible by 10 btw')
        return True
    else: return False

divisible_by_ten(num)
