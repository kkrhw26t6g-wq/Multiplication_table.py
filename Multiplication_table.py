def print_single_table(num):
    """PART A: Prints the multiplication table for a single number from 1 to 12."""
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


def print_multiple_tables(n):
    """PART B: Prints multiplication tables for all numbers from 1 to N."""
    for num in range(1, n + 1):
        print_single_table(num)
        # Print a separator line after each table except the last one
        if num < n:
            print("-------------------------")


def main():
    # --- PART A ---
    try:
        number = int(input("Enter a number: "))
        if number <= 0:
            print("Error: Number must be a positive integer.")
            return
        print_single_table(number)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return

    print("\n" + "=" * 30 + "\n")

    # --- PART B ---
    try:
        n = int(input("Enter a number N for multiple tables: "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        print_multiple_tables(n)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return


if __name__ == "__main__":
    main()