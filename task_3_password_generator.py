import random
import string

# Function to generate a random password
def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password using random.choices method
    password = ''.join(random.choices(characters, k=length))
    return password

# Main function
def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the program execution
