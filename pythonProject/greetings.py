# global scope
#    def greeting():
#        print("Hello", name)

# main program
#    name = input("Enter your name:\n")

#    greeting()

# Local scope
def greeting(name):
    print("Hello", name)

name1 = input("Enter your name:\n")
greeting(name1)
name2 = input("Enter another name:\n")
greeting(name2)