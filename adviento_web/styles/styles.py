import reflex as rx
from .fonts import Font
from .colors import TextColor
from .colors import Color
from enum import Enum

MAX_WIDTH = "1000px"

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap", # &display=swap: Para acelerar la descarga de la fuente
    #"https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.ACCENT.value,
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none",
        }
    },
    rx.chakra.span: {
        "font_size": Size.MEDIUM.value,
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {
            "color": f"{TextColor.PRIMARY.value} !important",
        }
    }
}

max_width_style = dict(
    align_items = "start",
    padding_x = Size.BIG.value,
    width = "100%",
    max_width = MAX_WIDTH,
)