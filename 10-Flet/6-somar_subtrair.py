import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 1. Criamos os elementos visuais
    texto_numero = ft.Text(value="0", size=50)
    #texto_numero_topo = ft.Text(value="0", size=50)
    #texto_numero_base = ft.Text(value="0", size=50)
    


    # 2. Criamos as funções que respondem aos cliques
    def somar(e):
        texto_numero.value = str(int(texto_numero.value) + 1)
        page.update() # IMPORTANTE: Avisa o Flet para atualizar a tela

    def subtrair(e):
        texto_numero.value = str(int(texto_numero.value) - 1)
        page.update()

    # 3. Adicionamos tudo à página organizando em uma Linha (Row)
    page.add(
    ft.Column( # A Coluna empilha tudo verticalmente
        controls=[
            # A LINHA DE CIMA
            ft.Row(
                controls=[
                    ft.IconButton(ft.Icons.REMOVE, on_click=subtrair),
                    ft.IconButton(ft.Icons.ADD, on_click=somar),
                    texto_numero # IMPORTANTE: Veja a nota abaixo
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            
            # A LINHA DE BAIXO
            ft.Row(
                controls=[
                    ft.IconButton(ft.Icons.REMOVE, on_click=subtrair),
                    texto_numero,
                    ft.IconButton(ft.Icons.ADD, on_click=somar)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )
)

ft.app(target=main)