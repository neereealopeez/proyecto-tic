import flet as ft

def main(page: ft.Page):
  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title="InfoVIP"
    page.bgcolor="#DDE3FF"
    
    img = ft.Image(src=f"esto no se ve", width=200, height=200)
    img.src = "imagen2.png"
   

    def cargarFichero():
        vDatos = []
        f= open("Datos.txt","r")
        for linea in f:
            vDatos.append(linea.replace("\n",""))
        
        f.close()
        return vDatos

    def comprobar_login(e):
        usuario = textField_Usuario.value
        password = textField_Contraseña.value
        vUsus = cargarFichero()

        if (vUsus.count(usuario) > 0) and (vUsus.count(password) > 0):
            print ("usuario en lista")

        else:
            dlg= ft.AlertDialog(title=ft.Text(f"Usuario y/o contraseña incorrectos. Te quedan {textField_Intentos.value} intentos."))
            textField_Intentos.value = textField_Intentos.value-1
            page.dialog = dlg
            dlg.open = True
            if 

            print(textField_Intentos.value)
        
        page.update()


    texto= ft.Text()
    t =ft.Text(value="INFOVIP", color="#6F82EB",size=30, font_family="Times New Roman")
    textField_Usuario= ft.TextField(label="Usuario", hint_text="Escribe aquí tu nombre de usuario", width=400)
    textField_Contraseña= ft.TextField(label="Contraseña", hint_text="Escribe aquí tu contraseña", width=400)
    textField_Intentos= ft.TextField(value=3)
    botonRegistrar =ft.ElevatedButton(text="Registrar", icon="Login",on_click=comprobar_login)
    page.add(textField_Usuario, textField_Contraseña, botonRegistrar, t, img, texto)

    



    
ft.app(target=main, assets_dir="Imagen")




