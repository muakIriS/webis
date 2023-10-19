import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

# Listas de saludos aleatorios
saludos_lista1 = ["Elemental", "Rompe Ralph", "Big Hero 6", "Zootopia", "Coco", "Del revés", "Wall-E", "Hermano Oso", "Red", "Cars", "Bolt", "Up", "Toy Story", "Tom and Jerry: The Fast and the Furry", "Tom e Jerry Rumo à Marte Cena 10"]
saludos_lista2 = ["¿Sale paja?", "Peliculita? (primer boton)", "Algun jueguito chulo?", "¿Sale llamadita con los catalanes?", "¿Toca mirar fotos de gatitos y twitter juntos?"]
saludos_lista3 = ["1", "2", "3", "4", "5", "6"]

# Diccionario que asocia cada texto con su imagen
imagenes_textos = {
    "Elemental": "Elemental.jfif",
    "Rompe Ralph": "RompeRalph.jpg",
    "Big Hero 6": "BigHero6.jpg",
    "Zootopia": "Zootopia.png",
    "Coco": "Coco.jpg",
    "Del revés": "Delrevés.jpg",
    "Wall-E": "Wall-E.jpeg",
    "Hermano Oso": "HermanoOso.png",
    "Red": "Red.png",
    "Cars": "Cars.jpg",
    "Bolt": "Bolt.jpg",
    "Up": "Up.jpg",
    "Toy Story": "ToyStory.jpg",
    "Tom and Jerry: The Fast and the Furry": "TomandJerryTheFastandtheFurry.jpg",
    "Tom e Jerry Rumo à Marte Cena 10": "TomeJerryRumoàMarteCena10.jpeg"
}

def click(lista):
    # Elegir un saludo aleatorio de la lista especificada
    saludo_aleatorio = random.choice(lista)
    label_texto.config(text=saludo_aleatorio)
    
    # Obtener la imagen asociada al texto y mostrarla
    if saludo_aleatorio in imagenes_textos:
        mostrar_imagen(imagenes_textos[saludo_aleatorio])
    else:
        label_imagen.config(image=None)

def mostrar_imagen(ruta_imagen):
    image = Image.open(ruta_imagen)
    photo = ImageTk.PhotoImage(image)
    label_imagen.config(image=photo)
    label_imagen.image = photo

# Crear una ventana
window = tk.Tk()
window.title("Mi Aplicación")

# Cambiar el fondo de la ventana a color rosa
window.configure(bg="pink")

# Establecer el tamaño de la ventana
window.geometry("400x400")

# Crear una etiqueta para mostrar el texto
label_texto = tk.Label(window, text="", font=("Arial", 14), bg="pink")
label_texto.place(relx=0.5, rely=0.1, anchor="center")

# Crear una etiqueta para mostrar la imagen en el centro de la ventana
label_imagen = tk.Label(window, bg="pink")
label_imagen.place(relx=0.5, rely=0.5, anchor="center")

# Crear un contenedor para los botones y centrarlos en la parte inferior
button_container = tk.Frame(window)
button_container.place(relx=0.5, rely=0.9, anchor="center")

# Estilo para los botones
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5, borderwidth=3, relief="groove", background="lightblue", foreground="black")

# Crear botones dentro del contenedor con estilo
button1 = ttk.Button(button_container, text="¿Pelicula de hoy?", command=lambda: click(saludos_lista1))
button2 = ttk.Button(button_container, text="Planes de hoy", command=lambda: click(saludos_lista2))
button3 = ttk.Button(button_container, text="Dado", command=lambda: click(saludos_lista3))

# Empaquetar los botones de izquierda a derecha para que estén centrados
button1.pack(side="left", padx=10)
button2.pack(side="left", padx=10)
button3.pack(side="left", padx=10)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()





