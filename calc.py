def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed!"
    return a / b

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        operation = input("Enter the number of the operation you want to perform (1, 2, 3, 4): ")

        if operation in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                print("Result:", add(num1, num2))
            elif operation == '2':
                print("Result:", subtract(num1, num2))
            elif operation == '3':
                print("Result:", multiply(num1, num2))
            elif operation == '4':
                print("Result:", divide(num1, num2))

            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
