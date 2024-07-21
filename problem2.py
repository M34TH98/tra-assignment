def decimal_to_binary(decimal_number):
    # Ensure the input is a positive integer
    if decimal_number < 0:
        raise ValueError("The input must be a positive integer.")
    
    # Initialize the binary string
    binary_string = ""
    
    # Handle the special case where the number is 0
    if decimal_number == 0:
        return "0"
    
    # Perform the conversion
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_string = str(remainder) + binary_string
        decimal_number = decimal_number // 2
    
    return binary_string

# Example usage
number = int(input("Enter a positive decimal number: "))
binary_representation = decimal_to_binary(number)
print(f"The binary equivalent of {number} is {binary_representation}.")
