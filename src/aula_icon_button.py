import flet as ft


def main(page: ft.Page):
    # Usando icons buttons.

    def play_pause(e: ft.ControlEvent):
        e.control.selected = not e.control.selected
        e.control.update()

    btn1 = ft.IconButton(
        icon=ft.Icons.DELETE_FOREVER_ROUNDED,
        icon_color=ft.Colors.PINK,
        icon_size=100,
        tooltip="Deletear ação",
    )

    btn2 = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE,
        selected_icon=ft.Icons.PAUSE_CIRCLE,
        selected=False,
        icon_size=150,
        on_click=play_pause,
        style=ft.ButtonStyle(
            color={
                ft.ControlState.SELECTED: ft.Colors.WHITE,
                ft.ControlState.DEFAULT: ft.Colors.RED,
            }
        )
    )

    page.add(btn1, btn2)


ft.app(target=main)
