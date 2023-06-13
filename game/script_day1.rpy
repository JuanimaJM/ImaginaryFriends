label day1:
    # Effects as if opening eyes
    Child "Huh?"
    Child "That’s weird."
    Child "How did I get here?"
    Child "And why is it so dark?"
    "I seem to have forgotten what I was doing a while ago."
    "I remember closing my eyes as if I was just blinking for a moment…"
    "Then, when I opened my eyes, I was standing in this darkness."
    Child "H-Hello?"
    "I said cautiously but I was met with silence."
    "W-what should I do?"

    menu:
        "Try yelling":
            call day1_menu1_choice1
        "Search the area":
            call day1_menu1_choice2
        "Stand Still":
            call day1_menu1_choice3
    
    "As time pass by, the action I chose led me nowhere."
    "I’ve decided to just walk straight ahead."
    # Sound: Heavy breathing of a child
    "I’ve been walking for so long that I feel like a day has passed."
    "I’m so tired."
    "Then I suddenly realized something."
    "It was really dark. And cold."
    "It was also quiet."
    "A-and I’m alone…"
    "I’m used to being alone though. "
    "To living a quiet life."
    "But that quiet life is quite lonely, I guess. "
    "Really lonely and sad."
    "I don’t know why but, my body started to feel cold."
    "And I started to shiver in this dark and cold place."
    Child "Really…"
    "Why is my life so lonely and sad…?"
    # Effects as if crying; Blurry View; Until Stop#
    "Suddenly I couldn’t see."
    "There were already tears coming out of my eyes."
    "I’m used to being left behind, I’m used to loneliness, I’m used to having a quiet life, but somehow, in this dark and cold place where I can’t see."
    "I can’t help but let all of these feelings out."
    # Sound: Crying and screaming of a child; Androgenous Voice# 
    "I filled the silence with my loud crying and screams…"
    "That’s weird."
    "As I cried alone in this darkness, I feel like I’m not alone."
    "In fact, I feel as if I’m with someone right now."
    "I feel comfortable."
    "After a few more minutes, I manage to calm myself and stopped crying."
    # End of Blurry View# 
    # Sound: Laughing# 
    "Suddenly, I heard someone laughing."
    "As if it saw something amusing."
    "The laugh was quite scary, the comfort I felt earlier suddenly disappeared."
    "I need to leave."
    "I continued walking."
    "Hoping that I won’t hear that laugh anymore."
    # Black Background with Dim (Little) Light#
    "As I walked more in this darkness, I was greeted by a dim light from a distance."
    Child "L-light…there’s light!"
    "I exclaimed excitedly, maybe this endless journey will finally come to an end."
    "I ran so fast, not looking back and not even stopping to breathe."
    "Just so I could see something else aside from this darkness."
    # Effect as if blinded by light# 
    "And as I go nearer and nearer to the dim light, it became brighter and brighter."
    # Background: Circus/Fun House/Carnival#
    scene circus
    pause
    # Enjoy view muna ahahah bago mag next dialog# 
    "And there, I saw a huge colorful tent."
    # Sound: Circus Music, fun and lively# 
    "And then music started to fill up the place. "
    "A very fun and lively music."
    "I can’t help but get excited."
    Child "T-this is-"
    "???" "My home."
    "I heard someone talk and laugh."
    Child "Huh? Who’s there?"
    "I look around me but don’t see anyone."
    # *Smiling Talking Face* 
    show cloud smiling
    "???" "Looking for me~?"
    # *Closed-Eye Smiling Face*
    "A very tall man appeared in front of me."
    "He wore a colorful suit. He looks like-"
    Child "A clown?"
    # *Surprised Talking Face*
    "???" "How did you know?"
    # *Surprised Face*
    Child "I-it’s pretty obvious because of your look and face."
    # *Smiling Talking Face* 
    "???" "How clever~"
    # *Closed-Eye Smiling Face*
    "He smiled warmly at me."
    "This is the first time someone ever smiled at me."
    "I can’t help but feel happy."
    # *Smiling Talking Face* 
    "???" "Don’t you have any questions for me?"
    # *Closed-Eye Smiling Face*
    Child "Questions?"
    # *Surprised Talking Face* 
    "???" "That’s weird."
    "???" "You’re not curious?"
    "???" "But you’re a child."
    # *Surprised Face*
    Child "W-what do you mean?"
    # *Smiling Talking Face* 
    "???" "Hmmm~ Never mind."
    "???" "Anyways~ "
    "???" "I am indeed a clown, and I am the owner of this fun and amazing place~"
    "???" "I am Cloud."
    Cloud "Cloud the Clown."
    Cloud "How about you?"
    # *Closed-Eye Smiling Face*
    "The man introduced himself with a smile."
    "So, his name is Cloud."
    Child "C-cloud."
    # *Smiling Talking Face* 
    Cloud "That’s right! That’s me~"
    Cloud "So? Tell me, what’s your name?"
    # *Closed-Eye Smiling Face*

    call cloud_asking_name
    $ Child.name = player_name

    # *Overly Excited Face* 
    Cloud "Oh! So that’s your name."
    # *Smiling Talking Face*
    Cloud "Nice to meet you [Child.name]"
    # *Closed-Eye Smiling Face*
    Child "N-nice to meet you too."
    # *Smiling Talking Face* 
    Cloud "Do you want to be my friend? "
    # *Closed-Eye Smiling Face*
    Child "O-oh! F-friend? Me?"
    # *Surprised Talking Face* 
    Cloud "Why are you so surprised? "
    # *Surprised Face*
    Child "I-I’ve never had a friend."
    Child "Let alone have someone to talk to aside from my parents…my mother."
    "At the thought of my mother, I can’t help but frown."
    "S-she never really like me."
    "Especially my father."
    # *Smiling Talking Face* 
    Cloud "Then~"
    Cloud "I’m glad to be your very first friend. "
    # *Closed-Eye Smiling Face*
    "My very first friend…"
    Child "T-thank you."
    "I said quietly."
    "I felt shy."
    "But I’m really happy."
    # *Happiness = +10; Sanity = +10; Message: Your stats have change. *
    $ update_player_stats(10, 10)
    # *Smiling Talking Face*
    Cloud "Hmmm~ But surely, I won’t be your only friend, right? "
    # *Closed-Eye Smiling Face*
    "Cloud asked me. He seems eager to hear my reply."
    Child "I’m really grateful. Thank you for being my friend."
    Child "And i-if it’s possible, I want to have more friends."
    Child "B-but it’s not like I don’t want to be your friend, I really want to-"
    "Cloud suddenly laughed loudly."
    # *Smiling Talking Face* 
    Cloud "You’re really funny."
    Cloud "Why are you so nervous? "
    Cloud "You won’t be getting any friends if you’re like that. "
    # *Closed-Eye Smiling Face*
    Child "I won’t?"
    # *Smiling Talking Face* 
    Cloud "Yes. You won’t."
    Cloud "If you want to be friends with someone, you should greet them with a smile. "
    Cloud "If you act all nervous and shy, they might feel uncomfortable and will leave you."
    Cloud "But~ Since you’re my friend. "
    Cloud "Do you want me to sing to you my “I want to be your friend” song? "
    # *Closed-Eye Smiling Face*
    Child "“I want to be your friend” song?"
    # *Smiling Talking Face* 
    Cloud "A song I made. "
    Cloud "I sing it when I want to be friends with someone. "
    Cloud "I should have sung it first earlier when I talked to you. "
    Cloud "So~ Do you want to hear it? "
    # *Closed-Eye Smiling Face*

    menu:
        "No":
            call day1_menu2_choice1
        "Yes":
            call day1_menu2_choice2
    
    Child "What if they don’t want to be my friend?"
    # *Smiling Talking Face* 
    Cloud "Nonsense! All you need to do is smile~"
    Cloud "Give them your brightest and most sincere smile."
    Cloud "And nothing can go wrong~"
    Cloud "Be confident, that’s my little advice to you my little friend. "
    # *Closed-Eye Smiling Face*
    Child "Okay. I’ll do my best."
    Child "Thank you Cloud."
    # *Smiling Talking Face* 
    Cloud "You’re welcome."
    Cloud "I hope you’ll be able to have many friends."
    # *Sinister Talking Face* 
    Cloud "I want you to be happy."
    Cloud "Not too happy though. "
    # *Sinister Smile Face*
    Child "W-what do you mean? "
    # *Sinister Talking Face* 
    Cloud "It’s time to wake up."
    # *Effects as if opening eyes*
    hide cloud
    scene black
    Child "Huh?"
    "I feel like I had a weird dream."
    "I can’t remember it though."
    "???" "{size=+8}[Child.name]!!{/size}"
    "I heard someone yelling my name."
    "When I realized who it was, my body started trembling."
    "I was terrified."
    # *Happiness = -5; Sanity = -5; Message: Your stats have change. *
    $ update_player_stats(-5, -5)
    Mother "This brat! Are you still sleeping!?"
    "Mother’s yelling stopped."
    "She’s really mad. She’s mad at me again."
    Child "B-but where am I?"
    # *Enjoy view muna ahahah bago mag next dialog*
    "I was inside a car. "
    "T-that’s right. I remember now."
    "I’m at our new house."
    # *Angry Shouting Face* 
    Mother "{size=+4}Ha! So, you were awake?{/size}{size=+8}You were ignoring me!?{/size}"
    # *Angry Face*
    Child "A-ah!"
    "Mother suddenly appeared."
    Child "N-no, I just woke up m-mother."
    "I said, my body slightly trembling."
    # *Annoyed Talking Face* 
    Mother "You even dare lie to me! "
    # *Annoyed Face*
    Child "N-no, I wouldn’t dare."
    "Mother sighed."
    # *Annoyed Talking Face* 
    Mother "Just hurry up! Help with the luggage."
    Mother "Your father isn’t here again, and the furniture movers will be running late."
    Mother "It’s so annoying! "
    Mother "You better stop being lazy, I’ll meet you inside the house. "
    # *Annoyed Face*
    Child "Y-yes."
    # *Annoyed Talking Face* 
    Mother "Hmph! "
    "Mother left."
    "I can’t help but sigh."
    "I better hurry up. I don’t want to further ruin mother’s mood."
    # *Background: Blue Sky*
    scene sky
    "As I stepped out the car, I can’t help but look at the sky."
    "There were so many clouds."
    Child "Clouds…"
    Child "Ah!"
    "I remember my dream. I remember Cloud, my very first friend."
    Mother "{size=+8}[Child.name]! What’s taking you so long!?{/size}"
    "Mother yelled again. Angrier and more impatient than before."
    Child "I-I’m on my way!"
    "I need to hurry and meet mother inside the house."
    # *Background: Hallway 1; No Hover*
    scene entrancehall
    # *Annoyed Talking Face* 
    Mother "Finally! You’re here."
    # *Annoyed Face*
    Child "I’m sorry for being late."
    # *Mocking Talking Face* 
    Mother "Ha! At least you know your place. "
    # *Serious Talking Face* 
    Mother "You better listen carefully."
    Mother "I’ll be going out for a while, I’ll be back at night. "
    # *Serious Face*
    Child "Where are you going?"
    # *Serious Talking Face* 
    Mother "It’s not something you should be concerned about."
    Mother "Now stop asking and just listen while I’m in a good mood."
    Mother "See that luggage over there? "
    # *Serious Face*
    "I looked to where my mother is pointing."
    Child "Yes."
    # *Serious Talking Face* 
    Mother "Good. "
    Mother "That luggage is yours. It has your belongings of course."
    Mother "Just put it in your room."
    Mother "On the second floor. In the middle room on the right."
    Mother "Don’t wander off."
    Mother "Do you understand? "
    # *Serious Face*
    Child "Yes."
    # *Mocking Talking Face* 
    Mother "Ha! You’re pretty obedient today."
    Mother "I wonder how long it will last. "
    # *Serious Talking Face* 
    Mother "I’ll be leaving now, just don’t cause any troubles when the furniture movers come. "
    "Mother left, leaving me alone in this big house."
    "I better follow her orders."
    "I took the luggage. It was kind of heavy."
    Child "I need to go upstairs."
    # *Background: Hallway 1; May Hover*
    call screen entranceHall
    "[room]"
    return


