# Utility Functions
python early:
    import datetime
    
    def identify_bar_color(value):
        if value > 80:
            return electric_green
        elif value > 60 and value < 80:
            return mango_green
        elif value > 40 and value < 60:
            return lemon_glacier
        elif value > 20 and value < 40:
            return american_orange
        else:
            return red

    def identify_image(key):
        if achievement_values.get(key):
            return img_badge
        else:
            return im.MatrixColor(img_badge, im.matrix.desaturate())
    
    def identify_text_color(key):
        if achievement_values.get(key):
            return white
        else:
            return gray
    
    def gui_path(file):
        return "gui/imaginary_friends/" + file
    
    def timely_bg():
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

        if sunrise_start <= now <= sunrise_end:
            return gui_path("bg_main_menu_sunrise.jpg")
        elif morning_start <= now <= morning_end:
            return gui_path("bg_main_menu_morning.jpg")
        elif afternoon_start <= now <= afternoon_end:
            return gui_path("bg_main_menu_afternoon.jpg")
        elif sunset_start <= now <= sunset_end:
            return gui_path("bg_main_menu_sunset.jpg")
        else:
            return gui_path("bg_main_menu_night.jpg")
################################################################################

# Game Functions
python early:
    def grant_achievement(title):
        achievement_values[title] = True
        renpy.display_notify(f"You achieve the {title} achievement")
    
    def update_friends_stats(character, value):
        friends_stats[character] += value
        return friends_stats[character]
################################################################################