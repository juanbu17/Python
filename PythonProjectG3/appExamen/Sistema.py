from Usuario import Usuario


class Sistema:
    def _init_(self):
        self.usuarios = {}
        usuarios = []
    def registrar_usuario(self, salario_bruto=None):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        if usuario not in self.usuarios:
            self.usuarios[usuario] = Usuario(nombre, apellido, usuario, contrasena, salario_bruto)
            print("Usuario registrado exitosamente.")
        else:
            print("El usuario ya existe. Intente nuevamente.")

    def autenticar_usuario(self, usuario, contrasena):
        if usuario in self.usuarios and self.usuarios[usuario].contrasena == contrasena:
            return self.usuarios[usuario]
        return None

    def mostrar_datos(self, usuario):
        print(f"Nombre: {usuario.nombre}")
        print(f"Apellido: {usuario.apellido}")

    def calcular_salario_neto(self, usuario):
        salario_bruto = usuario.salario_bruto
        impuesto_renta = salario_bruto * 0.15
        seguro_social = salario_bruto * 0.05
        salario_neto = salario_bruto - impuesto_renta - seguro_social
        print(f"Salario bruto: ${salario_bruto:.2f}")
        print(f"Impuesto de renta: ${impuesto_renta:.2f}")
        print(f"Seguro social: ${seguro_social:.2f}")
        print(f"Salario neto: ${salario_neto:.2f}")

def menu_ppal():
    sistema = Sistema()
    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrar_usuario()
        elif opcion_usuario == "2":
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            usuario_actual = sistema.autenticar_usuario(usuario, contrasena)
            if usuario_actual:
                while True:
                    print("\nMenú de usuario:")
                    print("1. Ver datos")
                    print("2. Calcular salario neto")
                    print("3. Salir")
                    opcion_usuario = input("Seleccione una opción: ")
                    if opcion_usuario == "1":
                        sistema.mostrar_datos(usuario_actual)
                    elif opcion_usuario == "2":
                        sistema.calcular_salario_neto(usuario_actual)
                    elif opcion_usuario == "3":
                        break
                    else:
                        print("Opción inválida.")
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "3":
            print("¡Vuelve pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu_ppal()