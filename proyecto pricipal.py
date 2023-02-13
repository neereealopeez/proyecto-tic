import flet as ft

def main(page: ft.Page):
    page.title = "Infovip"
    
    
        
    t =ft.Text(value="INFOVIP", color="#6F82EB",size=30)
    page.add(t)
    
    botonRegistrar =ft.ElevatedButton(text="Reg  istrar")
    page.add(botonRegistrar)
    





ft.app(target=main)