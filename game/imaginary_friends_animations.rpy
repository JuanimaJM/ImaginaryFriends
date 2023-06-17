label splashscreen:
    # $ _dismiss_pause = False
    $ renpy.movie_cutscene("videos/spring_studios_splash.webm")
    show text "All characters, events, and other items in this game are fictional." with dissolve
    pause 5
    hide text with dissolve
    show text "Any resemblance to people, things, and any entity in reality is purely coincidental." with dissolve
    pause 5
    hide text with dissolve
    $ _dismiss_pause = True
    return