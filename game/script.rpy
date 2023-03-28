# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Child = Character("The Child", color=sugar_plum)


# stats
default sanity = 100
default happiness = 100


# The game starts here.
label start:
    scene kitchen
    "A"
    "[life]"
    $ life -= 10
    "[life]"
    $ damage()
    "[life]"
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
