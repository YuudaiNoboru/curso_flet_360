import flet as ft


def main(page: ft.Page):
    # Utilização de Botões FilledButton
    btn1 = ft.FilledButton(text='Botão preenchido')
    btn2 = ft.FilledButton(
        text='Botão com ícone',
        icon=ft.Icons.STAR,
        icon_color=ft.Colors.AMBER,
    )

    style = ft.ButtonStyle(
        padding=50,
        animation_duration=1000,
        side={
            ft.ControlState.DEFAULT: ft.BorderSide(2, ft.Colors.RED),
            ft.ControlState.HOVERED: ft.BorderSide(10, ft.Colors.GREEN)
        },
        shape={
            ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=0),
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=30)
        }
    )

    bt3 = ft.FilledButton(
        text='Botão personalizado',
        style=style
    )

    bt4 = ft.FilledButton(
        text='Botão com link',
        url='http://www.google.com.br',
        tooltip='Google'
    )


    page.add(btn1, btn2, bt3, bt4)


ft.app(target=main)
