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
define dark_gunmetal = '#1F1D36'
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
    "Achv1": ("Title1", "Some Description"),
    "Achv2": ("Title2", "Some Description"),
    "Achv3": ("Title3", "Some Description"),
    "Achv4": ("Title4", "Some Description"),
    "Achv5": ("Title5", "Some Description"),
    "Achv6": ("Title6", "Some Description"),
    "Achv7": ("Title7", "Some Description"),
    "Achv8": ("Title8", "Some Description"),
    "Achv9": ("Title9", "Some Description")
}

default achievement_values = {
    "Achv1": True,
    "Achv2": True,
    "Achv3": False,
    "Achv4": True,
    "Achv5": False,
    "Achv6": True,
    "Achv7": True,
    "Achv8": False,
    "Achv9": False,
}
################################################################################

# Memories
default first_page = 1
default second_page = 2
default memories_list = ("Page 1")
################################################################################