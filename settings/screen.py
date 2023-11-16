from libqtile import layout, bar
from libqtile.config import Screen, Group, Match

from .widgets import init_widgets_list
from .manager import theme, Theme

screens = [Screen(top=bar.Bar(widgets=init_widgets_list(), size=28))]

layout_theme = {
    "margin"        : 4,
    "border_width"  : 2,
    "border_focus"  : theme[Theme.active],
    "border_normal" : theme[Theme.inactive],
}
layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]

floating_types = ["notification", "toolbar", "splash", "dialog"]
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
    ],
    border_normal=theme[Theme.inactive],
    border_focus=theme[Theme.active],
)


def group(group_labels):
    group = []
    group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(group_names)):
        group.append(Group(name=group_names[i], label=group_labels[i]))
    return group


groups = group(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"])
