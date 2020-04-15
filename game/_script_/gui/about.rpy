## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

init offset = -1

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            spacing 20

            label "[config.name!t]"
            #text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") size 12


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


style smallcredits:
    size 14
    color "#808080"
    kerning 0.7

define gui.about = """Witch Trainer Silver is a complete rework of Akabur's game, Witch Trainer.

It combines several mods for Witch Trainer into one game, with new features, bugfixes, improvements, events, and new art being added periodically.

The game is developed by {a=https://www.patreon.com/SilverStudioGames}Silver Studio Games{/a}, which is a group of people from around the world who work on it in their free time.

Current team{=smallcredits}
MadMerlin
Soggy
Johnny
LoafyLemon
TropeCode
CyniclePickle{/=smallcredits}

Special thanks to {a=https://www.patreon.com/akabur}Akabur{/a}
{=smallcredits}Creator of the original Witch Trainer and other awesome games!{/=smallcredits}
"""
