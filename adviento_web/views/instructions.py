import reflex as rx
import adviento_web.styles.styles as styles
from adviento_web.styles.styles import Size
from adviento_web.styles.colors import Color, TextColor
from adviento_web.components.button import button
import adviento_web.styles.constants as constants

def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo funciona el evento?",
                class_name = "title",
                color = f"{TextColor.ACCENT.value} !important",
                ),
            rx.chakra.span("· Del 1 al 24 de diciembre descubriré cada día un nuevo regalo en el calendario."),
            rx.chakra.span("· Puedes participar desde cualquier parte del mundo."),
            rx.chakra.span("· Sólo tendrás que hacer Retweet a la publicación que enlazaré desde esta web."),
            button(
                "Twitter",
                constants.TWITTER_URL,
            ),
            rx.chakra.span("· Al día siguiente realizaré el sorteo de forma pública en directo desde Twitch."),
            button(
                "Twitch",
                constants.TWITCH_URL,
            ),
            rx.chakra.span("· ¡Vuelta a empezar! Publicaré un nuevo regalo y comenzará de nuevo el proceso."),
            class_name = "nes-container is-dark with-title",
            align_items = "start",
            width = "100%",
        ),
        style = styles.max_width_style,
    )