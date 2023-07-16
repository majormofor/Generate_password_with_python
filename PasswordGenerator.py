import random
import string


print("""WELCOME TO PASSWORD GENERATOR!!!! \n """)
options = input("Do you want to generate a password? (y/n) - y for Yes, n for No: \n").lower() == "y"


while options:
    
    def generate_password(min_length, numbers = True, special_characters = True):
        # a generate password function that generates users password with letters, numbers or/and special characters 
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation


        characters = letters
        if numbers:
            characters += digits

        if special_characters:
            characters += special

        
        password = ""
        meets_standard = False
        has_number = False
        has_special = False

        while not meets_standard or len(password) < min_length:
            new_character = random.choice(characters)
            password += new_character

            if new_character in special:
                has_special = True
            elif new_character in digits:
                has_number = True

            meets_standard = True
            if numbers:
                meets_standard = has_number
            if special_characters:
                meets_standard = meets_standard and has_special

        return password

    min_length = int(input("How long should your password character be? \n"))
    has_special = input("Do you want to have special character? (y/n) \n") == "y"
    has_number = input("Do you want to have number? (y/n) \n") == "y"

    user_password = generate_password(min_length, has_number, has_special)
    print("Your New Password is: ", user_password, "\n")
    options = False
    options = input("Do you want to generate another password? (y/n)\n").lower() == "y"

else:
    print("\nThank you and Have a nice day")





