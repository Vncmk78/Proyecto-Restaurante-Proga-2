from ElementoMenu import CrearMenu

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

    def eliminar_menu(self, nombre_menu: str):
        self.menus = [m for m in self.menus if m.nombre != nombre_menu]

    def mostrar_pedido(self):
        # Retorna una lista con los datos del pedido para mostrar en la interfaz
        return [(m.nombre, m.cantidad, m.precio, m.precio * m.cantidad) for m in self.menus]

    def calcular_total(self) -> float:
        return sum(m.precio * m.cantidad for m in self.menus)