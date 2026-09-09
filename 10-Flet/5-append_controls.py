import flet as ft

def main(page: ft.Page):
    
    page.title = 'Flet To-Do list'
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = 'auto'
    page.window_resizable = False
    page.window_maximizable = False
    page.window_minimizable = False
    page.window_title_bar_hidden = True
    page.window_always_on_top = True
    page.window_center = True
    page.window_frameless = True
    page.window_full_screen = False
    page.window.width = 400
    page.window.height = 650
    page.padding = ft.padding.Padding(top=20, left=20, right=20, bottom=20)
    #page.padding = ft.padding.only(top=80)
    
    def add_task(e):
        print(new_task.value)
        task_list.controls.append(ft.Checkbox(label=new_task.value)) # adiciona a tarefa na lista de tarefas
        new_task.value = ''
        page.update()
        
    new_task = ft.TextField(hint_text='What needs to be done?', expand=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)
    
    task_list = ft.Column() # cria uma coluna para armazenar as tarefas adicionadas
    
    task_column = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    new_task, 
                    new_button 
                ]
            ),
            task_list # adiciona a coluna de tarefas na coluna principal
        ]
    )
    
    page.add(task_column)
    
ft.app(target=main)