# ==

def single_table(number):
    if number <= 0:
        print("Error: Please enter a positive integer.")
        return

    print(f"Multiplication Table for {number}:")

    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


def multiple_tables(n):
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

        print("---------------------------")


number = int(input("Enter a number: "))
single_table(number)

n = int(input("Enter a number N: "))
multiple_tables(n)