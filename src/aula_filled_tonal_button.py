import flet as ft


def main(page: ft.Page):
    # Utilização do Botão Filled Tonal Button
    btn1 = ft.FilledTonalButton(text='Botão secundário')

    page.add(
        btn1,
        ft.FilledTonalButton(text='Botão secundário'),
        ft.FilledTonalButton(text='Botão secundário desabilitado', disabled=True),
        ft.FilledTonalButton(text='Botão secundário com ícone', icon=ft.Icons.ADD),
        ft.FilledTonalButton(text='Botão secundário com ícone', icon=ft.Icons.ADD, icon_color=ft.Colors.GREEN),
        ft.FilledTonalButton(text='Botão secundário', tooltip='Ação não permitida', disabled=True),
        ft.FilledTonalButton(text='Botão com estilo', style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
        )


ft.app(target=main)
