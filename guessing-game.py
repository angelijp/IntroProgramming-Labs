# This program is designed to allow a user to guess an animal using while loop,if-else statements, and variables.
# Angeli Pinol
# Prof. Johnson
# CMPT 120L -113 / Lab Activity #5 
def main():
    
    print("\nWelcome to My Python Guessing Game!\n")
    print ("\nNote*** You may type 'Leave' at anytime to Quit the game.\n")
    animal = "panda" 
    print("I'm thinking of an animal...")
    guess = input("Guess my animal: ").upper().lower()
    _quit = "leave" 
    
    while animal != guess and _quit != guess:
            print("Nope, sorry.")
            guess = input("Guess my animal: ").upper().lower()
            break
    while animal == guess:
            print("Congratulations! You got it!")
            break
    while _quit == guess:
            print("Alright enough guessing... thanks for playing!")
            break
main()

# 2 Issues created in Github
# Created a new variable for the player to quit the game using elif statement.
