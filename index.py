invoice = []
insertProduct = 's'
amount = 0 

while insertProduct != 'n':
    product = input('Insert the product: ')
    price = float(input('Enter the price of the product: '))
    invoice.append([product, price])

    amount += price
    insertProduct = input('Do you want to add any more products? S or N ').lower()

for i in invoice:
    print(i[0], '-','$',i[1])

print('Amount payable:', '$',amount)