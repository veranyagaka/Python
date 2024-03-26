try:
    number =int(input('Enter a number greater than 0'))
    if(number <1):
     raise ValueError('Number must be greater than zero') 
except ValueError as ve:
    print(ve)
#specific exceptions
try:
    numerator =int(input('Enter a numerator'))
    denominator =int(input('Enter a denominator'))
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print('Valid denominator')
else:
    print('No exception occurred')
finally:
    print('Is always printed!!!')
#multiple exceptions
    
#raising exceptions
raise ZeroDivisionError('The denominator cannot be zero')