import reflex as rx
import adviento_web.styles.styles as styles
import adviento_web.styles.constants as constants
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color

def github() -> rx.Component:
    return rx.link(
            rx.vstack(
                rx.vstack(
                    rx.chakra.span(
                        "Proyecto ",
                    ),
                    rx.chakra.span(
                        "en GitHub",
                    ),
                    align_items = "start",
                    class_name = "nes-balloon from-right is-dark",
                    margin_bottom = Size.BIG.value,
                ),
                rx.box(
                    rx.chakra.span(
                        constants.VERSION,
                        class_name = "is-error",
                    ),
                    class_name = "nes-badge",
                ),
                #width = "100%",
            ),
            rx.box(
                class_name = "nes-octocat animate",
                #margin_top = Size.BIG.value,
            ),
        href = constants.GITHUB_REPO_URL,
        is_external = True,   
        margin_top = Size.ZERO.value,
        width = "100%",
        align_items = "center",
        display = "flex",
    )