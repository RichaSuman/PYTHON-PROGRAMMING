def square(x):
    return x**2

number = [1,2,3,4,5]
squared_numbers = map(square, number)
print(squared_numbers)
print(list(squared_numbers))

## Example 2
prices=[1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08

def get_price_after_tax(price):
    return price*(1+TAX_RATE)

final_price = map(get_price_after_tax,prices)
print(list(final_price))

##Using List comprehension
final_price = [get_price_after_tax(price) for price in prices]
print(final_price)

