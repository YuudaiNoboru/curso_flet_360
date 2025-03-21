import flet as ft


def main(page: ft.Page):
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Dragon Slayer": "fonts/Dragon Slayer.ttf",
    }

    t1 = ft.Text(
        value="Olá mundo, seja bem vindo ao curso de Flet do Programador Aventureiro",  # Texto mostrado na tela.
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,  # Estilo de textos predefinidos.
        bgcolor=ft.Colors.WHITE,  # Cor do fundo da caixa do texto.
        color=ft.Colors.BLACK,  # Altera a cor da fonte.
        # font_family="Dragon Slayer", # Altera a fonte do texto.
        italic=True,  # Define o texto como itálico
        # max_lines=2, # Defino o maxímo de linhas em que o texto pode ser quebrado
        overflow=ft.TextOverflow.ELLIPSIS,  # Define uma forma de corta o texto, nesse caso adiciona ...
        no_wrap=True,  # Não permite que o texto seja quebrado
        selectable=True,  # Permite que o texto seja selecionado pelo cursor.
        size=50,  # Tamanho do texo
        text_align=ft.TextAlign.JUSTIFY,  # Forma de alinhamento do texto.
        weight=ft.FontWeight.W_900,  # Peso da fonte.
    )

    # Criação de estilos em variaveis para reaproveitamento
    link_style = ft.TextStyle(
        color=ft.Colors.BLUE, decoration=ft.TextDecoration.UNDERLINE
    )
    title_style = ft.TextStyle(
        bgcolor=ft.Colors.AMBER,
        color=ft.Colors.RED,
        decoration=ft.TextDecoration.OVERLINE,
        decoration_color=ft.Colors.GREEN,
        decoration_thickness=5,
        decoration_style=ft.TextDecorationStyle.WAVY,
        italic=True,
        size=50,
        weight=ft.FontWeight.W_900,
    )
    # Personalisar cada parte do texto.
    t2 = ft.Text(
        spans=[
            ft.TextSpan(
                text="Texto com link ", style=link_style, url="https://www.google.com"
            ),
            ft.TextSpan(text="continuação do texto... ", style=title_style),
            ft.TextSpan(
                text="Texto em destaque!!!",
            ),
        ],
        size=70,
    )

    page.add(t1, t2)


ft.app(
    target=main,
    assets_dir="assets",  # Define o caminha da pasta de assets
)
