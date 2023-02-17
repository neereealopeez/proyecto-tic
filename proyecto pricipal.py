import flet as ft

def main(page: ft.Page):
  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def comprobar_login(e):
    a.value = f"Textboxes values are:  '{textField_Contraseña.value}', '{textField_Usuario.value}'"
    page.update()

    page.title="InfoVIP"
    page.bgcolor="#DDE3FF"
    img = ft.Image(src=f"esto no se ve", width=200, height=200)
    img.src = "imagen2.png"
    page.add(img)
    t =ft.Text(value="INFOVIP", color="#6F82EB",size=30, font_family="Times New Roman")
    page.add(t)
    a = ft.Text()
    textField_Usuario= ft.TextField(label="Usuario", hint_text="Escribe aquí tu nombre de usuario", width=400)
    textField_Contraseña= ft.TextField(label="Contraseña", hint_text="Escribe aquí tu contraseña", width=400)
    botonRegistrar =ft.ElevatedButton(text="Registrar", icon="Login",on_click=comprobar_login)
    page.add(textField_Usuario, textField_Contraseña, botonRegistrar)


    def cargarFichero():
        vDatos = []
        f= open("Datos.txt","r")
        for linea in f:
            vDatos.append(linea.replace("\n",""))
        
        f.close()
        return vDatos



    
ft.app(target=main, assets_dir="Imagen")




