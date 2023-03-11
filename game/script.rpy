# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Child = Character("The Child")


# stats
default sanity = 100
default happiness = 100



# The game starts here.
label start:
    scene kitchen
    "A"
    "B"
    "C"
    "D"
    "E"
    "F"
    "G"
    return
