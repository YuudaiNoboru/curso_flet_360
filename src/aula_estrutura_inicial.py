import flet as ft


def main(page: ft.Page):
    mensage = ft.Text(value="Olá Mundo!")
    page.add(mensage)

    page.add(ft.Text(value="Meu nome é Lucas"))

    page.add(ft.Text(value="Texto 1"), ft.Text(value="Texto 2"))

    elementos = [
        ft.Text(value="Elemento 1"),
        ft.Text(value="Elemento 4"),
        ft.Text(value="Elemento 3"),
        ft.Text(value="Elemento 4"),
        ft.Text(value="Elemento 5"),
    ]

    page.add(*elementos)


ft.app(target=main)

# class App:
#     def __init__(self, page: ft.Page):
#         pass


# ft.app(target=App)
