class Blog:
  def __init__(self, titulo, fecha, contenido):
    self.titulo = titulo
    self.fecha = fecha
    self.contenido = contenido

  def editarTitulo (self, nuevoTitulo):
    self.titulo = nuevoTitulo

  def editarContenido (self, nuevoContenido):
    self.contenido = nuevoContenido

  def mostrarBlog(self):
    return self.titulo + "\t" + self.fecha + "\n\n" + self.contenido


b1 = Blog("Star Wars", "07/09/2021", "La mejor de la saga de películas...")

#print(b1.mostrarBlog())

