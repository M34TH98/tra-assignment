def print_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1 ' * i)

def print_palindromic_triangle(n):
    for i in range(1, n + 1):
        # Create leading spaces
        print(' ' * (n - i) + '1 ' * i)

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            n = int(input("Enter the number of lines: "))
            print_right_angle_triangle(n)
        elif choice == '2':
            n = int(input("Enter the number of lines: "))
            print_palindromic_triangle(n)
        elif choice == '3':
            print("Choose 1 to display a right-angle triangle of ones.")
            print("Choose 2 to display a palindromic triangle.")
            print("Choose 4 to exit the program.")
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose from 1-4.")

if __name__ == "__main__":
    main()
