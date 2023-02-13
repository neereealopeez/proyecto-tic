import flet as ft

def main(page: ft.Page):
    page.title="InfoVIP"
    img = ft.Image(src=f"esto no se ve", width=300, height=300)
    img.src = "imagen.png"
    page.add(img)
    t =ft.Text(value="INFOVIP", color="#6F82EB",size=30, font_family="Times New Roman")
    page.add(t)
    textField_Usuario= ft.TextField(label="Usuario", hint_text="Escribe aquí tu nombre de usuario", width=400)
    textField_Contraseña= ft.TextField(label="Contraseña", hint_text="Escribe aquí tu contraseña", width=400)
    botonRegistrar =ft.ElevatedButton(text="Registrar")
    page.add(textField_Usuario, textField_Contraseña, botonRegistrar)
    
ft.app(target=main, assets_dir="Imagen")




