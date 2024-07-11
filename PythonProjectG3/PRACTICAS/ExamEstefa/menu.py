

class Menu:
    def __init__(self):
        self.opciones = {
            "1": "Registrar usuario",
            "2": "Iniciar sesión",
            "3": "Salir"
        }

    def mostrar_menu(self):
        print("\nMenú:")
        for key, value in self.opciones.items():
            print(f"{key}. {value}")

    def get_opcion(self):
        return input("Seleccione una opción: ")
