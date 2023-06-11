# Utility Screens
screen ask_name(question=""):
    on "show" action SetVariable("default_name", random_name())

    frame:
        xalign 0.5
        yalign 0.2
        xysize (1000, 200)
        
        vbox:
            text question:
                xalign 0.5
                color black

            frame:
                background None
                imagebutton:
                    xpos 40
                    idle button_randomizer
                    action SetVariable("default_name", random_name())

                input id "input":
                    xalign 0.5
                    length 12
                    allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                    value VariableInputValue("default_name", returnable=True)

screen script_keymap():
    key "repeat_ctrl_alt_shift_K_RIGHT" action Function(update_player_stats, "sanity", sanity + 1)
    key "repeat_ctrl_alt_shift_K_LEFT" action Function(update_player_stats, "sanity", sanity - 1)
    key "repeat_ctrl_alt_shift_K_UP" action Function(update_player_stats, "happiness", happiness + 1)
    key "repeat_ctrl_alt_shift_K_DOWN" action Function(update_player_stats, "happiness", happiness - 1)
    key "ctrl_alt_shift_K_n" action Function(set_random_name)
##############################################################################################################

# Script Scenes
#
#
#
# Map for EntranceHall
screen entranceHall():
    add "images/scenes/entrancehall.png"

    imagebutton:
        xpos 429
        ypos 316
        idle "images/scenes/entrancehall/door_kitchen.png"
        hover im.Color("images/scenes/entrancehall/door_kitchen.png", vivid_cerulean)
        action Call("kitchen")

    imagebutton:
        xpos 657
        ypos 477
        idle "images/scenes/entrancehall/door_dining.png"
        hover im.Color("images/scenes/entrancehall/door_dining.png", vivid_cerulean)
        action Call("dining")

    imagebutton:
        xpos 777
        ypos 564
        idle "images/scenes/entrancehall/door_bathroom1.png"
        hover im.Color("images/scenes/entrancehall/door_bathroom1.png", vivid_cerulean)
        action Call("bathroom1")

    imagebutton:
        xpos 845
        ypos 583
        idle "images/scenes/entrancehall/door_livingroom.png"
        hover im.Color("images/scenes/entrancehall/door_livingroom.png", vivid_cerulean)
        action Call("livingroom")

    imagebutton:
        xpos 1421
        ypos 315
        idle "images/scenes/entrancehall/door_basement.png"
        hover im.Color("images/scenes/entrancehall/door_basement.png", vivid_cerulean)
        action Call("basement")

    imagebutton:
        xpos 1164
        ypos 50
        idle "images/scenes/entrancehall/door_laundry.png"
        hover im.Color("images/scenes/entrancehall/door_laundry.png", vivid_cerulean)
        action Call("laundry")

screen hallWay():
    text "HallWay"
##############################################################################################################

# Screen for Diary
screen diary():
    if config.developer:
        key "ctrl_alt_shift_K_a" action Function(write_all_diary_pages)
        key "ctrl_alt_shift_K_r" action Function(randomly_write_diary)
        key "ctrl_alt_shift_K_d" action Function(remove_all_diary_pages)

    tag menu
    # add gui.game_menu_background
    add timely_bg_game_menu()
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
        xsize 1640
        ysize 820
        xalign 0.5
        yalign 0.7
        frame:
            xpos 10
            xsize 820
            yfill True
            background bg_left_page
            if len(persistent.diary_pages) > 0:
                image persistent.diary_pages[first_page - 1]:
                    xalign 0.5
                    yalign 0.5
            text "[first_page]":
                color black
                xalign 0.5
                yalign 0.98
            if has_back_page():
                imagebutton:
                    yalign 0
                    xoffset 10
                    yoffset 10
                    idle button_prev_page
                    action Function(back_page)
        frame:
            xpos -10
            xsize 820
            yfill True
            background bg_right_page
            if identify_second_page():
                image persistent.diary_pages[second_page - 1]:
                    xalign 0.5
                    yalign 0.5
            text "[second_page]":
                color black
                xalign 0.5
                yalign 0.98
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
    if config.developer:
        key "ctrl_alt_shift_K_a" action Function(grant_all_achievements)
        key "ctrl_alt_shift_K_r" action Function(randomly_grant_achievement)
        key "ctrl_alt_shift_K_d" action Function(remove_all_achievements)

    tag menu
    # add gui.game_menu_background
    add timely_bg_game_menu()
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
        grid 3 calculate_rows(3, persistent.achievement_list):
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
    frame:
        xsize 650
        ysize 800
        xalign 1.0
        left_padding 25
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
                if not player_name == "":
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
                    left_bar im.Color(bar_white, ColorSpectrum(sanity).get_color_spectrum())
                    right_bar bar_black
                text _("Happiness:"):
                    color black
                    font font_stats
                bar:
                    xalign 0.3
                    range 100
                    value happiness
                    xsize 500
                    left_bar im.Color(bar_white, ColorSpectrum(happiness).get_color_spectrum())
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
                                left_bar im.Color(bar_white, ColorSpectrum(value["stats"]).get_color_spectrum())
                                right_bar bar_black
