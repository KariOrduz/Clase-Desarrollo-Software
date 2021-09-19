from ClassBlog import Blog


class Persona:
    def __init__(self, nombre, usuario, contraseña, edad=0, nivelEducativo="Primaria"):
        self.nombre = nombre
        self.usuario = usuario 
        self.contraseña = contraseña
        self.edad = edad
        self.nivelEducativo = nivelEducativo

        self.blogs = []

    def cambiarContra (self, nueva):
        self.contraseña = nueva

    def addBlog (self, titulo, fecha, contenido):
        #Creacon de blog
        nuevoBlog = Blog(titulo, fecha, contenido)

        self.blogs.append(nuevoBlog)

    def mostrarTitulos (self):
        msg = "El usuario " + self.usuario + " tiene " + str(len(self.blogs)) + " blogs que se titulan: "
        for blog in self.blogs:
            msg += blog.titulo + ", "
        msg = msg [:-2] #Se retira el último espacio y la coma
        return msg

#Crear Personas
Jose = Persona("Jose Alexander", "jalex", "123")
Pedro = Persona("Pedro Pérez", "pp", "234")

#Creación de Blogs
Jose.addBlog("Educación siglo XXI", "2021", "La educación.....")
Pedro.addBlog("Peliculas de comedia", "2020", "No queras parar de verlas....")
Jose.addBlog("Política", "2020", "La nueva era de la plítica....")


print(Jose.mostrarTitulos())
print(Pedro.mostrarTitulos())
