import flet as ft


def main(page: ft.Page):
    # Incluir imagem por URL
    img = ft.Image(
        src="https://lginfo.com.br/site/wp-content/uploads/2023/10/Python-Symbol.png",
        border_radius=ft.border_radius.all(20),  # Define as bordas da imagem.
        height=550,
        width=550,
        fit=ft.ImageFit.CONTAIN,  # Forma de desenhar a imagem.
        repeat=ft.ImageRepeat.REPEAT,  # Forma de ocupação do espaço pela imagem.
    )

    # Incluir imagem local.
    img2 = ft.Image(
        src="images/python.png",
        tooltip="Logo do python",  # Mostra informações sobre a imagem quando passar o cursor.
        src_base64="",  # Importação de imagem por texto.
    )

    page.add(img, img2)


ft.app(target=main, assets_dir="assets")
