from core.technical.repo_manag import tomlm as t; settings = t("settings.toml"); s = settings["General"]; lang = s["language"]
from core.technical.repo_manag import tomlm as t; theme = t("themes/" + s["theme"] + ".toml")
from core.technical.repo_manag import tomlm as t; m = t("init.toml")
from core.technical.repo_manag import dir_lister as repo; accs: list = repo("accounts/")
from core.technical.repo_manag import lang_reader as langtxt
import logging as log
import PySimpleGUI as gui

#--------------|----------------------------------
# THEME        |
#--------------|----------------------------------
tt_text = (theme["Titlebar"])["text_colour"]
tt_back = (theme["Titlebar"])["background_colour"]
mn_text = (theme["Main"])["text_colour"]
mn_back = (theme["Main"])["background_colour"]
mn_butt = (theme["Main"])["button_colour"]
ls_text = (theme["List"])["text_colour"]
ls_back = (theme["List"])["background_colour"]
ls_high = (theme["List"])["highlight_colour"]
ls_txhg = (theme["List"])["text_highlight_colour"]
ls_scrl = (theme["List"])["scroll_colour"]

def runWindow():
    log.info("Initialising window...")
    flayout = [
        [
            gui.Titlebar(m["name"], text_color=tt_text, background_color=tt_back)
        ],
        [
            [gui.Text(langtxt("login__choose_account", lang), text_color=mn_text, background_color=mn_back)],
            [gui.Listbox(
                values=accs, size=(40,20), key=":Accounts",
                text_color=ls_text, background_color=ls_back, highlight_text_color=ls_txhg, highlight_background_color=ls_high
            )],
            [gui.Button(langtxt("login__enter", lang)), gui.Button(langtxt("login__add", lang))]
        ]
    ]
    window = gui.Window(title=m["name"], layout=flayout, margins=(700, 500),
                        background_color=mn_back, button_color=mn_butt,
                        sbar_background_color=ls_scrl, sbar_arrow_color=mn_text)
    return window