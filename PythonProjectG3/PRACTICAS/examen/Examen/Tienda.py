from usuario import Usuario
class Tienda:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del producto : ")
        marca = input("Ingrese la marca : ")
        precio = int(input("Ingresa el precio: "))
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if usuario not in self.usuarios:
            self.usuarios[usuario] = Usuario(nombre, marca, usuario, contrasena,precio)
            print("Registro exitoso.")
            print(self.usuarios[usuario])
        else:
            print("El producto ya existe")

    def autenticar_usuario(self, usuario, contrasena):
        print(usuario , contrasena)
        if usuario in self.usuarios and self.usuarios[usuario].contrasena == contrasena:

            return self.usuarios[usuario]
        return None

    def mostrar_datos(self, usuario):
        print(f"Producto: {usuario.nombre}")
        print(f"Marca: {usuario.marca}")

    def calcular_precio_neto(self, usuario):
        precio = usuario.precio
        impuesto = usuario.precio * 0.19
        precio_neto = usuario.precio + impuesto
        print(f"Precio bruto: ${precio:.2f}")
        print(f"Impuesto : ${impuesto:.2f}")
        print(f"Precio total: ${precio_neto:.2f}")

def main():
    sistema = Tienda()
    while True:
        print("\nMenú:")
        print("1. Registrar producto")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrar_usuario()
        elif opcion == "2":
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            usuario_actual = sistema.autenticar_usuario(usuario, contrasena)
            print (usuario_actual)
            if usuario_actual:
                while True:
                    print("\nMenú de usuario:")
                    print("1. Ver datos")
                    print("2. Calcular precio neto")
                    print("3. Salir")
                    opcion_usuario = input("Seleccione una opción: ")
                    if opcion_usuario == "1":
                        sistema.mostrar_datos(usuario_actual)
                    elif opcion_usuario == "2":
                        sistema.calcular_precio_neto(usuario_actual)
                    elif opcion_usuario == "3":
                        break
                    else:
                        print("Opción Incorrecta!!!.")
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "3":
            print("¡Vuelve pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()