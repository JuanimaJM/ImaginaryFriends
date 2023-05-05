# Offset
init offset = -8
##############################################################################################################

# Imaginary Friends Configurations
define config.rollback_enabled = False
##############################################################################################################

# Imaginary Friends GUI
define semi_transparent ="#000000bf"
define transparent = "#ffffff00"
define american_violet = '#5b1e99'
define american_purple = '#3d1466'
define sugar_plum = '#864879'
define jacarta = '#3F3351'
define dark_gunmetal = '#1f1d36ff'
define pastel_pink = '#E9A6A6'
define electric_green = "#00FF00"
define mango_green = "#8EFD00"
define lemon_glacier = "#FAFF00"
define american_orange = "#FF8A00"
define red = "#FF0000"
define white = "#ffffff"
define black = "#000000"
define gray = "#808080"
define black_olive = "#3e3e3e"
define alice_blue = "#F0F8FF"
define font_title = "gui/fonts/Griffy-Regular.ttf"
define font_regular = "gui/fonts/SongMyung-Regular.ttf"
define font_stats = "gui/fonts/erasdust.ttf"
define img_badge = "images/achievement/badge.png"
define icon_diary_white = "gui/icons/ic_diary_white.png"
define icon_diary_black = "gui/icons/ic_diary_black.png"
define icon_achievement_white = "gui/icons/ic_achievement_white.png"
define icon_achievement_black = "gui/icons/ic_achievement_black.png"
define button_back_arrow = "gui/icons/button_back.png"
define button_prev_page = "gui/icons/button_prev_page.png"
define button_next_page = "gui/icons/button_next_page.png"
define icon_cancel = "gui/icons/ic_cancel.png"
define icon_menu = "gui/icons/ic_menu.png"
define icon_debug = "gui/icons/ic_debug.png"
define bar_green = "gui/bar/bar_green.png"
define bar_yellowgreen = "gui/bar/bar_yellowgreen.png"
define bar_yellow = "gui/bar/bar_yellow.png"
define bar_orange = "gui/bar/bar_orange.png"
define bar_red = "gui/bar/bar_red.png"
define bar_white = "gui/bar/bar_white.png"
define bar_black = "gui/bar/bar_black.png"
define bg_left_page = "gui/frame_backgrounds/left_page.png"
define bg_right_page = "gui/frame_backgrounds/right_page.png"
define bg_paper = "gui/frame_backgrounds/bg_paper.jpg"
define paper_textbox = "gui/frame_backgrounds/paper_textbox.png"
define paper_namebox = "gui/frame_backgrounds/paper_namebox.png"
define paper_frame = "gui/frame_backgrounds/paper_frame.png"
define paper_slot = "gui/frame_backgrounds/paper_slot.png"
define scrollbar_crayon = "gui/scrollbar/scrollbar_crayon.png"
define scrollbar_paper_white = "gui/scrollbar/scrollbar_paper_white.png"
define scrollbar_paper_black = "gui/scrollbar/scrollbar_paper_black.png"
define crayon_black_line = "gui/scrollbar/crayon_black_line.png"
define leaf_particles1 = SnowBlossom(im.FactorScale("images/extra/leaf.png", 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=3)
define leaf_particles2 = SnowBlossom(im.FactorScale(im.Flip("images/extra/leaf.png", horizontal=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=5)
define leaf_particles3 = SnowBlossom(im.FactorScale(im.Flip("images/extra/leaf.png", vertical=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=7)

# Changing GUI
default icon_diary = timely_icon_diary()
default icon_achievement = timely_icon_achievement()
default bg_timely_main_menu = timely_bg()
##############################################################################################################

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default player_name = "Child"
define Child = Character("[player_name]", color=sugar_plum)
define Phantom = Character("Phantom", color=american_purple)
define Someone = Character("Someone", color=dark_gunmetal)
##############################################################################################################

# Stats
default sanity = 100
default happiness = 100
default friends_stats = {
    Phantom.name: {
        "stats": 0,
        "meet": False
    },
    Someone.name: {
        "stats": 0,
        "meet": False
    }
}
##############################################################################################################

# Achvievement
default achievement_unlocked = False
define achievement_list = {
    "Achv1": {
        "title": "Normal Ending",
        "description": "Get a normal ending.",
        "granted": True
    },
    "Achv2": {
        "title": "Best Ending",
        "description": "Help all of your friends.",
        "granted": True
    },
    "Achv3": {
        "title": "I'm the Menu",
        "description": "Get eaten.",
        "granted": True
    },
    "Achv4": {
        "title": "Moonlight Lovers",
        "description": "Unite the couple.",
        "granted": True
    },
    "Achv5": {
        "title": "Bad ending 1",
        "description": "Get the first bad ending.",
        "granted": True
    },
    "Achv6": {
        "title": "The Cat Idol",
        "description": "Meet the Cat Idol.",
        "granted": True
    },
    "Achv7": {
        "title": "The Dog Idol",
        "description": "Meet the Dog Idol.",
        "granted": False
    },
    "Achv8": {
        "title": "The Blue Alien",
        "description": "Meet the Blue Alien.",
        "granted": False
    },
    "Achv9": {
        "title": "Secret Ending",
        "description": "Get the secret ending.",
        "granted": False
    }
}

default sorted_achievements = {k: v for k, v in sorted(achievement_list.items(), key=lambda x: (not x[1]["granted"], x[0]))}

##############################################################################################################

# Diary
default diary_unlocked = False
default first_page = 1
default second_page = 2
define diary_content = {
    "Apple": {
        "content": "images/diary/apple_diary.png",
        "found": False
    },
    "Cat": {
        "content": "images/diary/cat_diary.png",
        "found": True
    },
    "Teddy": {
        "content": "images/diary/teddy_diary.png",
        "found": True
    },
    "Ghost": {
        "content": "images/diary/ghost_diary.png",
        "found": False
    },
    "Tree": {
        "content": "images/diary/tree_diary.png",
        "found": False
    },
    "Family": {
        "content": "images/diary/family_diary.png",
        "found": False
    }
}
define diary_pages = [value["content"] for key, value in diary_content.items() if value.get("found", False)]
##############################################################################################################