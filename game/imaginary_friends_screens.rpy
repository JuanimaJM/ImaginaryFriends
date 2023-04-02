# Screen for Memories
screen memories():
    tag menu
    add gui.game_menu_background

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle icon_back_arrow
        action Return()
    
    text _("Memories"):
        yalign 0.0
        xalign 0.5
        font font_title
        size gui.title_text_size
    
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.6
        background sugar_plum
        viewport:
            yinitial 0.0
            scrollbars "vertical"
            draggable True
            text lorem
################################################################################

# Screen for Achievements
screen achievements():
    tag menu
    add gui.game_menu_background

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle icon_back_arrow
        action Return()
    
    text _("Achievements"):
        yalign 0.0
        xalign 0.5
        font font_title
        size gui.title_text_size
    
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.6
        background dark_gunmetal
        grid 3 3:
            xfill True
            yfill True
            for key, value in achievement_list.items():
                frame:
                    background transparent
                    hbox:
                        xfill True
                        yfill True
                        spacing 20
                        image identify_image(key):
                                xalign 0.0
                                yalign 0.5
                        vbox:
                            xfill True
                            spacing 10
                            xalign 0.3
                            yalign 0.5
                            text key:
                                color identify_text_color(key)
                                size gui.label_text_size
                            text value:
                                color identify_text_color(key)
                                size gui.notify_text_size
################################################################################

# Screen for Stats
screen stats():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle icon_menu
        action Show("statsUI")

screen statsUI():
    frame:
        xsize 500
        ysize 1080
        xalign 1.0
        padding(20, 20)
        background dark_gunmetal

        imagebutton:
            xalign 1.0
            idle icon_cancel
            action Hide("statsUI")
        
        vbox:
            xsize 500
            yoffset 50
            vbox:
                spacing 10
                text "STATS":
                    xalign 0.5
                    font font_title
                text "Name: Player"
                text "Sanity:"
                bar:
                    range 100
                    value 90
                    xysize(400, 50)
                    left_bar identify_bar_color(90)
                    right_bar white
                text "Happiness:"
                bar:
                    range 100
                    value 20
                    xysize(400, 50)
                    left_bar identify_bar_color(20)
                    right_bar white
            
            frame:
                top_padding 30
                right_padding 30
                bottom_padding 50
                background transparent
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    draggable True
                    vbox:
                        spacing 10
                        box_wrap True
                        text "IMAGINARY FRIENDS":
                            xalign 0.5
                            font font_title
                        text "???1"
                        bar:
                            range 100
                            value 70
                            xysize(400, 50)
                            left_bar identify_bar_color(70)
                            right_bar white
                        text "???2"
                        bar:
                            range 100
                            value 30
                            xysize(400, 50)
                            left_bar identify_bar_color(30)
                            right_bar white
                        text "???3"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        text "???4"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        
                        text "???5"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        
                        text "???6"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        text "???7"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        text "???8"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        
                        text "???9"
                        bar:
                            xysize(400, 50)
                            right_bar white
                        
                        text "???10"
                        bar:
                            xysize(400, 50)
                            right_bar white
################################################################################