# Screen for Diary
screen diary():
    tag menu
    add gui.game_menu_background
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle button_back_arrow
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
        yalign 0.7
        frame:
            xsize 800
            yfill True
            background bg_left_page
            if len(diary_pages) > 0:
                image diary_pages[first_page - 1]:
                    xalign 0.5
                    yalign 0.5
            text "[first_page]":
                color black
                xalign 0.5
                yalign 1.0
            if identify_back_page():
                imagebutton:
                    yalign 1.0
                    xoffset 30
                    yoffset -10
                    idle button_back_page
                    action Function(back_page)
        frame:
            xsize 800
            yfill True
            background bg_right_page
            if identify_second_page():
                image diary_pages[second_page - 1]:
                    xalign 0.5
                    yalign 0.5
            text "[second_page]":
                color black
                xalign 0.5
                yalign 1.0
            if identify_next_page():
                imagebutton:
                    xalign 1.0
                    yalign 1.0
                    xoffset -10
                    yoffset -10
                    idle button_next_page
                    action Function(next_page)

##############################################################################################################

# Screen for Achievements
screen achievements():
    tag menu
    add gui.game_menu_background
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle button_back_arrow
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
                grid 2 1:
                    xfill True
                    yfill True
                    frame:
                        xfill True
                        yfill True
                        background None
                        if achievement_list[key]["granted"]:
                            imagebutton:
                                xalign 0.5
                                yalign 0.5
                                idle img_badge
                                action Show("badge", img=img_badge)
                    vbox:
                        xfill True
                        spacing 10
                        xalign 0.3
                        yalign 0.5
                        text _(achievement_list[key]["title"]):
                            size gui.text_size
                        text _(identify_achievement_description(key)):
                            size gui.notify_text_size

screen badge(img):
    add semi_transparent
    dismiss action Hide("badge")
    frame:
        modal True
        xalign 0.5
        yalign 0.5
        background None
        image img:
            xsize 480
            ysize 400
##############################################################################################################

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
        xsize 600
        ysize 1080
        xalign 1.0
        left_padding 50
        background bg_paper
        vbox:
            xfill True
            yoffset 50
            vbox:
                xfill True
                spacing 10
                text _("STATS"):
                    xalign 0.5
                    font font_title
                    color black
                text "Name: [player_name]":
                    color black
                text _("Sanity:"):
                    color black
                bar:
                    range 100
                    value sanity
                    xsize 400
                    left_bar identify_bar_color(sanity)
                    right_bar bar_black
                text _("Happiness:"):
                    color black
                bar:
                    range 100
                    value happiness
                    xsize 400
                    left_bar identify_bar_color(happiness)
                    right_bar bar_black
            frame:
                xfill True
                top_margin 50
                bottom_padding 50
                background None
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    draggable True
                    vbox:
                        xfill True
                        spacing 10
                        box_wrap True
                        text _("IMAGINARY FRIENDS"):
                            xalign 0.5
                            font font_title
                            color black
                        for key in friends_stats:
                            text identify_character(key):
                                color black
                            bar:
                                range 100
                                value friends_stats[key]["stats"]
                                xsize 400
                                left_bar identify_bar_color(friends_stats[key]["stats"])
                                right_bar bar_black
##############################################################################################################