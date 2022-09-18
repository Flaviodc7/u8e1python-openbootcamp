def leerArchivo():
    f = open('texto.txt', 'r')
    print(f.read())
    f.close()

def escribirArchivo():
    f = open('texto.txt', 'w')
    f.writelines("Estas son lineas\nque estoy añadiendo yo\nMuchas gracias")

escribirArchivo()
leerArchivo()