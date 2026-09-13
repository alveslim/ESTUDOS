import flet as ft
from custom_checkbox import Checkbox

def main(page: ft.Page):
    page.title = 'flet app'
    page.padding = 20
    
    # capturar a altura e largura da pagina do nosso aplicativo
    WIDTH:  int = page.width
    HEIGHT: int = page.height
    print(f'largura: {WIDTH} | altura: {HEIGHT}')
    
    async def add_task(e):
        if new_task.value == '':
            await new_task.focus()
            return
        task_list.controls.append(Checkbox(new_task.value))
        new_task.value = ''
        page.update()
        await new_task.focus()
        
    new_task = ft.TextField(hint_text="Insira uma tarefa", 
                            expand=True,
                            autofocus=True, on_submit=add_task)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, 
                                         on_click=add_task)
    
    task_list = ft.Column(spacing=0,
                          height=HEIGHT-170, 
                          scroll=ft.ScrollMode.ADAPTIVE, 
                          expand=True)
    
    task_column = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    new_button
                ]
            ),
            task_list,
        ]
    )
    
    page.add(task_column)
    
ft.app(target=main)