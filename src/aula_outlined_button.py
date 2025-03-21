import flet as ft


def main(page: ft.Page):
    # Usando Outlined Button.
    btn1 = ft.OutlinedButton(
        text='Botão terciário',
        icon=ft.icons.ZOOM_IN,
        icon_color=ft.Colors.TEAL,
        tooltip='Clique aqui',
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
        url='https://google.com.br',
        on_click=lambda _: print('Fui clicado')
    )

    page.add(btn1)


ft.app(target=main)
