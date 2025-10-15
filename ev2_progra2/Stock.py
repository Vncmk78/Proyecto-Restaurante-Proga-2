from ev2_progra2.Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        nombre_ing = ingrediente.nombre.lower() # convertimos a minusculas para evitar errores
        for ing in self.lista_ingredientes:
            nombre_ing_existente = ing.nombre.lower() 
            if nombre_ing_existente == nombre_ing: # si el ingrediente ya existe, sumamos la cantidad
                ing.cantidad += float(ingrediente.cantidad) # convertimos a float para evitar errores
                return
        self.lista_ingredientes.append(ingrediente)

    def eliminar_ingrediente(self, nombre_ingrediente):
        nombre_ingrediente = nombre_ingrediente.lower()
        for ing in self.lista_ingredientes:
            if ing.nombre.lower() == nombre_ingrediente:
                self.lista_ingredientes.remove(ing)
                return True
        return False
    
    def verificar_stock(self):
        ingredientes_disponibles = []
        for ing in self.lista_ingredientes:
            if ing.cantidad > 0:
                ingredientes_disponibles.append(ing)
        return ingredientes_disponibles

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        nombre_ingrediente = nombre_ingrediente.lower()
        for ing in self.lista_ingredientes:
            if ing.nombre.lower() == nombre_ingrediente:
                ing.cantidad = float(nueva_cantidad) # convertimos a float para evitar errores
                return True
        return False

    def obtener_elementos_menu(self):
        pass
        

