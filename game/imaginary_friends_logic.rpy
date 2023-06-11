# Utility Functions
python early:
    import datetime, math

    # Get the current time
    now = datetime.datetime.now().time()

    # Set the start and end times for each period
    dawn_start = datetime.time(5, 30)
    dawn_end = datetime.time(5, 59)
    sunrise_start = datetime.time(6, 0)
    sunrise_end = datetime.time(7, 59)
    morning_start = datetime.time(8, 0)
    morning_end = datetime.time(11, 59)
    noon_start = datetime.time(12, 0)
    noon_end = datetime.time(14, 59)
    afternoon_start = datetime.time(15, 0)
    afternoon_end = datetime.time(16, 59)
    sunset_start = datetime.time(17, 0)
    sunset_end = datetime.time(17, 59)
    dusk_start = datetime.time(18, 0)
    dusk_end = datetime.time(18, 30)
    night_start = datetime.time(18, 31)
    night_end = datetime.time(5, 29)

    def identify_text_color(key):
        if persistent.achievement_list[key]["granted"]:
            return black
        else:
            return gray
    
    def identify_achievement_description(key):
        if persistent.achievement_list[key]["granted"]:
            return persistent.achievement_list[key]["description"]
        else:
            return "???"
    
    def check_time():
        now = datetime.datetime.now().time()
        if dawn_start <= now <= dawn_end:
            store.game_time = 0
        elif sunrise_start <= now <= sunrise_end:
            store.game_time = 1
        elif morning_start <= now <= morning_end:
            store.game_time = 2
        elif noon_start <= now <= noon_end:
            store.game_time = 3
        elif afternoon_start <= now <= afternoon_end:
            store.game_time = 4
        elif sunset_start <= now <= sunset_end:
            store.game_time = 5
        elif dusk_start <= now <= dusk_end:
            store.game_time = 6
        else:
            store.game_time = 7

    def timely_bg_main_menu():
        if game_time == 0:
            # return "images/game_backgrounds/bg_main_menu_dawn.jpg"
            return "animated_bg_main_menu_dawn"
            # return Movie(play="videos/bg_main_menu_dawn.webm")
        elif game_time == 1:
            # return "images/game_backgrounds/bg_main_menu_sunrise.jpg"
            return "animated_bg_main_menu_sunrise"
            # return Movie(play="videos/bg_main_menu_sunrise.webm")
        elif game_time == 2:
            # return "images/game_backgrounds/bg_main_menu_morning.jpg"
            return "animated_bg_main_menu_morning"
            # return Movie(play="videos/bg_main_menu_morning.webm")
        elif game_time == 3:
            # return "images/game_backgrounds/bg_main_menu_noon.jpg"
            return "animated_bg_main_menu_noon"
            # return Movie(play="videos/bg_main_menu_noon.webm")
        elif game_time == 4:
            # return "images/game_backgrounds/bg_main_menu_afternoon.jpg"
            return "animated_bg_main_menu_afternoon"
            # return Movie(play="videos/bg_main_menu_afternoon.webm")
        elif game_time == 5:
            # return "images/game_backgrounds/bg_main_menu_sunset.jpg"
            return "animated_bg_main_menu_sunset"
            # return Movie(play="videos/bg_main_menu_sunset.webm")
        elif game_time == 6:
            # return "images/game_backgrounds/bg_main_menu_dusk.jpg"
            return "animated_bg_main_menu_dusk"
            # return Movie(play="videos/bg_main_menu_dusk.webm")
        elif game_time == 7:
            # return "images/game_backgrounds/bg_main_menu_night.jpg"
            return "animated_bg_main_menu_night"
            # return Movie(play="videos/bg_main_menu_night.webm")
           
    
    def timely_bg_game_menu():
        if game_time == 0:
            # return "images/game_backgrounds/bg_game_menu_dawn.jpg"
            return "animated_bg_game_menu_dawn"
            # return Movie(play="videos/bg_game_menu_dawn.webm")
        elif game_time == 1:
            # return "images/game_backgrounds/bg_game_menu_sunrise.jpg"
            return "animated_bg_game_menu_sunrise"
            # return Movie(play="videos/bg_game_menu_sunrise.webm")
        elif game_time == 2:
            # return "images/game_backgrounds/bg_game_menu_morning.jpg"
            return "animated_bg_game_menu_morning"
            # return Movie(play="videos/bg_game_menu_morning.webm")
        elif game_time == 3:
            # return "images/game_backgrounds/bg_game_menu_noon.jpg"
            return "animated_bg_game_menu_noon"
            # return Movie(play="videos/bg_game_menu_noon.webm")
        elif game_time == 4:
            # return "images/game_backgrounds/bg_game_menu_afternoon.jpg"
            return "animated_bg_game_menu_afternoon"
            # return Movie(play="videos/bg_game_menu_afternoon.webm")
        elif game_time == 5:
            # return "images/game_backgrounds/bg_game_menu_sunset.jpg"
            return "animated_bg_game_menu_sunset"
            # return Movie(play="videos/bg_game_menu_sunset.webm")
        elif game_time == 6:
            # return "images/game_backgrounds/bg_game_menu_dusk.jpg"
            return "animated_bg_game_menu_dusk"
            # return Movie(play="videos/bg_game_menu_dusk.webm")
        elif game_time == 7:
            # return "images/game_backgrounds/bg_game_menu_night.jpg"
            return "animated_bg_game_menu_night"
            # return Movie(play="videos/bg_game_menu_night.webm")
    
    def timely_text_color():
        if game_time >= 6:
            return white
        else:
            return dark_gunmetal
    
    def timely_icon_diary():
        if game_time >= 6:
            return icon_diary_white
        else:
            return icon_diary_black
    
    def timely_icon_achievement():
        if game_time >= 6:
            return icon_achievement_white
        else:
            return icon_achievement_black
    
    def timely_img_apple():
        if game_time == 7:
            return im.Blur(img_black_apple, 0.5)
        else:
            return img_black_apple
    
    def has_next_page():
        return (second_page < len(persistent.diary_pages))
    
    def has_back_page():
        return (first_page >= 3) and (len(persistent.diary_pages) >= 3)
    
    def identify_second_page():
        if first_page < len(persistent.diary_pages):
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

    def notify_achievement(key):
        title = persistent.achievement_list[key]["title"]
        renpy.display_notify(f"You achieve the \"{title}\"")
