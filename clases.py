class Libro:
  pass
# Usando el método constructor
class Libre:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

mi_libro = Libro("100 Años de soledad",  "Gabriel García Márquez")
otro_libro = Libro("Guerra y paz", "León Tolstoi")
