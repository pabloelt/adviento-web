import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color

def day(number: int, image: str = "gift.png", url: str = "") -> rx.Component:
    return rx.box(
        rx.cond(
            url != "",
            rx.link(
                rx.image(
                    src = image,
                    alt = f"Regalo asociado al día {number}",                  
                ),
                href = url,
                is_external = True,
                position = "absolute",
            )
        ),
        rx.cond(
            url == "",
            rx.link(
                rx.image(
                    src = image,
                    alt = f"Regalo asociado al día {number}",
                    position = "absolute",                  
                )            
            )
        ),
        rx.text(
            number,
            padding = Size.DEFAULT.value,
            position = "absolute",
        ),
        bg = Color.ACCENT.value,
        width = "100%",
        aspect_ratio = "1",
        position = "relative",
    )