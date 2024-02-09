# Importing the required modules
import random
import string

# Function to generate a random password
def generate_password(length):
    # Defining the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating the password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    # Returning the generated password
    return password

# Main function
def main():
    # Getting the desired length of the password from the user
    length = int(input("Enter the desired length of the password: "))

    # Generating the password
    password = generate_password(length)

    # Printing the generated password
    print("Generated password:", password)

# Running the main function if the script is executed directly
if __name__ == "__main__":
    main()