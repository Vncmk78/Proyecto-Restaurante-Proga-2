from ElementoMenu import CrearMenu
from ev2_progra2.Ingrediente import Ingrediente

class Pedido:
    def __init__(self):
        self.menus = []  # Lista de objetos CrearMenu (nombre, precio, cantidad, etc.)

    def agregar_menu(self, menu: CrearMenu, cantidad: int = 1):
        # Verificar si el menú ya está en el pedido
        for item in self.menus:
            if item.nombre == menu.nombre:
                item.cantidad += cantidad
                return
        # Si no está, se agrega con la cantidad inicial
        menu.cantidad = cantidad
        self.menus.append(menu)

    def eliminar_menu(self, nombre_menu: str, stock):
        nombre_menu = nombre_menu.lower()
        for men in self.menus:
            if men.nombre.lower() == nombre_menu:
                # Para cada ingrediente del menú: buscar en stock y sumar la cantidad devuelta
                for ingrediente_necesario in men.ingredientes:
                    nombre_ing = ingrediente_necesario.nombre
                    # cantidad por unidad del menú (convierte a int por seguridad)
                    cantidad_por_menu = ingrediente_necesario.cantidad
                    

                    # la cantidad total a devolver = cantidad_por_menu * men.cantidad
                    total_devolver = cantidad_por_menu * int(getattr(men, "cantidad", 1))

                    # buscar ingrediente en stock (stock.lista_ingredientes es lista de Objetos Ingrediente)
                    encontrado = False
                    for ing_stock in stock.lista_ingredientes:
                        if ing_stock.nombre.lower() == nombre_ing.lower():
                            # ing_stock.cantidad se maneja como string en tu app: convertir y sumar
                            try:
                                nueva = int(ing_stock.cantidad) + total_devolver
                            except Exception:
                                # si por alguna razón no es entero, intentar setear directamente
                                ing_stock.cantidad = str(total_devolver)
                                encontrado = True
                                break
                            ing_stock.cantidad = str(nueva)
                            encontrado = True
                            break

                # finalmente eliminar el menú del pedido
                self.menus.remove(men)
                return True

        return False


    def mostrar_pedido(self):
        # Retorna una lista con los datos del pedido para mostrar en la interfaz
        return [(m.nombre, m.cantidad, m.precio, m.precio * m.cantidad) for m in self.menus]

    def calcular_total(self) -> float:
        return sum(m.precio * m.cantidad for m in self.menus)