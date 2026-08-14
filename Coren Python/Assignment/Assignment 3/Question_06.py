cost_price = int(input('Enter cost price :'))
Selling_price = int(input('Enter selling price :'))

if Selling_price > cost_price:
    print('Profit.')
elif cost_price > Selling_price :
    print('Loss.') 
else:
    print('No profit .', ' no loss.')       