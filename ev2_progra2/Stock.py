from ev2_progra2.Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        for ing in self.lista_ingredientes:
            if ing.nombre == ingrediente.nombre and ing.unidad == ingrediente.unidad:
                ing.cantidad += ingrediente.cantidad
                return
        self.lista_ingredientes.append(ingrediente)

    def eliminar_ingrediente(self, nombre_ingrediente):
        for ing in self.lista_ingredientes:
            if ing.nombre == nombre_ingrediente:
                self.lista_ingredientes.remove(ing)
                return True

    def verificar_stock(self):
        ingredientes_disponibles = []
        for ing in self.lista_ingredientes:
            if ing.cantidad > 0:
                ingredientes_disponibles.append(ing)
        return ingredientes_disponibles

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        pass

    def obtener_elementos_menu(self):
        pass

