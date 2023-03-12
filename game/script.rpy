# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Child = Character("The Child", color=color_primary)


# stats
default sanity = 100
default happiness = 100



# The game starts here.
label start:
    scene kitchen
    "A"
    Child "eyyy"
    "B"
    Child "bhii"
    "C"
    Child "sii"
    "D"
    Child "....... ..."
    "E"
    "F"
    "G"
    return
