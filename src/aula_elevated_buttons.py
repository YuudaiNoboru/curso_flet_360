import flet as ft


def main(page: ft.Page):
    page.spacing = 50

    # Utilização de Botões.

    style = ft.ButtonStyle(
        color={
            ft.ControlState.HOVERED: ft.Colors.WHITE,
            ft.ControlState.DEFAULT: ft.Colors.BLACK,
        },
        bgcolor={
            ft.ControlState.HOVERED: ft.Colors.PINK,
            ft.ControlState.DISABLED: ft.Colors.GREEN,
            ft.ControlState.FOCUSED: ft.Colors.RED,
            "": ft.Colors.AMBER,
        },
        padding={
            ft.ControlState.HOVERED: 20,
            ft.ControlState.DEFAULT: 10,
        },
        animation_duration=1000,
        side={
            ft.ControlState.HOVERED: ft.BorderSide(width=1, color=ft.Colors.BLUE),
            ft.ControlState.DEFAULT: ft.BorderSide(width=5, color=ft.Colors.ORANGE_600),
        },
        shape={
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=10),
            ft.ControlState.DEFAULT: ft.ContinuousRectangleBorder(radius=20),
        },
    )

    btn1 = ft.ElevatedButton(text="Clique aqui")
    btn2 = ft.ElevatedButton(text="Botão inativo", disabled=True)
    btn3 = ft.ElevatedButton(text="Botão inativo", icon=ft.Icons.FAVORITE)
    btn4 = ft.ElevatedButton(
        text="Botão inativo",
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE,
        icon=ft.Icons.FAVORITE_BORDER,
        icon_color=ft.Colors.WHITE,
        tooltip="Favorito",
        url="http://www.google.com.br",
    )

    text = ft.Text()

    def button_click(e: ft.ControlEvent):
        e.control.data += 1
        text.value = f"Botão clicado {e.control.data} vezes"
        text.update()
        e.control.update()

    btn6 = ft.ElevatedButton(text="Clique", on_click=button_click, data=0)

    btn5 = ft.ElevatedButton(
        text="Personalisado", style=style, data=10, on_click=button_click
    )

    page.add(btn1, btn2, btn3, btn4, btn5, btn6, text)


ft.app(target=main)
