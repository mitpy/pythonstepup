#keyword arguments

def cart(product,price):
    print('Producnt name ', product)
    print('Product price ', price)


#cart('mobile',25000) valid
#cart(25000,'mobile') valid but get unexpeceted output

#cart(product='Mobile',price=25000) valid
#cart(price=25000,product='Mobile') valid

#cart('Mobile',price=25000) valid

#cart(price=25000,'Mobile') invalid