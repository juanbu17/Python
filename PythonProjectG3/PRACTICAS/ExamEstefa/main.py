from menu import Menu
from calcular_salario import CalcularSalario
from usuario import Usuario

def main():
    usuarios_registrados = []
    menu = Menu()

    while True:
        menu.mostrar_menu()
        opcion = menu.get_opcion()

        if opcion == "1":
            nuevo_usuario = Usuario(None, None, None, None, None)
            nuevo_usuario.registrar_usuario()
            usuarios_registrados.append(nuevo_usuario)
            print("Usuario registrado exitosamente.")

        elif opcion == "2":
            usuario_nombre = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            usuario_encontrado = None

            for usuario in usuarios_registrados:
                if usuario.autenticar_usuario(usuario_nombre, contrasena):
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                calculadora_salario = CalcularSalario(usuario_encontrado)
                while True:
                    print("\nMenú de usuario:")
                    print("1. Ver datos")
                    print("2. Calcular salario neto")
                    print("3. Salir")
                    opcion_usuario = input("Seleccione una opción: ")
                    if opcion_usuario == "1":
                        print(usuario_encontrado)
                    elif opcion_usuario == "2":
                        calculadora_salario.calcular_salario_neto()
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

if __name__ == "__main__":
    main()
