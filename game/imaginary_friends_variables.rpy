# offset
init offset = -8
################################################################################

# Imaginary friends configurations
define config.rollback_enabled = False
################################################################################

# Imaginary friends gui
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
define font_title = gui_path("Griffy-Regular.ttf")
define font_regular = gui_path("SongMyung-Regular.ttf")
define img_badge = gui_path("badge.png")
define icon_memories = gui_path("memories.png")
define icon_achievement = gui_path("achievement.png")
define icon_back_arrow = gui_path("back_arrow.png")
define icon_cancel = gui_path("stats_selected_idle.png")
define icon_menu = gui_path("stats_idle.png")
################################################################################

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Child = Character("The Child", color=sugar_plum)
define Phantom = Character("Phantom", color=american_purple, font=font_title)
define Someone = Character("Someone", color=dark_gunmetal)
################################################################################

# Stats
default sanity = 100
default happiness = 100
default friends_stats = {
    Phantom : 0,
    Someone : 0
}
################################################################################

# Achvievement
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
        "granted": False
    },
    "Achv4": {
        "title": "Moonlight Lovers",
        "description": "Unite the couple.",
        "granted": True
    },
    "Achv5": {
        "title": "Bad ending 1",
        "description": "Get the first bad ending.",
        "granted": False
    },
    "Achv6": {
        "title": "The Cat Idol",
        "description": "Meet the Cat Idol.",
        "granted": False
    },
    "Achv7": {
        "title": "The Dog Idol",
        "description": "Meet the Dog Idol.",
        "granted": True
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

################################################################################

# Memories
default first_page = 1
default second_page = 2
default memories_list = ("Page 1")
################################################################################