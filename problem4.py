def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def get_sublist(numbers, start, end):
    return numbers[start:end]

def main():
    # User input for list of integers
    numbers = input("Enter the list of integers: ")
    numbers = list(map(int, numbers.strip("[]").split(",")))

    # Display list of squares of even numbers
    even_squares = get_even_squares(numbers)
    print("List of squares of even numbers:", even_squares)

    # User input for start and end index for slicing
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))

    # Display the sliced sublist
    sublist = get_sublist(numbers, start_index, end_index)
    print("Sublist:", sublist)

if __name__ == "__main__":
    main()
