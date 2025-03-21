import flet as ft


def main(page: ft.Page):
    # Formas de trabalhar com cores no Flet.
    page.bgcolor = "amber100"  # Aletaração de cor por string
    page.bgcolor = "#B12B12"  # Alteração de cor com HEX
    page.bgcolor = ft.Colors.RED  # Aleração de cor com o módulo Colors

    # Alinhamentos horizontais
    page.horizontal_alignment = (
        ft.CrossAxisAlignment.CENTER
    )  # Alinha no centro da linha.
    page.horizontal_alignment = ft.CrossAxisAlignment.END  # Alinha no final da linha.
    page.horizontal_alignment = (
        ft.CrossAxisAlignment.START
    )  # Alinha no ínicio da linha, esse é o padrão.
    page.horizontal_alignment = (
        ft.CrossAxisAlignment.STRETCH
    )  # Estica os elementos por toda a linha.

    # Alinhamentos verticais
    page.vertical_alignment = (
        ft.MainAxisAlignment.CENTER
    )  # Alinha os elementos no centro da coluna.
    page.vertical_alignment = (
        ft.MainAxisAlignment.END
    )  # Alinha os elementos no final da coluna.
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND  # Alinha os elementos com espaço iguais de cada elemento no início e no final entre eles na coluna
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN  # Alinah os elementos com espaço igual apenas entre eles, não coloca espaco no início e no final da coluna.
    page.vertical_alignment = (
        ft.MainAxisAlignment.SPACE_EVENLY
    )  # Alinha os elementos com espaçõ iguais entre os elementos na coluna.
    page.vertical_alignment = (
        ft.MainAxisAlignment.START
    )  # Alinha os elementos no incío da coluna. Esse é o padrão.]

    # Padding
    page.padding = 100  # Adiciona o padding em todos os lados.
    page.padding = ft.padding.symmetric(
        horizontal=50, vertical=100
    )  # Adiciona o padding diferentes nas laterais e no topo e na base.
    page.padding = ft.padding.only(
        left=15, top=35, right=40, bottom=50
    )  # Adiciona padding diferente para cada lado.
    page.padding = ft.padding.all(
        10
    )  # Adiciona o padding em todos os lados. Por padrão o padding de 10 já é adicionado.

    # Spacing
    page.spacin = 10  # Adiciona espaço entre os elementos, por padrão o espaço de 10 já é adicionado.

    # Title
    page.title = "Flet App" # Adiciona um título à página.

    page.add(
        ft.Container(
            ft.Text(
                value="Olá Mundo 1!",
            ),
            bgcolor="teal",
        ),
        ft.Container(ft.Text(value="Olá mundo 2!"), bgcolor="black"),
        ft.Container(ft.Text(value="Olá mundo 3!"), bgcolor="green"),
    )

    page.update()


ft.app(target=main)
