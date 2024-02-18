import math

numbers = [1, 2, 3, 4]


def add_all_numbers_from_collection(number_one, number_two, number_three, number_four):
    return number_one + number_two + number_three + number_four


print(add_all_numbers_from_collection(*numbers))

# To run for linting: pycodestyle formatting_error.py
# flake8 formatting_error.py

# To Format: black formatting_error.py
# If you want to alter the line length limit, then you can use the --line-length flag
# black --line-length=79 formatting_error.py

# ruff check formatting_error.py
# To Fix the issue : ruff check --fix formatting_error.py
# Format related fixes: ruff format formatting_error.py
