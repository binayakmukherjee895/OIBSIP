import random
import string

def generate_pwd(length,use_upper,use_lower,use_digit,use_symbol):
    password=[]
    character_pool= ""

    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
        character_pool+=string.ascii_uppercase
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
        character_pool+=string.ascii_lowercase
    if use_digit:
        password.append(random.choice(string.digits))
        character_pool+=string.digits
    if use_symbol:
        password.append(random.choice(string.punctuation))
        character_pool+=string.punctuation

    while len(password)<length:
        password.append(random.choice(character_pool))

    random.shuffle(password)
    return "".join(password)

while True:
    print("\n========== RANDOM PASSWORD GENERATOR ==========")
    try:
        length=int(input("Enter password length ( Minimum 8 characters !): "))

        if length<8:
            print("Password length must be atleast 8")
            continue

        upper=input("Include uppercase characters (Y/N)? ").lower()=="y"
        lower=input("Include lowercase characters (Y/N)? ").lower()=="y"
        digit=input("Include digits (Y/N)? ").lower()=="y"
        symbol=input("Include symbols (Y/N)? ").lower()=="y"

        selected_types=upper+lower+digit+symbol

        if selected_types<2:
            print("Select atleast two character types")
            continue

        password=generate_pwd(length,upper,lower,digit,symbol)
        print("\nGenerated Password: ",password)

    except ValueError:
        print("Invalid input. Please enter a valid number !")
    choice= input("\nGenerate another password (Y/N): ").lower()

    if choice!="y":
        print("\nThank you for using the Password Generator !")
        break








