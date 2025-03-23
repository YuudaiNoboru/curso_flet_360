import flet as ft


def main(page: ft.Page):
    page.padding = ft.padding.only(top=100)

    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(text=1, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text=1, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ft.ElevatedButton(text=1, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
        ],
        alignment=ft.MainAxisAlignment.CENTER, # Alinhamento do elementos na row.
        spacing=20, # Espaçamento entre os elementos na row.
        wrap=True, # Ativa a quebra de linha para caso o conteudo passe dos limites da janela.
        run_spacing=20, # Espaçamento entre as linhas que foram quebradas.
        vertical_alignment=ft.CrossAxisAlignment.CENTER, # Alinha os elementos na vertical.
        expand=True, # Expande a row para ocupar todo o espaço disponível da tela.
    )

    row2 = ft.Row(
        controls=[
            ft.Image(src='https://www.google.com/imgres?q=python&imgurl=https%3A%2F%2Fassets.bitdegree.org%2Fonline-learning-platforms%2Fstorage%2Fmedia%2F2018%2F11%2F10-Tips-To-Learn-Python.jpg&imgrefurl=https%3A%2F%2Fbr.bitdegree.org%2Ftutoriais%2Fcursos-de-python&docid=CHO5iyUBf6LqWM&tbnid=HDC6HxfjvUYNiM&vet=12ahUKEwiL79Sq8J6MAxUCL7kGHYONOPc4ChAzegQIIxAA..i&w=900&h=560&hcb=2&ved=2ahUKEwiL79Sq8J6MAxUCL7kGHYONOPc4ChAzegQIIxAA'),
            ft.Image(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKgyzql0gnXIx-6IJlyo1k_wQpEuF_7cpy0Q&s'),
            ft.Image(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbcQhiY19jIRjg1hs9FsJkb_3GUNNf6QQWfw&s'),
            ft.Image(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYVRNXpVxo0vi-n9an6M2zaCF0tgsJbja3hw&s'),
            ft.Image(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYPf1U_b2w5g6CYeVlhYq_y9BNA6ZIHyrA_Q&s')
        ],
        scroll=ft.ScrollMode.ALWAYS, # Adiciona a barra de rolagem caso seja necessário.
        auto_scroll=True # Faz o scroll automaticamente para o ultimo elemento.
    )

    page.add(row1, row2)


ft.app(target=main)
