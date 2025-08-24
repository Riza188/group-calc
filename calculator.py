def add(a, b):
  return a + b
  
def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

else:
return "Error! Division by Zero. "
def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
