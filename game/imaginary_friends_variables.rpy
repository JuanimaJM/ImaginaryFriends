# Offset
init offset = -8
##############################################################################################################

# Imaginary Friends Configurations
define config.rollback_enabled = True
define config.developer = True
define allowDev = True
default showDevMenu = True
default game_time = 4
##############################################################################################################

# Imaginary Friends GUI
# Colors
define semi_transparent ="#000000bf"
define transparent = "#ffffff00"
define american_violet = '#5b1e99'
define american_purple = '#3d1466'
define sugar_plum = '#864879'
define jacarta = '#3F3351'
define dark_gunmetal = '#1f1d36'
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
define pastel_green = "#77dd77"
define pastel_yellow = "#fdfd96"
define pastel_red = "#ff6961"

# Fonts
define font_title = "gui/fonts/Griffy-Regular.ttf"
define font_regular = "gui/fonts/SongMyung-Regular.ttf"
define font_stats = "gui/fonts/erasdust.ttf"

# Assets
define img_badge = "images/achievement/badge.png"
define icon_diary_white = "gui/icons/ic_diary_white.png"
define icon_diary_black = "gui/icons/ic_diary_black.png"
define icon_achievement_white = "gui/icons/ic_achievement_white.png"
define icon_achievement_black = "gui/icons/ic_achievement_black.png"
define button_back_arrow = "gui/icons/button_back.png"
define button_prev_page = "gui/icons/button_prev_page.png"
define button_next_page = "gui/icons/button_next_page.png"
define button_randomizer = "gui/icons/button_randomizer.png"
define icon_cancel = "gui/icons/ic_cancel.png"
define icon_menu = "gui/icons/ic_menu.png"
define icon_developer = "gui/icons/ic_dev_menu.png"
define bar_white = "gui/bar/bar_white.png"
define bar_black = "gui/bar/bar_black.png"
define bg_left_page = "gui/frame_backgrounds/left_page.png"
define bg_right_page = "gui/frame_backgrounds/right_page.png"
define bg_paper = "gui/frame_backgrounds/bg_paper.jpg"
define paper_textbox = "gui/frame_backgrounds/paper_textbox.png"
define paper_namebox = "gui/frame_backgrounds/paper_namebox.png"
define paper_frame = "gui/frame_backgrounds/paper_frame.png"
define paper_idle_slot = "gui/frame_backgrounds/paper_idle_slot.png"
define paper_hover_slot = "gui/frame_backgrounds/paper_hover_slot.png"
define paper_nvl = "gui/frame_backgrounds/paper_nvl.png"
define paper_skip = "gui/frame_backgrounds/paper_skip.png"
define paper_notify = "gui/frame_backgrounds/paper_notify.png"
define paper_checkbox = "gui/button/paper_checkbox.png"
define paper_checkedbox = "gui/button/paper_selected_checkbox.png"
define paper_choice = "gui/button/paper_choice.png"
define scrollbar_thumb_vertical = "gui/bar/scrollbar_thumb_vertical.png"
define slider_thumb_horizontal = "gui/bar/slider_thumb_horizontal.png"
define paper_idle_horizontal_bar = "gui/bar/paper_idle_horizontal_bar.png"
define paper_hover_horizontal_bar = "gui/bar/paper_hover_horizontal_bar.png"
define paper_idle_vertical_scrollbar = "gui/bar/paper_idle_vertical_scrollbar.png"
define paper_hover_vertical_scrollbar = "gui/bar/paper_hover_vertical_scrollbar.png"
define crayon_black_line = "gui/bar/crayon_black_line.png"

