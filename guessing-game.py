# This program is designed to allow a user to guess an animal using while loop,if-else statements, and variables.
# Angeli Pinol
# Prof. Johnson
# CMPT 120L -113 / Lab Activity #5 
def main():
    animal = "panda"
    print("\nWelcome to the Python Guessing Game!\n")
    print("I'm thinking of an animal...")
    guess = input("Guess my animal: ")
    while animal != guess:
        print("Dang! Try again!")
        guess = input("Guess my animal: ")
    if animal == guess:
        print("Congratulations, you got it right!")
    else:
        print("Dang! Try again!")
        guess = input("Guess my animal: ")
        
main()

