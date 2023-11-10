import os
import json

qtile_path = os.path.join(os.path.expanduser("~"), ".config", "qtile")
qtile_scripts = os.path.join(qtile_path, "scripts")


def getenv(key): return json.load(open(f"{qtile_path}/.env", "r"))[key]

terminal = getenv("console")
font = getenv("font")
mail = getenv("mail")


def theme_selector(theme=getenv("theme")):
    qtile_themes = os.path.join(qtile_path, "themes")
    try:
        with open(os.path.join(qtile_themes, "themes.json")) as f:
            return json.load(f)[theme]
    except:
        try:
            with open(os.path.join(qtile_themes, f"{theme}.json")) as g:
                return json.load(g)
        except:
            pass

    return {"background": "#0f101a", "foreground": "#f1ffff", "active": "#f1ffff", "inactive": "#4c566a", "color1": "#a151d3", "color2": "#F07178", "color3": "#fb9f7f", "color4": "#ffd47e"}


theme = theme_selector()