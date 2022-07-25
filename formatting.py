product = input("what item did you buy?")
price = float(input("how much did you pay?"))
qty = int(input("how many did you buy?"))

print('you purchased' , product , qty, 'for', price)

#formatting string
print ( f'you purchased {product} {qty} for {price}')