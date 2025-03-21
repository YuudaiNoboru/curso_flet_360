import flet as ft


def main(page: ft.Page):

    # Botão Floating Action Button (FAT)
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        bgcolor=ft.Colors.GREEN,
        mini=False, # True para botão pequeno
        shape=ft.RoundedRectangleBorder(radius=10),
        tooltip='Cadastrar um novo produto',
        # text='Adicionar', # Não é comum, mas é possivel adicionar texto
        on_click=lambda _: print('Fui Clicada'),
    )

    page.update()


ft.app(target=main)
