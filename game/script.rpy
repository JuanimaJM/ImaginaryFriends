# The script of the game goes in this file.

# The game starts here.
label start:
    show screen stats
    scene kitchen
    "Im showing some sprites"
    show phantom 920
    Phantom "920x920"
    hide phantom 920
    Someone "..."
    show phantom 980
    Phantom "980x980"
    hide phantom 980
    Someone  "..."
    show phantom 960
    Phantom "960x960"
    $ grant_achievement("Title9")
    "Grant Some Achievement"
    "Life: [life]"
    $ life -= 10
    "Get some damage"
    "Life: [life]"
    $ damage()
    "Get some damage"
    "Life: [life]"
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
