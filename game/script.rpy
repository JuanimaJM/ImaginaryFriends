# The script of the game goes in this file.

# The game starts here.
label start:
    stop music fadeout 1.0
    scene kitchen
    $ output = renpy.variant("small")
    "Is Small Variant?: [output]"
    $ output = renpy.variant("pc")
    "Is PC Variant?: [output]"
    $ output = renpy.variant("mobile")
    "Is Mobile Variant?: [output]"
    "Im showing some sprites"
    "Ahmmm before that, what is your name?"
    $ player_name = renpy.input("What is your name?", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    "Meet Phantom [Child]"
    $ meet_friend(Phantom.name)
    $ write_diary("Ghost")
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
    $ grant_achievement("Achv8")
    $ life = 100
    "Life: [life]"
    $ life -= 10
    "Get some damage"
    "Life: [life]"
    $ damage()
    "Get some damage"
    "Life: [life]"
    "A{size=+5}A{/size}{size=+10}A{/size}{size=+15}A{/size}{size=+25}A{/size}"
    Child "eyyy"
    $ write_diary("Apple")
    "B"
    Child "bhii"
    "C"
    Child "sii"
    "D"
    Child "....... ..."
    "E"
    "F"
    "G"
    $ write_diary("Tree")
    return
