import random
import string
import pyfiglet

# HEADER
name = pyfiglet.figlet_format("Password Generator V1.0", font="graffiti", width=100)
print(name)
print("#" * 100)
print(("#" + "PASSWORD GENERATOR V1.0 by Ashita13".center(98) + "#"))
print("#" * 100)

# FUNCTION 
def password_generator(minlength, nums, specialchars):

    letters = string.ascii_letters      # letter in lower and uppercase
    digits = string.digits              # digit numbers
    spchars = string.punctuation        # special characters
    
    # LETTERS, DIGIT AND SPECIAL LIST
    lds = list(digits) + list(spchars) + list(letters)
    # LETTERS AND DIGITS LIST
    ld = list(letters) + list(digits)
    # LETTERS AND SPECIAL LIST
    ls = list(letters) + list(spchars)

    # GENERATE LETTERS, DIGITS, SPECIAL CHARACTERS IN RANGE OF LENGTH
    output = []
    if nums == "Y" and specialchars == "Y":
        output += random.choices(lds, k = minlength)
    elif nums == "Y" and specialchars == "N":
        output += random.choices(ld, k = minlength)
    elif nums == "N" and specialchars == "Y":
        output += random.choices(ls, k = minlength)
    elif nums == "N" and specialchars == "N":
        output += random.choices(list(letters), k  = minlength)
    
    # JOIN RANDOMED LETTERS DIGITS AND SPECIAL CHARACTERS
    print("Password generated: " + "".join(output))

# USER INPUT
while True:
    # LENGTH OF PASSWORD
    try:
        minlength = int(input("Please enter password length (8 chars - 20 chars): "))
        if 8 <= minlength <= 20:
            break
        else:
            print("INVALID INPUT! Please enter number between 8 to 20")
    except ValueError:
        print("INVALID INPUT! Please enter numbers")
# INCLUDE NUMBERS OR SPECIAL CHARACTERS
nums = input("Do you want to include numbers in your password? (Y/N) ")
while (nums not in ["Y", "N", "y", "n"]):
    print("INVALID INPUT! Please enter Y or N")
    nums = input("Do you want to include numbers in your password? (Y/N) ")
specialchars = input("Do you want to include special characters? (Y/N) ")
while (specialchars not in ["Y", "N", "y", "n"]):
    print("INVALID INPUT! Please enter Y or N")
    specialchars = input("Do you want to include special characters? (Y/N) ")


if __name__ == "__main__":
    # EXECUTE
    password_generator(minlength, nums, specialchars)



