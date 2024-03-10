import reflex as rx
from adviento_web.styles.styles import Size

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name = f"nes-icon {icon} is-small",
        href = url,
        is_external = True,
    )