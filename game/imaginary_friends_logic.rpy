# Utility Functions
python early:
    import datetime, math

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
    
    # def identify_bar_color(value):
    #     if value >= 80:
    #         return bar_green
    #     elif value >= 60 and value < 80:
    #         return bar_yellowgreen
    #     elif value >= 40 and value < 60:
    #         return bar_yellow
    #     elif value >= 20 and value < 40:
    #         return bar_orange
    #     else:
    #         return bar_red

    def identify_text_color(key):
        if achievement_list[key]["granted"]:
            return black
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
            return "images/game_backgrounds/bg_main_menu_sunrise.jpg"
        elif morning_start <= now <= morning_end:
            return "images/game_backgrounds/bg_main_menu_morning.jpg"
        elif afternoon_start <= now <= afternoon_end:
            return "images/game_backgrounds/bg_main_menu_afternoon.jpg"
        elif sunset_start <= now <= sunset_end:
            return "images/game_backgrounds/bg_main_menu_sunset.jpg"
        else:
            # return "images/game_backgrounds/bg_main_menu_night.png")
            # return Movie(play="videos/bg_main_menu.webm")
            return "animated_bg_main_menu_night"
    
    def timely_text_color():
        if is_sky_dark():
            return white
        else:
            return sugar_plum
    
    def timely_icon_diary():
        if is_sky_dark():
            return icon_diary_white
        else:
            return icon_diary_black
    
    def timely_icon_achievement():
        if is_sky_dark():
            return icon_achievement_white
        else:
            return icon_achievement_black
    
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

    def calculate_rows(columns,list):
        return math.ceil(len(list) / columns)
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

# Debugging
python early:
    import random

    def start_debug():
        renpy.config.always_shown_screens.append("debug")
    
    def modify_achievements(granted):
        for achievement in achievement_list.values():
            achievement["granted"] = granted

    def grant_all_achievements():
        modify_achievements(True)

    def randomly_grant_achievement():
        keys_with_false = [key for key, value in achievement_list.items() if not value["granted"]]
        if keys_with_false:
            random_key = random.choice(keys_with_false)
            achievement_list[random_key]["granted"] = True

    def remove_all_achievements():
        modify_achievements(False)

    def modify_diary_pages(found):
        for value in diary_content.values():
            value["found"] = found
            refresh_diary()
    
    def refresh_diary():
        for value in diary_content.values():
            if (value["found"]) and not (value["content"] in diary_pages):
                diary_pages.append(value["content"])

    def write_all_diary_pages():
        modify_diary_pages(True)

    def randomly_write_diary():
        keys_with_false = [key for key, value in diary_content.items() if not value["found"]]
        if keys_with_false:
            random_key = random.choice(keys_with_false)
            diary_content[random_key]["found"] = True
        refresh_diary()

    def remove_all_diary_pages():
        modify_diary_pages(False)
        diary_pages.clear()
        store.first_page = 1
        store.second_page = 2
##############################################################################################################

# Color Spectrum
python early:
    class ColorSpectrum:
        def get_color_spectrum(number):
            if number >= 50:
                start_color = "#FAFF00"  # Lemon Glacier
                end_color = "#00FF00"  # Electric Green
                start_percentage = 50
                end_percentage = 100
            # elif 60 <= number < 80:
            #     start_color = "#FAFF00"  # Lemon Glacier
            #     end_color = "#8EFD00"  # Mango Green
            #     start_percentage = 60
            #     end_percentage = 79
            # elif 40 <= number < 60:
            #     start_color = "#FF8A00"  # American Orange
            #     end_color = "#FAFF00"  # Lemon Glacier
            #     start_percentage = 40
            #     end_percentage = 59
            # elif 20 <= number < 40:
            #     start_color = "#FF0000"  # Red
            #     end_color = "#FF8A00"  # American Orange
            #     start_percentage = 20
            #     end_percentage = 39
            else:
                start_color = "#FF0000"  # Red
                end_color = "#FAFF00"  # Lemon Glacier
                start_percentage = 1
                end_percentage = 49
            percentage = (number - start_percentage) / (end_percentage - start_percentage)
            color = ColorSpectrum._blend_colors(start_color, end_color, percentage)
            return color
        
        def _blend_colors(start_color, end_color, percentage):
            r1, g1, b1 = ColorSpectrum._hex_to_rgb(start_color)
            r2, g2, b2 = ColorSpectrum._hex_to_rgb(end_color)
            r = int(r1 + (r2 - r1) * percentage)
            g = int(g1 + (g2 - g1) * percentage)
            b = int(b1 + (b2 - b1) * percentage)
            blended_color = ColorSpectrum._rgb_to_hex((r, g, b))
            return blended_color
        
        def _hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip("#")
            return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        
        def _rgb_to_hex(rgb_color):
            r, g, b = rgb_color
            return f"#{r:02x}{g:02x}{b:02x}"
##############################################################################################################