##############################################################################################################

# Game Functions
python early:
    def update_player_stats(variable_name, value):
        value = max(0, min(value, 100))  # Enforce limits of 0 and 100
        globals()[variable_name] = value

    def grant_achievement(key):
        if not persistent.achievement_list[key]["granted"]:
            persistent.achievement_list[key]["granted"] = True
            refresh_achievements()
            notify_achievement(key)
    
    def refresh_achievements():
        sorted_achievements.clear()
        sorted_achievements.update({k: v for k, v in sorted(persistent.achievement_list.items(), key=lambda x: (not x[1]["granted"], x[0]))})

    def refresh_diary():
        for value in persistent.diary_content.values():
            if (value["found"]) and not (value["content"] in persistent.diary_pages):
                persistent.diary_pages.append(value["content"])
    
    def update_friends_stats(character, value):
        value = max(0, min(value, 100))  # Enforce limits of 0 and 100
        friends_stats[character]["stats"] += value
        return friends_stats[character]["stats"]
    
    def meet_friend(character):
        friends_stats[character]["meet"] = True
    
    def write_diary(key):
        persistent.diary_content[key]["found"] = True
        refresh_diary()
    
    def random_name():
        return random.choice(name_list)
##############################################################################################################

# Developer Options
python early:
    import random

    def developer_mode():
        renpy.config.always_shown_screens.append("developer")
    
    def delete_persistent():
        persistent._clear(True)
        renpy.reload_script()
    
    def modify_achievements(granted):
        for achievement in persistent.achievement_list.values():
            achievement["granted"] = granted

    def grant_all_achievements():
        modify_achievements(True)

    def randomly_grant_achievement():
        keys_with_false = [key for key, value in persistent.achievement_list.items() if not value["granted"]]
        if keys_with_false:
            random_key = random.choice(keys_with_false)
            persistent.achievement_list[random_key]["granted"] = True
            refresh_achievements()
            notify_achievement(random_key)

    def remove_all_achievements():
        modify_achievements(False)

    def modify_diary_pages(found):
        for value in persistent.diary_content.values():
            value["found"] = found
            refresh_diary()

    def write_all_diary_pages():
        modify_diary_pages(True)

    def randomly_write_diary():
        keys_with_false = [key for key, value in persistent.diary_content.items() if not value["found"]]
        if keys_with_false:
            random_key = random.choice(keys_with_false)
            persistent.diary_content[random_key]["found"] = True
        refresh_diary()

    def remove_all_diary_pages():
        modify_diary_pages(False)
        persistent.diary_pages.clear()
        store.first_page = 1
        store.second_page = 2

    def set_random_name():
        store.default_name = random_name()