label day1_menu1_choice1:
    "I should try yelling. "
    "Maybe someone would hear me."
    "Someone good, I hope."
    Child "H-H{size=+8}ello! Is anybody there?{/size}"
    Child "{size=+8}Can someone hear me?{/size}"
    "No one answered."
    Child "{size=+12}Is there anybody out there? Anyone?{/size}"
    Child "{size=+12}Please yell back!{/size}"
    "I yelled, louder."
    "No one answered, again."
    return

label day1_menu1_choice2:
    "If I search the area, will I really be able to find something?"
    Child "No."
    Child "Stop thinking negatively."
    "I said to myself."
    "Even if it’s really dark, I should still try."
    "I hope I’ll be able to find something."
    "Anything at all. "
    "Anything that can help me."
    "A flashlight, I hope."
    "Or any light."
    return

label day1_menu1_choice3:
    "I-I’m scared…"
    "It’s really dark. Really, really dark."
    "If I yell, I might attract something…"
    "Something not good."
    "If I try to search the area…"
    "I might bump into something."
    "Or maybe fall into a hole I couldn’t see."
    "I better stand still."
    "That’s the safest thing to do."
    "I hope."
    return

label day1_menu2_choice1:
    # *Sad Talking Face* 
    Cloud "No?"
    Cloud "Are you sure you don’t want to hear it?"
    # *Sad Face*
    Child "Yes, I don’t want to hear it. I’m sorry."
    # *Disappointed Talking Face* 
    Cloud "Don’t say sorry."
    Cloud "But it’s quite disappointing. "
    # *Smiling Talking Face* 
    Cloud "But I guess singing a song isn’t the only way to befriend someone. "
    Cloud "Just be friendly. "
    # *Closed-Eye Smiling Face*
    return

