import flet as ft

def main(page: ft.Page):
    page.title = 'flet app'
    page.padding = 20
    
    def add_task(e):
        task_list.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()
        
    new_task = ft.TextField(hint_text="Insira uma tarefa", expand=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)
    
    task_list = ft.Column()
    task_column = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    new_button
                ]
            ),
            task_list
        ]
    )
    
    page.add(task_column)
    
ft.app(target=main)