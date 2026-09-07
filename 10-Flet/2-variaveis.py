import flet as ft

def main(page: ft.Page):
    
    def add_task(e):
        print(new_task.value)
    
    # Input de texto
    new_task = ft.TextField(hint_text='Insira uma tarefa...')
    page.add(new_task)
    
    # Botão
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD,  on_click=add_task)
    page.add(new_button)

    pass

ft.app(target=main)