import flet as ft


def main(page: ft.Page):
    
    container = ft.Container(
        height=100,
        width=200,
        image='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
        expand=True,
        margin=ft.margin.all(19),
        border=ft.border.all(width=10, color=ft.Colors.RED),
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.Colors.AMBER,
        content=ft.Row(
            ft.ElevatedButton(text='1', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='4', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
        )
    )

    page.add(container)


ft.app(target=main)
