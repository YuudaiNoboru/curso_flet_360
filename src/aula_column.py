import flet as ft


def main(page: ft.Page):
    
    column1 = ft.Column(
        controls=[
            ft.ElevatedButton(text='1', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.Colors.AMBER, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.Colors.AMBER, color=ft.Colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.Colors.AMBER, color=ft.Colors.WHITE),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.ALWAYS,
    )

    page.add(column1)


ft.app(target=main)