# Particles
define leaf_particles1 = SnowBlossom(im.FactorScale("images/extra/leaf.png", 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=3)
define leaf_particles2 = SnowBlossom(im.FactorScale(im.Flip("images/extra/leaf.png", horizontal=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=9)
define leaf_particles3 = SnowBlossom(im.FactorScale(im.Flip("images/extra/leaf.png", vertical=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=15)
##############################################################################################################

# Declare characters used by this game. The color argument colorizes the name of the character.
default default_name = random_name()
default player_name = ""
define name_list = (
    "Alex", "Andy", "Charly", "Dylan", "Finli", "Frankie", "Jade", "Jayden", "Jacky", "Jaymee", "Jesse", "Jordan", "Ky", "Kendall", "Kyran",
    "Lane", "Micky", "Quin", "Rayne", "Reese", "Riley", "Robin", "Sky", "Tony", "Tris"
)
define Child = Character("[player_name]", color=sugar_plum)
define Phantom = Character("Phantom", color=american_purple)
define Someone = Character("Someone", color=dark_gunmetal)

# Other Characters
define Mother = Character("Mother")
define Father = Character("Father")
define Cloud = Character("Cloud")
define Jayem = Character("Jayem")
define Jennie = Character("Jennie")
define Ali = Character("Ali")
define Kimmy = Character("Kimmy")

# The Seven Imaginary Friends
define Aithne = Character("Aithne")
define Barktholomeow = Character("Barktholomeow")
define Bertrand = Character("Bertrand")
define Blayr = Character("Blayr")
define Carwyn = Character("Carwyn")
define Iris = Character("Iris")
define Mikaela = Character("Mikaela")
##############################################################################################################

# Stats
default sanity = 100
default happiness = 100
default friends_stats = {
    "Phantom": {
        "stats": 0,
        "meet": False
    },
    "Someone": {
        "stats": 0,
        "meet": False
    },
    "Aithne": {
        "stats": 0,
        "meet": False
    },
    "Barktholomeow": {
        "stats": 0,
        "meet": False
    },
    "Bertrand": {
        "stats": 0,
        "meet": False
    },
    "Blayr": {
        "stats": 0,
        "meet": False
    },
    "Carwyn": {
        "stats": 0,
        "meet": False
    },
    "Iris": {
        "stats": 0,
        "meet": False
    },
    "Mikaela": {
        "stats": 0,
        "meet": False
    }
}
##############################################################################################################

# Achievement
default achievement_unlocked = False
define persistent.achievement_list = {
    "Achv1": {
        "title": "Normal Ending",
        "description": "Get a normal ending.",
        "granted": False
    },
    "Achv2": {
        "title": "Best Ending",
        "description": "Help all of your friends.",
        "granted": False
    },
    "Achv3": {
        "title": "I'm the Menu",
        "description": "Get eaten.",
        "granted": False
    },
    "Achv4": {
        "title": "Moonlight Lovers",
        "description": "Unite the couple.",
        "granted": False
    },
    "Achv5": {
        "title": "The Cat Idol",
        "description": "Meet the Cat Idol.",
        "granted": False
    },
    "Achv6": {
        "title": "The Dog Idol",
        "description": "Meet the Dog Idol.",
        "granted": False
    },
    "Achv7": {
        "title": "The Blue Alien",
        "description": "Meet the Blue Alien.",
        "granted": False
    },
    "Achv8": {
        "title": "Secret Ending",
        "description": "Get the secret ending.",
        "granted": False
    },
    "Achv9": {
        "title": "Are you Stupid? Ending",
        "description": "Don't tell your name.",
        "granted": False
    }
}

default sorted_achievements = {k: v for k, v in sorted(persistent.achievement_list.items(), key=lambda x: (not x[1]["granted"], x[0]))}
##############################################################################################################

# Diary
default diary_unlocked = False
default first_page = 1
default second_page = 2
define persistent.diary_content = {
    "Apple": {
        "content": "images/diary/apple_diary.png",
        "found": False
    },
    "Cat": {
        "content": "images/diary/cat_diary.png",
        "found": False
    },
    "Teddy": {
        "content": "images/diary/teddy_diary.png",
        "found": False
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
define persistent.diary_pages = [value["content"] for key, value in persistent.diary_content.items() if value.get("found", False)]
##############################################################################################################