label day1_menu2_choice2:
    Child "Can I hear it?"
    # *Overly Excited Face* 
    Cloud "Of course~ "
    # *Overly Excited Talking Face*
    "Cloud smiled and said happily. He looks overjoy."
    # *Smiling Talking Face* 
    Cloud "{i}Be Friends, Be Friends, can we be friends?{/i}"
    Cloud "{i}Who sings and dance all day, all night,{/i}"
    Cloud "{i}We talk, we smile, we laugh, we cry,{/i}"
    Cloud "{i}We share all feelings known and not,{/i}"
    Cloud "{i}We’re here for each and every one,{/i}"
    Cloud "{i}Make sure no one is left behind.{/i}"
    Cloud "{i}So, here’s my hand I reach to you,{/i}"
    Cloud "{i}Reach out to it and let’s be friends.{/i}"
    # *Closed-Eye Smiling Face*
    "Cloud reached out his hand."
    "I think he wants me to hold his hand."
    "I held Cloud’s hand, and he started singing again."
    # *Smiling Talking Face* 
    Cloud "{i}You’ve held my hand so now we’re friends,{/i}"
    Cloud "{i}We’re Friends, We’re Friends, now we are friends.{/i}"
    Cloud "Easy right? "
    # *Closed-Eye Smiling Face*

    return

