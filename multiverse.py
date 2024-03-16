def print_multiplication_table(number):
    for i in range(1, 21):
        result = number * i
        print(f"{number} * {i} = {result}")

def main():
    try:
        number = int(input("Enter a number: "))
        print(f"\nMultiplication table for {number}:\n")
        print_multiplication_table(number)
    except ValueError:
        print("Please enter a valid number.")


main()