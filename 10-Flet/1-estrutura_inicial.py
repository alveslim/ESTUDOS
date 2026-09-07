import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value="Olá, Flet!", 
                     size=30, 
                     weight="bold", color="#1E293B"))
    pass

ft.app(target=main)