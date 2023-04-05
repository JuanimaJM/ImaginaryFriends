# The script of the game goes in this file.

# The game starts here.
label start:
    scene kitchen
    "Im showing some sprites"
    "Meet Phantom"
    $ meet_friend(Phantom.name)
    show phantom 920
    Phantom "920x920"
    $ update_friends_stats(Phantom.name, 10)
    hide phantom 920
    Someone "..."
    $ meet_friend(Someone.name)
    show phantom 980
    Phantom "980x980"
    $ update_friends_stats(Phantom.name, 40)
    hide phantom 980
    Someone  "..."
    $ update_friends_stats(Someone.name, 75)
    show phantom 960
    Phantom "960x960"
    $ update_friends_stats(Phantom.name, -20)
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
