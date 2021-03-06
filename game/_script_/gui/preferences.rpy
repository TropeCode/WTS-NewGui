#
# Preferences screen
#
# The preferences screen allows the player to configure the game to better suit
# themselves.
#
# https://www.renpy.org/doc/html/screen_special.html#preferences

init offset = -1

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):
        style_prefix "pref"

        vbox:
            yoffset -gui.pref_spacing

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # vbox:
                #     style_prefix "radio"
                #     label _("Rollback Side")
                #     textbutton _("Disable") action Preference("rollback side", "disable")
                #     textbutton _("Left") action Preference("rollback side", "left")
                #     textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Interface")
                    textbutton _("Tooltips") action Function(print, "tooltips")
                    textbutton _("Custom Cursor") action Function(print, "custom_cursor")
                    textbutton _("Night Mode") action Function(print, "night_mode")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height (2 * gui.pref_spacing)

            hbox:
                box_wrap True

                vbox:
                    style_prefix "slider"

                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                    label _("Text Scaling")
                    hbox:
                        xalign 0.25
                        textbutton "--" action Preference("font size", 0.6)
                        textbutton "-" action Preference("font size", 0.9)
                        textbutton "Normal" action Preference("font size", 1.0)
                        textbutton "+" action Preference("font size", 1.2)
                        textbutton "++" action Preference("font size", 1.5)

                vbox:
                    style_prefix "slider"

                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                        label _("Weather Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height (2 * gui.pref_spacing)

            hbox:
                box_wrap True

                vbox:
                    style_prefix "check"

                    label _("Text Colour")
                    default color_square = "{size=-0}{font=DejaVuSans.ttf}❖{/font}{/size}"
                    hbox:
                        textbutton "Day Text" size_group "text_colour" action Function(print, "text_day")
                        text "{color=[persistent.text_color_day]}[color_square]{/color}" yalign 0.5
                        textbutton "Reset" text_size 14 yalign 0.5
                    hbox:
                        textbutton "Night Text" size_group "text_colour" action Function(print, "text_night")
                        text "{color=[persistent.text_color_night]}[color_square]{/color}" yalign 0.5
                        textbutton "Reset" text_size 14 yalign 0.5
                    hbox:
                        textbutton "Outline" size_group "text_colour" action Function(print, "text_shadow")

                vbox:
                    style_prefix "check"

                    label _("Advanced")
                    hbox:
                        vbox:
                            textbutton _("Autosave")
                            textbutton _("Confirm Delete")
                            textbutton _("Drawable Resolution")
                        vbox:
                            textbutton "Accessibility {size=-4}{font=[gui.glyph_font]}♿︎{/font}{/size}" action Show("_accessibility")
                            textbutton "Rendering" action Function(renpy.call_in_new_context, "_choose_renderer")
                            textbutton "Full reset" action Confirm(gui.CONFIRM_FULL_RESET, Function(delete_persistent))


define gui.CONFIRM_FULL_RESET = """{color=#f00}Warning!{/color}
This will clear everything except for saves!

{size=-4}Reset persistent data, such as
achievements, seen text, and preferences.{/size}

Are you sure you want to perform a full reset of the game?"""

init python:
    def delete_persistent():
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.quit(relaunch=True)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xminimum 245

style pref_hbox:
    box_wrap_spacing 2 * gui.pref_spacing

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 300

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 368
