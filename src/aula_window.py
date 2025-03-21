import flet as ft


def main(page: ft.Page):
    page.bgcolor = (
        ft.Colors.TRANSPARENT
    )  # Cor transparente permite visualisar o que está no fundo do app.
    page.title = "Flet App"

    # Propiedades das janelas
    page.window.always_on_top = True  # Permite que a janela do App seje esteja sobreposta as outras. O padrão é false.
    page.window.title_bar_hidden = True  # Oculta a barra de título. O padrão é False.
    page.window.title_bar_hidden = False
    page.window.frameless = True  # Funciona semelhante ao title_bar_hidden no Windows e Linux, mas no Mac Os permite retirar os botões de ação do title. O padrão é falso.
    page.window.frameless = False
    page.window.bgcolor = ft.Colors.AMBER
    page.window.full_screen = (
        True  # Obriga a aplicação a ser executa em Full Screen. O padrão é False.
    )
    page.window.full_screen = False

    page.window.height = 300  # Define o tamanho inicial da tela. Ela ainda pode ser alterada pelo usuário.
    page.window.width = 300
    page.window.max_height = (
        400  # Define o tamanho máximo que pode ser redirecionado pelo usuário.
    )
    page.window.max_width = 400
    page.window.min_height = 250  # Define o tamanho mínimo da janela.
    page.window.min_width = 250

    # page.window.resizable = False  # Desabilita a posibilidade do usário redimencionar o App. O padrão é True.

    page.window.movable = (
        False  # Desabilita a possibilidade do usuário mover o App. O padrão é True.
    )

    page.window.top = 500  # Define a distancia do top da tela que o App deve iniciar.
    page.window.left = (
        400  # Define a distancia da esquerda da tela que o App deve iniciar.
    )

    page.window.prevent_close = (
        True  # Impede que o usuario feche o App. So funciona no Mac OS. Padrão False.
    )

    page.window.progress_bar = (
        0.8  # Mostra uma barra de progresso na barra de tarefa. So funciona no Mac
    )

    print(
        page.platform
    )  # Mostra em qual plataforma o App está rodando, Windows, Linux, Android e etc, mesmo rodando na Web ele mostra o sistema operacional.

    page.window.center()  # Inicia a aplicação no centro da tela.

    # Essa função mostra os tamanho da tela, só funciona no apps rodando em desktop.
    def page_resize(e):
        print("Tamanho:", page.window.width, page.window.height)

    page.on_resized = page_resize  # Essa função on_resized só funciona em apps desktop.

    page.update()


ft.app(target=main)
