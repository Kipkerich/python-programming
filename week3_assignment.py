def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (price- (price * (discount_percent)/100))
    return price


print(calculate_discount(400, 50))



# def calculate_discount():
#     price = input("Value of price:")
#     price = calculate_discount()
#     discount_percent = input("Discount percent:")
#     discount_percent = calculate_discount()
    
#     if discount_percent >= 20:
#         return (price- (price * (discount_percent)/100))
#     return price


# price = calculate_discount()

# discount = calculate_discount()

# print("{price}, {discount}")