## https://realpython.com/list-comprehension-python/?utm_source=notification_summary&utm_medium=email&utm_campaign=2024-01-23#transforming-lists-in-python
## Example 1
square = []

for i in range(10):
    square.append(i*i)

print(f'Square of numbers are : {square}')

## Using list comprehension
square = [i*i for i in range(10)]
print(f'Square of numbers are : {square}')

## Example 2
sentence = "the rocket came back from mars"
vowel = [c for c in sentence if c in 'aeiou']
print(f'Vowel in sentence is : {vowel}')

## Example 3
sentence = ("The rocket, who was named Ted, came back"\
            "from Mars because he missed his friends." )

def is_consonant(letter):
    vowels='aeiou'
    return  letter.isalpha() and letter.lower() not in vowels

output1=[char for char in sentence if is_consonant(char)]
print(f'Output1 is : {output1}')

## Example 4 (If we need to change the a value rather than filtering out the use if condition before for instead of after)
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
select_price = [price if price > 0 else 0 for price in original_prices]
print(f' Selected prices are: {select_price}')

def get_price(price):
    return price if price > 0 else 0

select_price = [get_price(price) for price in original_prices]
print(f' Selected prices are: {select_price}')

select_price = [price for price in original_prices if get_price(price)] ## using this technic we cannot update the price
print(f' Selected prices are: {select_price}')
## Example 5
## Use Walrus operator(:=)
## Walrus operator allows you to run an expression while simultaneously assigning the output value to a variable
import random
def get_weather_data():
    return random.randrange(90,110)

output3 = [temp for _ in range(40) if (temp := get_weather_data()) >= 100]
print(f'Output3 is : {output3}')

## Example 6 
## Set Comprehension (to avoid duplicate values) 
## Use {} instead of []
quote = "life, uh, finds a way"
output2 = {char for char in quote if char in 'aeiou'}
print(f'Output2 is : {output2}')

## Example 7
## Dict Comprehension
output_dict = {number:number*number for number in range(10)}
print(f'Output_dict is {output_dict}')

## Example 8
## Nested list Comprehension
cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]
#cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]
City_list = {city: [0 for _ in range(7)] for city in cities}
print(f'City is : {City_list}')

## Example 9
## Nested lists are a common way to create matrices
Matrix = [[number for number in range(7)] for _ in range(4)]
print(f'Matrix is : {Matrix}')

## Example 10
## To flatten a Matrix
Flat_matrix = [num for row in Matrix for num in row]
print(f'Flat_Matrix is : {Flat_matrix}')

