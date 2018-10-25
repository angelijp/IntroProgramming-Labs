# This program is designed to allow a user to guess an animal using while loop,if-else statements, and variables.
# Angeli Pinol
# Prof. Johnson
# CMPT 120L -113 / Lab Activity #5 
def main():
    animal = "panda"
    print("\nWelcome to My Python Guessing Game!\n")
    print ("\nNote*** You may type 'quit' at anytime to Quit the game.")
    print("I'm thinking of an animal...")
    guess = input("Guess my animal: ").upper().lower()
    
    while animal == guess:
        print("Congratulations! You got it!")
        corr_guess = input("Do you like pandas? Y or N: ").upper().lower()
        if corr_guess == "y":
            print("They are so cute!")
        elif corr_guess == "n":
            print("Aww! That's too bad!")
        break
    
    while animal != guess:
        print("Nope, sorry")
        gu = input("Give Up? (Y/N): ").upper().lower()
        while gu == "y":
            q = input("Type any 'q' word to Quit: ").upper().lower()
            while "q" in q[0]:
                print("Alright enough guessing... Thanks for playing!")
                break
            break
        break
    
    while animal != guess:
        print("Nope, sorry")
        gu = input("Give Up? (Y/N): ").upper().lower()
        while gu == "n":
            guess = input("Guess my animal: ").upper().lower()
            while animal == guess:
                print("Congratulations! You got it!")
                corr_guess = input("Do you like pandas? Y or N: ").upper().lower()
                if corr_guess == "y":
                    print("They are so cute!")
                elif corr_guess == "n":
                    print("Aww! That's too bad!")
                    break
                break
            break
main()

# 2 Issues created in Github
# Created a new variable for the player to quit the game using elif statement.
