#
# Common styles
#

init offset = -1

style default:
    properties gui.text_properties()
    language gui.language
    outline_scaling "linear"
    outlines [(1, "#000000", 1, 0)]

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline False

style hyperlink_text:
    underline False
    hover_color "#4cf"
    idle_color "#08f"

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar "bar_[prefix_]fill"
    right_bar "bar_[prefix_]empty"

style vbar:
    xsize gui.bar_size
    bottom_bar "bar_[prefix_]fill"
    top_bar "bar_[prefix_]empty"

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("scrollbar_horizontal_[prefix_]bar", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("scrollbar_horizontal_[prefix_]thumb", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("scrollbar_vertical_[prefix_]bar", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("scrollbar_vertical_[prefix_]thumb", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("slider_horizontal_[prefix_]bar", gui.slider_borders, tile=gui.slider_tile)
    thumb "slider_horizontal_[prefix_]thumb"

style vslider:
    xsize gui.slider_size
    base_bar Frame("slider_vertical_[prefix_]bar", gui.vslider_borders, tile=gui.slider_tile)
    thumb "slider_vertical_[prefix_]thumb"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
