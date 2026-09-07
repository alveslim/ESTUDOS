import flet as ft

def main(page: ft.Page):
    
    def add_task(e):
        
        print(new_task.value)
        page.add(ft.Checkbox(label=f'{new_task.value}'))
        new_task.value = '' # para limpar o campo de texto apos clicar no botao
        page.update() # aparentemente funciona sem o update, mas é bom colocar para garantir que a tela seja atualizada
        
    new_task = ft.TextField(hint_text='Insira uma funcao')
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)
    
    
    page.add(new_task, new_button)

ft.app(target=main)