label cloud_asking_name:
    call screen ask_name("What is your name?")
    $ player_name = _return
    $ Child.name = player_name
    if not player_name == "":
        return
    Cloud "You haven't given me your name yet."
    Cloud "Please tell me your name."
    "Cloud smiled warmly at me."
    call screen ask_name("Tell Cloud your name.")
    $ player_name = _return
    if not player_name == "":
        return
    Cloud "Don't tell me you don't have a name?"
    Cloud "You must have one. Even a nickname."
    Cloud "What is your name?"
    "Cloud asked me once again, still having a smile on his face."
    call screen ask_name("Please tell Cloud your name.")
    $ player_name = _return
    if not player_name == "":
        return
    Cloud "Ha!"
    "Cloud exclaimed loudly. He seems to be irritated."
    Cloud "My patience is running out."
    Cloud "Are you stupid!?"
    Cloud "It's either you are being stubborn or you are really stupid since you don't even know your own name."
    Cloud "What am I to do with you?"
    "Cloud sighed."
    Cloud "I'll give you once last chance."
    Cloud "Just tell me your name kid, please."
    call screen ask_name("Just tell Cloud your name. You'll regret it if you don't.")
    $ player_name = _return
    if not player_name == "":
        return
    Cloud "Fine! I'll name you myself!"
    "Cloud shouted."
    Cloud "From now on, your name is Stupid."
    $ grant_achievement("Achv9")
    $ player_name = "Stupid"
    $ Child.name = player_name
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