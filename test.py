import random

def inputCheck(text):
    var = True
    while var:
        try:
            int_input = int(text)
            if int_input < 0 or int_input > 10:
                raise TypeError
            var = False
        except ValueError:
            text = input("Error, Please pick a number: ")
        except TypeError:
            text = input("Error, Please pick a number between 0,10: ")
    return int_input

number = random.randint(0,10)

int_input = inputCheck(input("Please pick a number: "))

while int_input != number:
    
    if int_input < number:
        print("Guess higher!")
    elif int_input > number:
        print("Guess lower!")
    else:
        print("Oh no! error.")

    int_input = inputCheck(input("Please pick a number: "))

print("congrats!")