import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size

from adviento_web.views.navbar import navbar
from adviento_web.views.header import header
from adviento_web.views.instructions import instructions
from adviento_web.views.calendar import calendar
from adviento_web.views.author import author
from adviento_web.views.partners import partners
from adviento_web.views.github import github
from adviento_web.views.footer import footer


def index() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src = "js/snow.js"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                calendar(),
                author(),
                partners(),
                github(),
                footer(),
                spacing = "5",
            ),
            width = "100%",
            align_items = "center",
        ),
    )





app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLE,
)

app.add_page(
    index,
    title = "Calendario de aDEViento 2024 | 24 días. 24 regalos.",
    description = "Calendario de adviento de mouredev"
)
