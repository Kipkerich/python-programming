def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (price- (price * (discount_percent)/100))
    return price


print(calculate_discount(400, 50))



def calculate_discount():
    price = input("Value of price:")
    
    discount_percent = input("Discount percent:")
   
    
    if discount_percent >= 20:
        return (price- (price * (discount_percent)/100))
    return price
print("Price of the product is", int(calculate_discount()))