from components import vars
from emoji import emojize


def total(value):
    # do some logic to see which character you selected

    if value == 2:
        vars.character = vars.characters[0]
        print("It's " + vars.character)

    elif value == 3:
        vars.character = vars.characters[1]
        print("It's " + vars.character)
    
    elif value == 4:
        vars.character = vars.characters[2]
        print("It's " + vars.character)
    
    elif value == 5:
        vars.character = vars.characters[3]
        print("It's " + vars.character)
    
    elif value == 6:
        vars.character = vars.characters[4]
        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

    