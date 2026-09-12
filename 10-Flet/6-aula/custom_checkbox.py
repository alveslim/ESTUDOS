import flet as ft

class Checkbox(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(ft.icons.SAVE, on_click=self.save_button,
                                         visible=False)
        self.delete_button = ft.IconButton(ft.icons.DELETE, on_click=self.delete)
        
        #controles da row
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button,
        ]

        def edit(self, e):
            pass
        
        def save(self, e):
            pass
        
        def delete(self, e):
            pass