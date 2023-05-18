# Utility Screens
screen ask(who, question):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text who style "namebox"
            text question style "input_prompt"
            input id "input"
##############################################################################################################

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
            if has_back_page():
                imagebutton:
                    yalign 0
                    xoffset 10
                    yoffset 10
                    idle button_prev_page
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
            if has_next_page():
                imagebutton:
                    xalign 1.0
                    yalign 0
                    xoffset -10
                    yoffset 10
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
        # background im.Crop(bg_paper, (0, 0, 1600, 800))
        grid 3 calculate_rows(3, achievement_list):
            xfill True
            yfill True
            for key, value in sorted_achievements.items():
                grid 2 1:
                    xfill True
                    yfill True
                    frame:
                        xfill True
                        yfill True
                        background None
                        if value["granted"]:
                            imagebutton:
                                xalign 0.5
                                yalign 0.5
                                idle im.FactorScale(img_badge, 0.4)
                                action Show("badge", img=img_badge)
                        else:
                            image im.FactorScale(im.Grayscale(img_badge), 0.4):
                                xalign 0.5
                                yalign 0.5
                    vbox:
                        xfill True
                        spacing 10
                        xalign 0.3
                        yalign 0.5
                        text _(value["title"]):
                            size gui.text_size
                            color identify_text_color(key)
                        text _(identify_achievement_description(key)):
                            size gui.notify_text_size
                            color identify_text_color(key)

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
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle icon_menu
        selected_idle icon_cancel
        selected_hover icon_cancel
        action ToggleScreen("statsUI")

screen statsUI():
    zorder 100
    # tag menu
    # modal True
    frame:
        xsize 650
        ysize 800
        xalign 1.0
        left_padding 25
        # background bg_paper
        vbox:
            xfill True
            yoffset 10
            vbox:
                xfill True
                spacing 10
                text _("STATS"):
                    xalign 0.5
                    font font_stats
                    color black
                    size (gui.name_text_size + 10)
                text "Name: [player_name]":
                    color black
                    font font_stats
                text _("Sanity:"):
                    color black
                    font font_stats
                bar:
                    xalign 0.3
                    range 100
                    value sanity
                    xsize 500
                    left_bar im.Color(bar_white, ColorSpectrum.get_color_spectrum(sanity))
                    # left_bar identify_bar_color(sanity)
                    right_bar bar_black
                text _("Happiness:"):
                    color black
                    font font_stats
                bar:
                    xalign 0.3
                    range 100
                    value happiness
                    xsize 500
                    left_bar im.Color(bar_white, ColorSpectrum.get_color_spectrum(happiness))
                    # left_bar identify_bar_color(happiness)
                    right_bar bar_black
            frame:
                xfill True
                top_margin 50
                bottom_padding 50
                background None
                image crayon_black_line:
                    xsize 565
                    yoffset -30
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    vbox:
                        xfill True
                        spacing 10
                        text _("IMAGINARY FRIENDS"):
                            xalign 0.5
                            font font_stats
                            color black
                            size gui.name_text_size
                        for key, value in friends_stats.items():
                            text identify_character(key):
                                color black
                                font font_stats
                            bar:
                                xalign 0.2
                                range 100
                                value value["stats"]
                                xsize 500
                                left_bar im.Color(bar_white, ColorSpectrum.get_color_spectrum(happiness))
                                # left_bar identify_bar_color(value["stats"])
                                right_bar bar_black
#####################################################################S#########################################

# Screen for Developer Options
screen developer():
    zorder 210
    drag:
        xalign 0.5
        yoffset 30
        image icon_developer
        clicked ToggleScreen("developerOptions")

screen developerOptions():
    zorder 200
    add semi_transparent
    dismiss action Hide("developerOptions")
    frame:
        xalign 0.0
        yalign 0.0
        yoffset 100
        xoffset 100
        background None
        grid 3 4:
            xspacing 50
            yspacing 10
            textbutton "Grant All Achievements" action Function(grant_all_achievements)
            textbutton "Randomly Grant Achievement" action Function(randomly_grant_achievement)
            textbutton "Remove All Achievements" action Function(remove_all_achievements)
            textbutton "Write All Diary Pages" action Function(write_all_diary_pages)
            textbutton "Randomly Write Diary" action Function(randomly_write_diary)
            textbutton "Remove All Diary Pages" action Function(remove_all_diary_pages)
            textbutton "Open Diary" action ShowMenu("diary")
            textbutton "Open Achievements" action ShowMenu("achievements")
            vbox:
                text "Sanity:"
                bar:
                    xsize 300
                    left_bar sugar_plum
                    right_bar jacarta
                    thumb american_violet
                    value VariableValue("sanity", 100)
            vbox:
                text "Happiness:"
                bar:
                    xsize 300
                    left_bar sugar_plum
                    right_bar jacarta
                    thumb american_violet
                    value VariableValue("happiness", 100)
            textbutton "Previous Dialogue" action Rollback()
            null
##############################################################################################################