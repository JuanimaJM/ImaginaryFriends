# Screen for Diary
screen diary():
    tag menu
    add gui.game_menu_background

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle icon_back_arrow
        action Return()
    
    text _("Diary"):
        yalign 0.0
        xalign 0.5
        font font_title
        size gui.title_text_size

    use book

screen book():
    hbox:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.6
        frame:
            xsize 800
            yfill True
            background jacarta
            text diary_list[first_page - 1]
            if identify_back_page():
                imagebutton:
                    yalign 1.0
                    xoffset 10
                    yoffset -10
                    idle icon_back_arrow
                    action Function(back_page)
        
        frame:
            xsize 800
            yfill True
            background dark_gunmetal
            if identify_second_page():
                text diary_list[second_page - 1]
            
            if identify_next_page():
                imagebutton:
                    xalign 1.0
                    yalign 1.0
                    xoffset -10
                    yoffset -10
                    idle icon_next_arrow
                    action Function(next_page)

################################################################################

# Screen for Achievements
screen achievements():
    tag menu
    add gui.game_menu_background

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle icon_back_arrow
        action Return()
    
    text _("Achievements"):
        yalign 0.0
        xalign 0.5
        font font_title
        size gui.title_text_size
    
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.6
        background dark_gunmetal
        grid 3 3:
            xfill True
            yfill True
            for key in achievement_list:
                frame:
                    background None
                    hbox:
                        xfill True
                        yfill True
                        spacing 20
                        image identify_image(key):
                                xalign 0.0
                                yalign 0.5
                        vbox:
                            xfill True
                            spacing 10
                            xalign 0.3
                            yalign 0.5
                            text _(achievement_list[key]["title"]):
                                size gui.label_text_size
                            text _(identify_achievement_description(key)):
                                size gui.notify_text_size
################################################################################

# Screen for Stats
screen stats():
    zorder 110
    imagebutton auto ("gui/imaginary_friends/stats_%s.png"):
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        action ToggleScreen("statsUI")

screen statsUI():
    zorder 100
    tag menu
    modal True
    frame:
        xsize 500
        ysize 1080
        xalign 1.0
        padding(20, 20)
        background dark_gunmetal
        
        vbox:
            xsize 500
            yoffset 50
            vbox:
                spacing 10
                text _("STATS"):
                    xalign 0.5
                    font font_title
                text "Name: Player"
                text _("Sanity:")
                bar:
                    range 100
                    value 90
                    xysize(400, 50)
                    left_bar identify_bar_color(90)
                    right_bar white
                text _("Happiness:")
                bar:
                    range 100
                    value 20
                    xysize(400, 50)
                    left_bar identify_bar_color(20)
                    right_bar white
            
            frame:
                top_padding 30
                right_padding 30
                bottom_padding 50
                background None
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    draggable True
                    vbox:
                        spacing 10
                        box_wrap True
                        text _("IMAGINARY FRIENDS"):
                            xalign 0.5
                            font font_title
                        for key in friends_stats:
                            text identify_character(key)
                            bar:
                                range 100
                                value friends_stats[key]["stats"]
                                xysize(400, 50)
                                left_bar identify_bar_color(friends_stats[key]["stats"])
                                right_bar white
################################################################################