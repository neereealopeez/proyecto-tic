import flet as ft

def main(page: ft.Page):
    page.title="InfoVIP"
    page.bgcolor="#DDE3FF"
    img = ft.Image(src=f"esto no se ve", width=300, height=300)
    img.src = "imagen.png"
    page.add(img)
    t =ft.Text(value="INFOVIP", color="#6F82EB",size=30, font_family="Times New Roman")
    page.add(t)
    textField_Usuario= ft.TextField(label="Usuario", hint_text="Escribe aquí tu nombre de usuario", width=400)
    textField_Contraseña= ft.TextField(label="Contraseña", hint_text="Escribe aquí tu contraseña", width=400)


    def cargarFichero():
        vDatos = []
        f= open("Datos.txt","r")
        for linea in f:
            vDatos.append(linea.replace("\n",""))
        
        f.close()
        return vDatos


    def comprobar_login(e):
        #Leer textfield

        #Cargar datos del fichero
        vDatos = cargarFichero()
        print(vDatos)
        #Comprobar que coincidan los datos
        0


    botonRegistrar =ft.ElevatedButton(text="Registrar", icon="Login",on_click=comprobar_login)
    page.add(textField_Usuario, textField_Contraseña, botonRegistrar)


    
    
ft.app(target=main, assets_dir="Imagen")




