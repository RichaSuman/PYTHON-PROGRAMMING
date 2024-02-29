#define  a dictionary mapping case value to lamda function

operations = {
    'add': lambda x,y:x+y,
    'sub': lambda x,y:x-y,
    'mul': lambda x,y:x*y,
    'div': lambda x,y:x/y if y > 0 else "Divide by Zero is not allowed",
}

operation = input("Enter operation (add,sub,mul,div): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Execute the lambda function or default if not found

result = operations.get(operation, lambda x,y: "Invalid operation")(num1,num2)
print(f"Result: ",result)
print(f"Result: {result}")