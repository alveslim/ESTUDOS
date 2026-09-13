import flet as ft

# classe para criar as tarefas
class Task(ft.Column):
    pass
# classe para criar o aplicativo
class TodoApp(ft.Column):
    
    def build(self):
        self.new_task = ft.TextField(
            hint='Insira a Tarefa: ',
            expand=True,
            on_submit=self.add_task,
            )
        
        self.task = ft.Column()
        
        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text='Todas'),
                ft.Tab(text='Ativas'),
                ft.Tab(text='Concluidas'),
            ],
        )
        self.items_left = ft.Text('0 tarefas adicionadas')
        
        return ft.Column(
            controls=[
                # titulo da aplicacao
                ft.Row([
                    ft.Text(value='Tarefas',
                            theme_style='headlineMedium'
                            size=34,
                            weight='bold',
                            color=ft.color.with_opacity(0,7, 'black'),                            
                        )
                ],
                alignment='center'
                ),
                ft.Row(
                    controls=[
                        
                    ]
                    ),  
                ft.Column()  
            ]
        )
        
    def tabs_changed(self, e):
        pass
    
    def add_task(self, e):
        pass
        
    def main(page: ft.Page):
        page.title = 'Minhas Tarefas'
        page.padding = 20
        app = TodoApp()
        page.add(app)
    
ft.app(target=main)