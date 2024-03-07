price= input('Enter original price of item:')
discount_percent=input('Enter original price of item:')

def calculateDiscount(price, discount_percent):
    price= float(price)
    discount_percent = float(discount_percent)
    if(discount_percent < 20):
        print('Your total is: ',price) 
    else:
         discount = price * (discount_percent/100)
         final_price = price - discount
         print('Your total is: ',final_price) 
calculateDiscount(price, discount_percent)