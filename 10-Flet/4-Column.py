import flet as ft

def main(page: ft.Page):
    
    def add_task(e):
        print(new_task.value)
        page.add(ft.Checkbox(label=f'{new_task.value}'))
        new_task.value = ''
        page.update()
        
    new_task = ft.TextField(hint_text='Insira uma tarefa', expand=True) # expand=True faz com que o campo de texto ocupe todo o espaço disponivel na tela
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)
    
    task_column = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    new_task, # task_column.add(new_task) # adiciona o campo de texto na coluna
                    new_button # pode ir adicionando nossas variaveis na coluna, e elas vao se organizando em linha, uma ao lado da outra
                ]
            )
        ]
    )
    
    page.add(task_column)
    
ft.app(target=main)