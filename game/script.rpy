# The script of the game goes in this file.

# The game starts here.
label start:
    show screen script_keymap
    stop music fadeout 1.0
    scene kitchen
    jump testing

label asking_name:
    $ player_name = renpy.input("What is your name?", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if not player_name == "":
        jump end
    Cloud "You haven't given me your name yet."
    Cloud "Please tell me your name."
    "Cloud smiled warmly at me."
    $ player_name = renpy.input("What is your name?", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if not player_name == "":
        jump end
    Cloud "Don't tell me you don't have a name?"
    Cloud "You must have one. Even a nickname."
    Cloud "What is your name?"
    "Cloud asked me once again, still having a smile on his face."
    $ player_name = renpy.input("What is your name?", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if not player_name == "":
        jump end
    Cloud "Ha!"
    "Cloud exclaimed loudly. He seems to be irritated."
    Cloud "My patience is running out."
    Cloud "Are you stupid!?"
    Cloud "It's either you are being stubborn or you are really stupid since you don't even know your own name."
    Cloud "What am I to do with you?"
    "Cloud sighed."
    Cloud "I'll give you once last chance."
    Cloud "Just tell me your name kid, please."
    $ player_name = renpy.input("What is your name?", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if not player_name == "":
        jump end
    else:
        $ player_name = "Stupid"
    $ grant_achievement("Achv9")
    Cloud "Fine! I'll name you myself!"
    "Cloud shouted."
    Cloud "From now on, your name is Stupid."
    Cloud "Hi Stupid!"
    Cloud "But since you made me quite upset-"
    Cloud "No."
    Cloud "I must say, I'm quite disappointed in you."
    Cloud "You must leave this game!"
    Cloud "Come back when you are willing to give me your name."
    Cloud "Thank you and good bye. Stupid."
    "Cloud smiled at me, but I feel like he isn't really happy."
    "I think he's angry at me."
    $ renpy.quit()

label testing:
    "1"
    "2"
    "3"
    "Before we start, I would like you to input something"
    $ player_name = renpy.input("What is your name?", random_name(), length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    $ player_name = random_name() if player_name == "" else player_name
    "Oohh. So your name is [player_name]"
    "I will show some choices for testing"
    call testing_menu
    jump end

label testing_menu:
    menu:
        "Change player name":
            $ player_name = renpy.input("Input your new name.", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            $ player_name = random_name() if player_name == "" else player_name
            "Your new name is [player_name]"
        "Get random achievement":
            $ randomly_grant_achievement()
            "Check your achievements I added some"
        "Show sprite size":
            show phantom 960
            "The sprite size is 960x960"
        "Write random diary":
            $ randomly_write_diary()
            "Check your diary I added some"
        "Meet some friend":
            $ meet_friend("Phantom")
            show phantom 960
            Phantom "Hi, nice to meet you."
            hide phantom
            "Now that you meet some friend, it will now be shown in your stats window."
        "Randomly decrease the value sanity and happiness" if  1 < sanity <= 100 and 1 < happiness <= 100:
            $ random_sanity = random.randint(1, sanity - 1)
            $ random_happiness = random.randint(1, happiness - 1)
            $ sanity -= random_sanity
            $ happiness -= random_happiness
            $ random_sanity = abs(random_sanity)
            $ random_happiness = abs(random_happiness)
            "Check your stats window. I decrease your sanity by [random_sanity] and happiness by [random_happiness]"
        "Randomly increase the value sanity and happiness" if  1 <= sanity <= 99 and 1 <= happiness <= 99:
            $ random_sanity = random.randint(1, 100 - sanity)
            $ random_happiness = random.randint(1, 100 - happiness)
            $ sanity += random_sanity
            $ happiness += random_happiness
            $ random_sanity = abs(random_sanity)
            $ random_happiness = abs(random_happiness)
            "Check your stats window. I increase your sanity by [random_sanity] and happiness by [random_happiness]"
    jump show_test_choices

label show_test_choices:
    "Do you want to test something again?"
    menu:
        "Yes":
            jump testing_menu
        "No":
            return
    

label random_test:
    $ output = renpy.variant("small")
    "Is Small Variant?: [output]"
    $ output = renpy.variant("pc")
    "Is PC Variant?: [output]"
    $ output = renpy.variant("mobile")
    "Is Mobile Variant?: [output]"
    "Im showing some sprites"
    "Ahmmm before that, what is your name?"
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

label end:
    "3"
    "2"
    "1"
    "The End!"
    return
