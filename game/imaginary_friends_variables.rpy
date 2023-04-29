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
define font_title = gui_path("Griffy-Regular.ttf")
define font_regular = gui_path("SongMyung-Regular.ttf")
define font_stats = gui_path("erasdust.ttf")
define img_badge = gui_path("badge.png")
define icon_diary_white = gui_path("ic_diary_white.png")
define icon_achievement_white = gui_path("ic_achievement_white.png")
define button_back_arrow = gui_path("button_back.png")
define button_back_page = gui_path("button_back_page.png")
define button_next_page = gui_path("button_next_page.png")
define icon_cancel = gui_path("stats_selected_idle.png")
define icon_menu = gui_path("stats_idle.png")
define bg_left_page = gui_path("left_page.png")
define bg_right_page = gui_path("right_page.png")
define bar_green = gui_path("bar_green.png")
define bar_yellowgreen = gui_path("bar_yellowgreen.png")
define bar_yellow = gui_path("bar_yellow.png")
define bar_orange = gui_path("bar_orange.png")
define bar_red = gui_path("bar_red.png")
define bar_white = gui_path("bar_white.png")
define bar_black = gui_path("bar_black.png")
define bg_paper = gui_path("bg_paper.jpg")
define scrollbar_crayon = gui_path("scrollbar_crayon.png")
define scrollbar_paper_white = gui_path("scrollbar_paper_white.png")
define scrollbar_paper_black = gui_path("scrollbar_paper_black.png")
define crayon_black_line = gui_path("crayon_black_line.png")
define leaf_particles1 = SnowBlossom(im.FactorScale(gui_path("leaf.png"), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=1)
define leaf_particles2 = SnowBlossom(im.FactorScale(im.Flip(gui_path("leaf.png"), horizontal=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=3)
define leaf_particles3 = SnowBlossom(im.FactorScale(im.Flip(gui_path("leaf.png"), vertical=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=5)

# Changing GUI
default icon_diary = timely_icon_diary()
default icon_achievement = timely_icon_achievement()
default bg_timely_main_menu = timely_bg()
##############################################################################################################

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default player_name = "Child"
define Child = Character("[player_name]", color=sugar_plum)
define Phantom = Character("Phantom", color=american_purple, font=font_title)
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
        "content": "images/apple_diary.png",
        "found": False
    },
    "Cat": {
        "content": "images/cat_diary.png",
        "found": True
    },
    "Teddy": {
        "content": "images/teddy_diary.png",
        "found": False
    },
    "Ghost": {
        "content": "images/ghost_diary.png",
        "found": False
    },
    "Tree": {
        "content": "images/tree_diary.png",
        "found": False
    },
    "Family": {
        "content": "images/family_diary.png",
        "found": True
    }
}
define diary_pages = [value["content"] for key, value in diary_content.items() if value.get("found", False)]
##############################################################################################################