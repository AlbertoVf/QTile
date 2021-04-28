import json
from settings.path import qtile_themes, qtile_path
from os import path


def theme_selector():
    tema: str
    with open(f"{qtile_path}/theme.json") as f:
        theme = json.load(f)["theme"]
        tema = str(theme)

    with open(f"{qtile_themes}/{tema}.json") as themes:
        for colors in json.load(themes)[tema]:
            return {
                "dark": colors["dark"],
                "grey": colors["grey"],
                "light": colors["light"],
                "text": colors["text"],
                "focus": colors["focus"],
                "active": colors["active"],
                "inactive": colors["inactive"],
                "urgent": colors["urgent"],
                "color1": colors["color1"],
                "color2": colors["color2"],
                "color3": colors["color3"],
                "color4": colors["color4"],
            }