##############################################################################################################

# Color Spectrum
python early:
    class ColorSpectrum:
        def __init__(self, number):
            self.number = max(0, min(number, 100))  # Enforce limits of 0 and 100
        
        def get_color_spectrum(self):
            if self.number >= 51:
                start_color = pastel_yellow
                end_color = pastel_green
                start_percentage = 51
                end_percentage = 100
            else:
                start_color = pastel_red
                end_color = pastel_yellow
                start_percentage = 1
                end_percentage = 50
            percentage = (self.number - start_percentage) / (end_percentage - start_percentage)
            color = self._blend_colors(start_color, end_color, percentage)
            return color
        
        def _blend_colors(self, start_color, end_color, percentage):
            r1, g1, b1 = self._hex_to_rgb(start_color)
            r2, g2, b2 = self._hex_to_rgb(end_color)
            r = int(r1 + (r2 - r1) * percentage)
            g = int(g1 + (g2 - g1) * percentage)
            b = int(b1 + (b2 - b1) * percentage)
            blended_color = self._rgb_to_hex((r, g, b))
            return blended_color
        
        def _hex_to_rgb(self, hex_color):
            hex_color = hex_color.lstrip("#")
            return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        
        def _rgb_to_hex(self, rgb_color):
            r, g, b = rgb_color
            return f"#{r:02x}{g:02x}{b:02x}"
"""
The code defines a class called ColorSpectrum.

The get_color_spectrum method is a public method of the ColorSpectrum class. 

It takes a number as input and returns a color based on that number.

Inside the get_color_spectrum method, an if-else statement is used to determine the color based on the value of the number.

If the number is greater than or equal to 51, the start color is set to pastel_yellow, the end color is set to pastel_green, and the start and end percentages are set to 51 and 100, respectively.

Otherwise, if the number is less than 51, the start color is set to pastel_red, the end color is set to pastel_yellow, and the start and end percentages are set to 1 and 50, respectively.

The percentage is calculated by subtracting the start percentage from the number and dividing it by the difference between the start and end percentages. 

This calculates how far the number is between the start and end range.

The _blend_colors method is a private method of the ColorSpectrum class. 

It takes the start color, end color, and percentage as input and blends the colors based on the percentage.

Inside the _blend_colors method, the start and end colors are converted from hexadecimal to RGB values using the _hex_to_rgb method.

The RGB values of the blended color are calculated by interpolating between the start and end colors based on the percentage.

The _rgb_to_hex method is a private method of the ColorSpectrum class. 

It takes RGB values as input and converts them back to a hexadecimal color code.

Finally, the blended color is returned as the result of the get_color_spectrum method.
"""
##############################################################################################################