import flet as ft

def main(page: ft.Page):
    page.title="InfoVIP"
    img = ft.Image(src=f"esto no se ve", width=300, height=300)
    img.src = "imagen.png"
    page.add(img)
    t =ft.Text(value="INFOVIP", color="#6F82EB",size=30)
    page.add(t)
    botonRegistrar =ft.ElevatedButton(text="Registrar")
    page.add(botonRegistrar)
    
ft.app(target=main, assets_dir="Imagen")