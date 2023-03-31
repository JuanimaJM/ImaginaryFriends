# The script of the game goes in this file.

# The game starts here.
label start:
    show screen stats
    scene kitchen
    "A"
    $ grant_achievement("Title9")
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
