import flet as ft


def main(page: ft.Page):
    btn1 = ft.TextButton(
        text='Editar',
        icon=ft.Icons.EDIT,
        icon_color=ft.Colors.BLUE,
        tooltip='Clique aqui para editar o texto',
        url='https://www.google.com',
        style=ft.ButtonStyle(color=ft.Colors.RED),
        on_click=lambda _: print('Editando o conteúdo...'),
    )

    page.add(btn1)


ft.app(target=main)
