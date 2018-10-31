# CMPT 120 - Lab #6
# Angeli Pinol
# 25 08 2018
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
    cmd_list = ["add","mult","sub","div","quit"]
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
        
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    while True:
        cmd = input("What computation do you want to perform?: ").lower()
        cmd_list = ["add","mult","sub","div","quit"]
        if cmd == "quit":
                showOutro()
                break
        
        while cmd in cmd_list:         
            if cmd == "add":
                result = num1 + num2
                print("The result is " + str(result) + ".\n")
                break
            elif cmd == "sub":
                result = num1 + -num2
                print("The result is " + str(result) + ".\n")
                break
            elif cmd == "mult":
                result = num1 * num2
                print("The result is " + str(result) + ".\n")
                break
            elif cmd == "div":
                result = num1 // num2
                print("The result is " + str(result) + ".\n")
                break    
        else:
            print(cmd, "is not a valid command.")
def main():
    showIntro()
    doLoop()
    showOutro
main()
         
