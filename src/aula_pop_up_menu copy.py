import flet as ft


def main(page: ft.Page):
    def check_item_clicked(e: ft.ControlEvent):
        e.control.checked = not e.control.checked
        e.control.update()

    # Opções do PopupMenuButton
    pb = ft.PopupMenuButton(
        icon=ft.Icons.MENU_BOOK,
        items=[
            ft.PopupMenuItem(text="Item 1"),
            ft.PopupMenuItem(text="Item 2", icon=ft.Icons.POWER_INPUT),
            ft.PopupMenuItem(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.NOTIFICATION_IMPORTANT),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value="Lucas gostaria de enviar uma menssagem para você.",
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                ft.Text(
                                    value="Olá, tudo bem? Como está indo os estudos de Flet ? Espero que esteja gostando do curso.",
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                            ],
                            width=200,
                        ),
                    ]
                ),
                on_click=lambda _: print('Fui clicada')
            ),
            ft.PopupMenuItem(), # Quando em branco, funciona como um separador
            ft.PopupMenuItem(text='Item 3'),
            ft.PopupMenuItem(text='Item 4', checked=False, on_click=check_item_clicked),
        ],
    )

    page.add(pb)


ft.app(target=main)
