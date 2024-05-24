invoice = []
insertProduct = 's'
amount = 0 
valid_price = False

while insertProduct != 'n':
    product = input('Insert the product: ')

    while valid_price == False:
        price = input('Enter the price of the product: ')
        try:
            price = float(price)
            valid_price = True
        except: 
            print('Format of price invalid. Use only numbers with .')

    invoice.append([product, price])

    amount += price
    valid_price = False
    insertProduct = input('Do you want to add any more products? S or N ').lower()

for i in invoice:
    print(i[0], '-','$',i[1])

print('Amount payable:', '$',amount)