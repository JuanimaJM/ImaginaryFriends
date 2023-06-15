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
define vivid_cerulean = "#0099ff"

# Fonts
define font_curvy = "gui/fonts/Griffy-Regular.ttf"
define font_regular = "gui/fonts/SongMyung-Regular.ttf"
define font_hand_written = "gui/fonts/erasdust.ttf"

# Assets
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
define icon_white_bookmark = "gui/icons/white_bookmark.png"
define icon_purple_bookmark = "gui/icons/purple_bookmark.png"
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
define img_black_leaf = "images/extra/leaf.png"
define img_black_apple = "images/extra/black_apple.png"

# Particles
define leaf_particles1 = SnowBlossom(im.FactorScale(img_black_leaf, 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=3)
define leaf_particles2 = SnowBlossom(im.FactorScale(im.Flip(img_black_leaf, horizontal=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=9)
define leaf_particles3 = SnowBlossom(im.FactorScale(im.Flip(img_black_leaf, vertical=True), 0.3), count=5, horizontal=False, xspeed=(100, 150), yspeed=100, start=15)
##############################################################################################################

# Declare characters used by this game. The color argument colorizes the name of the character.
default default_name = random_name()
default player_name = ""
define name_list = (
    "Alex", "Andy", "Charly", "Dylan", "Finli", "Frankie", "Jade", "Jayden", "Jacky", "Jaymee", "Jesse", "Jordan", "Ky", "Kendall", "Kyran",
    "Lane", "Micky", "Quin", "Rayne", "Reese", "Riley", "Robin", "Sky", "Tony", "Tris"
)
define Child = Character("You", color=sugar_plum)
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

# Character Profile
default persistent.profiles_unlocked = False
default selected_character = list(characters_info.keys())[0]
define characters_info = {
    "Mother": {
        "Name": "Nameless Mother",
        "Alias": "The Mother",
        "Gender": "Female",
        "Age": "32",
        "Height": "160 cm",
        "Species": "Human",
        "Occupation": "Housewife",
        "Personality": "Ill-tempered, Frank, and Insensitive",
        "Image": "images/characters/mother serious_face.png"
    },
    "Father": {
        "Name": "Nameless Father",
        "Alias": "The Father",
        "Gender": "Male",
        "Age": "32",
        "Height": "185 cm",
        "Species": "Human",
        "Occupation": "Sales Manager",
        "Personality": "Quiet, Apathetic, and Indifferent",
        "Image": "images/characters/father.png"
    },
    "Jennie": {
        "Name": "Jennie",
        "Alias": "The Cat Idol",
        "Gender": "Female",
        "Age": "21",
        "Height": "161 cm",
        "Species": "Cat",
        "Occupation": "Idol",
        "Personality": "Cutesy and Cheerful",
        "Image": "images/characters/jennie closed_eye_smiling_face.png"
    },
    "Ali": {
        "Name": "Ali",
        "Alias": "The Dog Idol",
        "Gender": "Female",
        "Age": "22",
        "Height": "165 cm",
        "Species": "Dog",
        "Occupation": "Idol",
        "Personality": "Cool and Impatient",
        "Image": "images/characters/ali serious_face.png"
    },
    "Kimmy": {
        "Name": "Kimmy",
        "Alias": "The Blue Alien",
        "Gender": "Genderless",
        "Age": "Unknown",
        "Height": "174 cm",
        "Species": "Alien",
        "Language": "???",
        "Occupation": "Alien",
        "Personality": "Mysterious",
        "Image": "images/characters/kimmy.png"
    },
    "Jayem": {
        "Name": "Jayem",
        "Alias": "The Psychopomp",
        "Gender": "Genderless",
        "Age": "Unknown",
        "Height": "Unknown",
        "Species": "Unknown",
        "Occupation": "Unknown",
        "Personality": "Calm and Mysterious",
        "Image": "images/characters/jayem.png"
    },
    "Cloud": {
        "Name": "Cloud",
        "Alias": "The Clown",
        "Gender": "Male",
        "Age": "Unknown",
        "Height": "188 cm",
        "Species": "Demon",
        "Occupation": "Dream Demon",
        "Personality": "Friendly, Enthusiastic, and Mysterious",
        "Image": "images/characters/cloud closed_eye_smiling_face.png"
    },
    "Iris": {
        "Name": "Iris",
        "Alias": "The Mother Goat",
        "Sin": "Lust",
        "Gender": "Female",
        "Age": "29",
        "Height": "165 cm",
        "Species": "Goat",
        "Occupation": "Imaginary Friend",
        "Personality": "Cold but affectionate to children",
        "Image": "???"
    },
    "Barktholomeow": {
        "Name": "Barktholomeow",
        "Alias": "The Thieving Fox",
        "Sin": "Greed",
        "Gender": "Male",
        "Age": "27",
        "Height": "198 cm",
        "Species": "Fox",
        "Occupation": "Imaginary Friend",
        "Personality": "Greedy, Mischievous, and Cunning",
        "Image": "images/characters/barktholomeow.png"
    },
    "Aithne": {
        "Name": "Aithne",
        "Alias": "The Hot-headed Lioness",
        "Sin": "Wrath",
        "Gender": "Female",
        "Age": "20",
        "Height": "165 cm",
        "Species": "Lioness",
        "Occupation": "Imaginary Friend",
        "Personality": "Short-Tempered, Frank, Ambitious, and Passionate",
        "Image": "???"
    },
    "Bertrand": {
        "Name": "Bertrand",
        "Alias": "Count Peacock of Yorkshire",
        "Sin": "Pride",
        "Gender": "Male",
        "Age": "42",
        "Height": "195 cm",
        "Species": "Peacock",
        "Occupation": "Imaginary Friend",
        "Personality": "Prideful, Arrogant, Intellectual, and Stern",
        "Image": "???"
    },
    "Carwyn": {
        "Name": "Carwyn",
        "Alias": "Rag Doll Snake Groom",
        "Sin": "Envy",
        "Gender": "Male",
        "Age": "20",
        "Height": "185 cm",
        "Species": "Snake",
        "Occupation": "Imaginary Friend",
        "Personality": "Envious, Ambitious, Greedy, Faithful, and Loving Groom",
        "Image": "images/characters/carwyn.png"
    },
    "Mikaela": {
        "Name": "Mikaela",
        "Alias": "Rag Doll Bear Bride",
        "Sin": "Sloth",
        "Gender": "Female",
        "Age": "20",
        "Height": "160 cm",
        "Species": "Bear",
        "Occupation": "Imaginary Friend",
        "Personality": "Lazy, Apathetic, Faithful, and Loving Bride",
        "Image": "images/characters/mikaela.png"
    },
    "Blayr": {
        "Name": "Blayr",
        "Alias": "The Alcoholic Pig",
        "Sin": "Gluttony",
        "Gender": "Male",
        "Age": "19",
        "Height": "180 cm",
        "Species": "Pig",
        "Occupation": "Imaginary Friend",
        "Personality": "Alcoholic, Ambitious, Arrogant, Rebellious, and Hardworking",
        "Image": "???"
    }
}
##############################################################################################################

# Stats
default sanity = 20
default happiness = 20
default energy = 50
default hunger = 30
default thirst = 30
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
        "title": "The Friendly Clown",
        "description": "Meet the clown.",
        "granted": False,
        "image": "images/achievement/the_friendly_clown.png"
    },
    "Achv2": {
        "title": "The Mysterious Phantom",
        "description": "Meet the hooded figure.",
        "granted": False,
        "image": "images/achievement/the_mysterious_phantom.png"
    },
    "Achv3": {
        "title": "The Blue Alien",
        "description": "Meet the alien.",
        "granted": False,
        "image": "images/achievement/the_blue_alien.png"
    },
    "Achv4": {
        "title": "The White Cat",
        "description": "Meet the white cat idol.",
        "granted": False,
        "image": "images/achievement/the_white_cat.png"
    },
    "Achv5": {
        "title": "The Black Dog",
        "description": "Meet the black dog idol.",
        "granted": False,
        "image": "images/achievement/the_black_dog.png"
    },
    "Achv6": {
        "title": "The Pink Goat",
        "description": "Meet the goat.",
        "granted": False,
        "image": "images/achievement/the_pink_goat.png"
    },
    "Achv7": {
        "title": "The Golden Fox",
        "description": "Meet the fox.",
        "granted": False,
        "image": "images/achievement/the_golden_fox.png"
    },
    "Achv8": {
        "title": "The Red Lioness",
        "description": "Meet the lioness.",
        "granted": False,
        "image": "images/achievement/the_red_lioness.png"
    },
    "Achv9": {
        "title": "The Violet Peacock",
        "description": "Meet the peacock.",
        "granted": False,
        "image": "images/achievement/the_violet_peacock.png"
    },
    "Achv10": {
        "title": "The Green Snake",
        "description": "Meet the snake.",
        "granted": False,
        "image": "images/achievement/the_green_snake.png"
    },
    "Achv11": {
        "title": "The Blue Bear",
        "description": "Meet the bear.",
        "granted": False,
        "image": "images/achievement/the_blue_bear.png"
    },
    "Achv12": {
        "title": "The Orange Pig",
        "description": "Meet the pig.",
        "granted": False,
        "image": "images/achievement/the_orange_pig.png"
    },
    "Achv13": {
        "title": "Little Songbird",
        "description": "Sing a song to a friend.",
        "granted": False,
        "image": "images/achievement/little_songbird.png"
    },
    "Achv14": {
        "title": "Peaceful Death",
        "description": "Gain the I’m Still Weak Ending.",
        "granted": False,
        "image": "images/achievement/peaceful_death.png"
    },
    "Achv15": {
        "title": "Gingerbread House",
        "description": "Gain the Hansel and Gretel Ending.",
        "granted": False,
        "image": "images/achievement/gingerbread_house.png"
    },
    "Achv16": {
        "title": "Lonely Once Again",
        "description": "Gain the Failed Attempt Ending.",
        "granted": False,
        "image": "images/achievement/lonely_once_again.png"
    },
    "Achv17": {
        "title": "Happily Ever After",
        "description": "Gain the Happy Ending.",
        "granted": False,
        "image": "images/achievement/happily_ever_after.png"
    },
    "Achv18": {
        "title": "The Fallen Apple",
        "description": "Unlock the Character Profile.",
        "granted": False,
        "image": "images/achievement/the_fallen_apple.png"
    },
    "Achv19": {
        "title": "Dear Diary",
        "description": "Write on your diary for the first time.",
        "granted": False,
        "image": "images/achievement/dear_diary.png"
    },
    "Achv20": {
        "title": "Badge Hoarder",
        "description": "Gain all achievements.",
        "granted": False,
        "image": "images/achievement/badge_hoarder.png"
    }
}

default sorted_achievements = {k: v for k, v in sorted(persistent.achievement_list.items(), key=lambda x: (not x[1]["granted"], x[0]))}
##############################################################################################################

# Diary
default diary_unlocked = False
default first_page = 1
default second_page = 2
define persistent.diary_content = {
    "Tree": {
        "content": "images/diary/diary_tree.png",
        "found": False
    },
    "Cat": {
        "content": "images/diary/diary_cat.png",
        "found": False
    },
    "Bear": {
        "content": "images/diary/diary_bear.png",
        "found": False
    },
    "Phantom": {
        "content": "images/diary/diary_phantom.png",
        "found": False
    },
    "Dog": {
        "content": "images/diary/diary_dog.png",
        "found": False
    },
    "Snake": {
        "content": "images/diary/diary_snake.png",
        "found": False
    },
    "Lion": {
        "content": "images/diary/diary_lion.png",
        "found": False
    },
    "Fox": {
        "content": "images/diary/diary_fox.png",
        "found": False
    },
    "Peacock": {
        "content": "images/diary/diary_peacock.png",
        "found": False
    },
    "Pig": {
        "content": "images/diary/diary_pig.png",
        "found": False
    },
    "Goat": {
        "content": "images/diary/diary_goat.png",
        "found": False
    },
    "Cloud": {
        "content": "images/diary/diary_cloud.png",
        "found": False
    }
}
define persistent.diary_pages = [value["content"] for key, value in persistent.diary_content.items() if value.get("found", False)]
##############################################################################################################