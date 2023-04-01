# offset
init offset = -8
################################################################################

# Imaginary friends configurations
define config.rollback_enabled = False
################################################################################

# Imaginary friends gui
define gui_path = "gui/imaginary_friends/"
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
define font_title = gui_path + "Griffy-Regular.ttf"
define font_regular = gui_path + "SongMyung-Regular.ttf"
define img_badge = gui_path + "badge.png"
define icon_memories = gui_path + "memories.png"
define icon_achievement = gui_path + "achievement.png"
define icon_cancel = gui_path + "cancel.png"
define icon_back_arrow = gui_path + "back_arrow.png"
define icon_menu = gui_path + "menu.png"
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
    Phantom : 100,
    Someone : 100
}
################################################################################

# Achievement
define achievement_list = {
    "Title1": "Some Description",
    "Title2": "Some Description",
    "Title3": "Some Description",
    "Title4": "Some Description",
    "Title5": "Some Description",
    "Title6": "Some Description",
    "Title7": "Some Description",
    "Title8": "Some Description",
    "Title9": "Some Description"
}

default achievement_values = {
    "Title1": True,
    "Title2": True,
    "Title3": True,
    "Title4": True,
    "Title5": True,
    "Title6": True,
    "Title7": True,
    "Title8": False,
    "Title9": False,
}
################################################################################

# Memories

################################################################################