##############################################################################################################

# Screen for Character Profile
screen profile():
    tag menu
    add timely_bg_game_menu()
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle button_back_arrow
        action Return()
    text _("Character Profile"):
        yalign 0.0
        xalign 0.5
        font font_title
        size gui.title_text_size
    use profile_book

screen profile_book():
    fixed:
        xfill True
        ysize 820
        xoffset 40
        xalign 0.5
        yalign 0.7
        vbox:
            xpos 1400
            yoffset 100
            xfit True
            yfit True
            spacing 20
            style_prefix "bookmark"
            textbutton "Characters" action ShowMenu("character_tab")
            textbutton "Info" action ShowMenu("info_tab")
            textbutton "Lore" action ShowMenu("lore_tab")
        frame:
            xsize 820
            yfill True
            background bg_left_page

screen character_tab():
    tag menu
    use profile
    fixed:
        xfill True
        ysize 820
        xoffset 40
        xalign 0.5
        yalign 0.7
        frame:
            xpos 800
            xsize 820
            yfill True
            background bg_right_page
            text "Character"

screen info_tab():
    tag menu
    use profile
    fixed:
        xfill True
        ysize 820
        xoffset 40
        xalign 0.5
        yalign 0.7
        frame:
            xpos 800
            xsize 820
            yfill True
            background bg_right_page
            text "Info"

screen lore_tab():
    tag menu
    use profile
    fixed:
        xfill True
        ysize 820
        xoffset 40
        xalign 0.5
        yalign 0.7
        frame:
            xpos 800
            xsize 820
            yfill True
            background bg_right_page
            text "Lore"
##############################################################################################################

# Screen for Developer Options
screen developer():
    zorder 210
    frame:
        yoffset 30
        background None
        xysize (1920, 50)
        if showDevMenu:
            drag:
                xalign 0.5
                add icon_developer
                clicked [ToggleScreen("developerOptions"), ToggleVariable("showDevMenu")]

screen developerOptions():
    zorder 200
    add semi_transparent
    dismiss action [Hide("developerOptions"), ToggleVariable("showDevMenu")]
    frame:
        xalign 0.0
        yalign 0.0
        yoffset 100
        xoffset 100
        background None
        grid 3 5:
            xspacing 50
            yspacing 10
            textbutton "Delete Persistent" action Show("confirm", message="Are you sure you want to delete persistent data?", yes_action=Function(delete_persistent), no_action=Hide("confirm"))
            textbutton "Previous Dialogue" action Rollback()
            textbutton "Grant All Achievements" action Function(grant_all_achievements)
            textbutton "Randomly Grant Achievement" action Function(randomly_grant_achievement)
            textbutton "Remove All Achievements" action Function(remove_all_achievements)
            textbutton "Write All Diary Pages" action Function(write_all_diary_pages)
            textbutton "Randomly Write Diary" action Function(randomly_write_diary)
            textbutton "Remove All Diary Pages" action Function(remove_all_diary_pages)
            textbutton "Open Diary" action ShowMenu("diary")
            textbutton "Open Achievements" action ShowMenu("achievements")
            textbutton "Set Random Name" action Function(set_random_name)
            textbutton "Unlock Character Profile" action SetVariable("persistent.profiles_unlocked", True)
            vbox:
                text "Sanity: ([sanity])"
                bar:
                    xsize 300
                    left_bar sugar_plum
                    right_bar jacarta
                    thumb american_violet
                    value VariableValue("sanity", 100)
            vbox:
                text "Happiness: ([happiness])"
                bar:
                    xsize 300
                    left_bar sugar_plum
                    right_bar jacarta
                    thumb american_violet
                    value VariableValue("happiness", 100)
            vbox:
                text "Time: ([game_time])"
                bar:
                    xsize 300
                    left_bar sugar_plum
                    right_bar jacarta
                    thumb american_violet
                    value VariableValue("game_time", 7)
##############################################################################################################