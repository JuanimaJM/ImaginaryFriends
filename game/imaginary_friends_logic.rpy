# Utility Functions
python early:
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