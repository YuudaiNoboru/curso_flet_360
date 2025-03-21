import flet as ft


def main(page: ft.Page):
    # Utilização de Icones.
    icon1 = ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK)
    icon2 = ft.Icon(name=ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN_400, size=50)
    icon3 = ft.Icon(name=ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=80)
    icon4 = ft.Icon(name="settings", color="#C1C1C1", size=100, tooltip="Configurações")

    page.add(icon1, icon2, icon3, icon4)


ft.app(target=main)
