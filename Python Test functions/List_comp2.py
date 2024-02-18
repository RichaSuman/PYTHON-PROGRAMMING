## A list comprehension in Python works by loading the entire output list into memory. For small or even medium-sized lists, this is generally fine.
## To create a list with one billion integers, which consumes more memory and the m/c slows down or even crashes
## it’s often helpful to use a generator instead of a list comprehension in Python.
## A generator doesn’t create a single, large data structure in memory, but instead returns an iterable. 
## Your code can ask for the next value from the iterable as many times as necessary or until you’ve reached the end of your sequence, 
## while only storing a single value at a time.

## Example 1 (Using Generator)
sum(number * number for number in range(1_000_000_000))

## Example 2 (Using Map)
sum(map(lambda number: number * number, range(1_000_000_000)))

## Example 3 (Using Timeit to compare map, list, comprehension)
import random
import timeit
TAX_RATE = 0.08
PRICES = [random.randrange(100) for _ in range(100_000)]

def get_price(price):
    return  price *(1+ TAX_RATE)

def get_price_with_map():
    return list(map(get_price,PRICES))

def get_price_with_comprehension():
    return [get_price(price) for price in PRICES]

def get_price_with_generator():
    generator = ((g, get_price(g)) for g in PRICES)
    return lambda: list(generator)

def get_price_with_loop():
    prices = []
    for price in PRICES:
        prices.append(get_price(price))
    return prices
    
print("Time for Loop:\n", end="")
print(timeit.timeit(get_price_with_loop, globals=globals(), number=100))

print("Time for List Comprehension:\n", end="")
print(timeit.timeit(get_price_with_comprehension, globals=globals(), number=100))

print("\nTime for Map Function:\n", end="")
print(timeit.timeit(get_price_with_map, globals=globals(), number=100))

print("\nTime for Generator Function:\n", end="")
print(timeit.timeit(get_price_with_generator, number=100))

# The generator function is faster than the other two methods because it generates one item at a time and 
# does not need to store all items in memory before beginning to process them. This makes generators
# The results show that using the generator function is faster than both the other methods. 
# This makes sense because generators don't need to store all the values in memory at once;