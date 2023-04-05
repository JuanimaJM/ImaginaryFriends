# The script of the game goes in this file.

# The game starts here.
label start:
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
    $ grant_achievement("Achv3")
    "Life: [life]"
    $ life -= 10
    "Get some damage"
    "Life: [life]"
    $ damage()
    "Get some damage"
    "Life: [life]"
    "A{size=+5}A{/size}{size=+10}A{/size}{size=+15}A{/size}{size=+25}A{/size}"
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
