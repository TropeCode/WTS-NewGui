#
# GUI images
#

image game_menu:
    contains:
        zoom 0.5
        "gui/main_menu/00.png"
        pause 3
        "gui/main_menu/01.png"
        pause.1
        "gui/main_menu/02.png"
        pause.1
        "gui/main_menu/01.png"
        pause.1
        "gui/main_menu/00.png"
        pause 6
        "gui/main_menu/01.png"
        pause.1
        "gui/main_menu/02b.png"
        pause.1
        "gui/main_menu/01b.png"
        pause.1
        "gui/main_menu/00b.png"
        pause 3
        "gui/main_menu/01b.png"
        pause.1
        "gui/main_menu/02b.png"
        pause.1
        "gui/main_menu/01b.png"
        pause.1
        "gui/main_menu/00b.png"
        pause 6
        "gui/main_menu/01b.png"
        pause.1
        "gui/main_menu/02b.png"
        pause.1
        "gui/main_menu/02.png"
        pause.1
        "gui/main_menu/01.png"
        pause.1
        repeat

    contains:
        xpos -17
        ypos -151
        zoom 2.0
        "candle_fire"

    contains:
        xpos -255
        ypos 100
        zoom 0.8
        "gui/main_menu/fire00.png"
        pause.1
        "gui/main_menu/fire01.png"
        pause.1
        "gui/main_menu/fire02.png"
        pause.1
        "gui/main_menu/fire03.png"
        pause.1
        "gui/main_menu/fire04.png"
        pause.1
        "gui/main_menu/fire05.png"
        pause.1
        "gui/main_menu/fire06.png"
        pause.1
        "gui/main_menu/fire07.png"
        pause.1
        repeat

image main_menu:
    contains:
        "game_menu"

    # contains:
    #     xalign 1.0
    #     yalign 0.5
    #     xoffset -210
    #     "game_title"

image game_title:
    size (339, 242)

    contains:
        #zoom 0.9
        "gui/logos/title.png"

    #TODO Add sparkle to game logo
    # #sparkle
    # contains:
    #     subpixel True
    #     xpos 798-682
    #     ypos 200
    #     xanchor 0.5
    #     yanchor 0.5
    #     zoom 0.0
    #     "gui/main_menu/sparkle.png"
    #     linear 0.8 zoom 1.0
    #     linear 0.5 zoom 0.0
    #     pause 5
    #     repeat

    # #shine silver (synchronized)
    # contains:
    #     subpixel True
    #     xpos 848-682
    #     ypos 230-12
    #     xanchor 0.5
    #     yanchor 0.5
    #     zoom 0.0
    #     "gui/main_menu/sparkle.png"
    #     pause 1.3
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 870-682
    #     ypos 205-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 914-682
    #     ypos 227-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 948-682
    #     ypos 233-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0

    #     xpos 999-682
    #     ypos 226-12
    #     linear 0.5 zoom 1.0
    #     linear 0.5 zoom 0.0
    #     pause 12.6
    #     repeat

image candle_fire:
    "gui/main_menu/candle/fire_01.png"
    pause.1
    "gui/main_menu/candle/fire_02.png"
    pause.1
    "gui/main_menu/candle/fire_03.png"
    pause.1
    "gui/main_menu/candle/fire_04.png"
    pause.1
    "gui/main_menu/candle/fire_05.png"
    pause.1
    "gui/main_menu/candle/fire_06.png"
    pause.1
    "gui/main_menu/candle/fire_07.png"
    pause.1
    "gui/main_menu/candle/fire_08.png"
    pause.1
    "gui/main_menu/candle/fire_09.png"
    pause.1
    "gui/main_menu/candle/fire_10.png"
    pause.1
    repeat

image discord_idle:
    zoom 0.5
    alpha 0.5
    "gui/logos/discord.png"

image discord_hover:
    zoom 0.55
    "gui/logos/discord.png"

image patreon_idle:
    zoom 0.5
    alpha 0.5
    "gui/logos/patreon.png"

image patreon_hover:
    zoom 0.55
    "gui/logos/patreon.png"

image silverstudiogames_idle:
    zoom 0.5
    alpha 0.5
    "gui/logos/silverstudiogames.png"

image silverstudiogames_hover:
    zoom 0.55
    "gui/logos/silverstudiogames.png"


# Sliders

image slider_horizontal_idle_thumb = Solid(gui.idle_color, xsize=gui.thumb_size)

image slider_horizontal_hover_thumb = Solid(gui.hover_color, xsize=gui.thumb_size)

image slider_horizontal_idle_bar = Solid(gui.muted_color)

image slider_horizontal_hover_bar = Solid(gui.hover_muted_color)

image slider_vertical_idle_thumb = Solid(gui.idle_color, ysize=gui.thumb_size)

image slider_vertical_hover_thumb = Solid(gui.hover_color, ysize=gui.thumb_size)

image slider_vertical_idle_bar = Solid(gui.muted_color)

image slider_vertical_hover_bar = Solid(gui.hover_muted_color)


# Scrollbars

image scrollbar_horizontal_idle_thumb = Solid(gui.accent_color)

image scrollbar_horizontal_hover_thumb = Solid(gui.hover_color)

image scrollbar_horizontal_idle_bar = Solid(gui.muted_color)

image scrollbar_horizontal_hover_bar = Solid(gui.hover_muted_color)

image scrollbar_vertical_idle_thumb = Solid(gui.accent_color)

image scrollbar_vertical_hover_thumb = Solid(gui.hover_color)

image scrollbar_vertical_idle_bar = Solid(gui.muted_color)

image scrollbar_vertical_hover_bar = Solid(gui.hover_muted_color)


# Bars

image bar_idle_fill = Solid(gui.idle_color)

image bar_hover_fill = Solid(gui.hover_color)

image bar_idle_empty = Solid(gui.muted_color)

image bar_hover_empty = Solid(gui.hover_muted_color)
