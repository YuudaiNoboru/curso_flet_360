import flet as ft



# Breakpoint    Dimension
# xs	        <576px  Cecular
# sm	        ≥576px  Tablet
# md	        ≥768px  Tablet maiores
# lg	        ≥992px  Notebooks
# xl	        ≥1200px Monitores padrões
# xxl	        ≥1400px Monitores grandes ou widescreen

def main(page: ft.Page):

    row1 = ft.ResponsiveRow(
        columns=12, # Número de colunas do layout, o padrão é 12.
        run_spacing=50, # Espaçamento entre as linhas quebradas.
        spacing=20,
        expand=True,
        controls=[
            ft.ElevatedButton(
                col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1}, # Tamanho da coluna que o Componente ira ocular em cada breakpoint
                text='1',
                bgcolor=ft.Colors.AMBER,
                color=ft.Colors.BLACK,
            ),
            ft.ElevatedButton(
                col=4, # Tamanho unico de coluna que o Componente ira ocular em cada breakpoint
                text='1',
                bgcolor=ft.Colors.AMBER,
                color=ft.Colors.BLACK,
            )
        ]

    )


    page.add(row1)


ft.app(target=main)
