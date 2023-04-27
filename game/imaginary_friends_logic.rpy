# Utility Functions
python early:
    import datetime

    # Get the current time
    now = datetime.datetime.now().time()

    # Set the start and end times for each period
    sunrise_start = datetime.time(6, 0)
    sunrise_end = datetime.time(6, 59)
    morning_start = datetime.time(7, 0)
    morning_end = datetime.time(11, 59)
    afternoon_start = datetime.time(12, 0)
    afternoon_end = datetime.time(15, 59)
    sunset_start = datetime.time(16, 0)
    sunset_end = datetime.time(17, 59)
    night_start = datetime.time(18, 0)
    night_end = datetime.time(5, 59)

    now = night_start

    def gui_path(file):
        return "gui/imaginary_friends/" + file
    
    def identify_bar_color(value):
        if value > 80:
            return bar_green
        elif value > 60 and value < 80:
            return bar_yellowgreen
        elif value > 40 and value < 60:
            return bar_yellow
        elif value > 20 and value < 40:
            return bar_orange
        else:
            return bar_red

    def identify_text_color(key):
        if achievement_list[key]["granted"]:
            return  white
        else:
            return gray
    
    def identify_achievement_description(key):
        if achievement_list[key]["granted"]:
            return achievement_list[key]["description"]
        else:
            return "???"

    def is_sky_dark():
        return not (sunrise_start <= now <= afternoon_end)

    def timely_bg():
        if sunrise_start <= now <= sunrise_end:
            return gui_path("bg_main_menu_sunrise.jpg")
        elif morning_start <= now <= morning_end:
            return gui_path("bg_main_menu_morning.jpg")
        elif afternoon_start <= now <= afternoon_end:
            return gui_path("bg_main_menu_afternoon.jpg")
        elif sunset_start <= now <= sunset_end:
            return gui_path("bg_main_menu_sunset.jpg")
        else:
            # return gui_path("bg_main_menu_night.jpg")
            return Movie(play=gui_path("bg_main_menu.webm"))
    
    def timely_text_color():
        if is_sky_dark():
            return white
        else:
            return sugar_plum
    
    def timely_icon_diary():
        if is_sky_dark():
            return gui_path("ic_diary_white.png")
        else:
            return gui_path("ic_diary_black.png")
    
    def timely_icon_achievement():
        if is_sky_dark():
            return gui_path("ic_achievement_white.png")
        else:
            return gui_path("ic_achievement_black.png")
    
    def has_next_page():
        return (second_page < len(diary_pages))
    
    def has_back_page():
        return (first_page >= 3) and (len(diary_pages) >= 3)
    
    def identify_second_page():
        if first_page < len(diary_pages):
            return True
        else:
            return False
    
    def next_page():
        store.first_page += 2
        store.second_page += 2
    
    def back_page():
        store.first_page -= 2
        store.second_page -= 2
    
    def identify_character(key):
        if friends_stats[key]["meet"]:
            return key
        else:
            return "???"
##############################################################################################################

# Game Functions
python early:
    def grant_achievement(key):
        if not achievement_list[key]["granted"]:
            achievement_list[key]["granted"] = True
            title = achievement_list[key]["title"]
            renpy.display_notify(f"You achieve the {title}")
        return renpy.say(None, "You get some achievement")
    
    def update_friends_stats(character, value):
        friends_stats[character]["stats"] += value
        return friends_stats[character]["stats"]
    
    def meet_friend(character):
        friends_stats[character]["meet"] = True
    
    def write_diary(key):
        diary_content[key]["found"] = True
        if (diary_content[key]["found"]) and not (diary_content[key]["content"] in diary_pages):
            diary_pages.append(diary_content[key]["content"])
##############################################################################################################