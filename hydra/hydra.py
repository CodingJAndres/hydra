import os

def show_menu():
    print("\033[1;32m--- Menú de Comandos de Hydra ---\033[0m")
    print("\033[1;36m1. Ejecutar Hydra con lista de usuarios y contraseñas")
    print("2. Ejecutar Hydra con ataque de fuerza bruta")
    print("3. Ejecutar Hydra con un diccionario de contraseñas")
    print("4. Mostrar resultados de Hydra")
    print("5. Mostrar configuración actual de Hydra")
    print("6. Salir\033[0m")

def main():
    try:
        while True:
            try:
                show_menu()
                choice = input("Selecciona una opción (1-6): ")

                if choice == '1':
                    target = input("Introduce la IP o URL del objetivo: ")
                    username_file = input("Introduce el nombre del archivo de usuarios: ")
                    password_file = input("Introduce el nombre del archivo de contraseñas: ")
                    os.system(f"hydra -L {username_file} -P {password_file} {target} ssh")
                elif choice == '2':
                    target = input("Introduce la IP o URL del objetivo: ")
                    username = input("Introduce el nombre de usuario: ")
                    os.system(f"hydra -l {username} -P common_passwords.txt {target} ssh")
                elif choice == '3':
                    target = input("Introduce la IP o URL del objetivo: ")
                    username = input("Introduce el nombre de usuario: ")
                    password_file = input("Introduce el nombre del archivo de contraseñas: ")
                    os.system(f"hydra -l {username} -P {password_file} {target} ssh")
                elif choice == '4':
                    print("No hay una opción para mostrar resultados en Hydra.")
                elif choice == '5':
                    print("No hay una opción para mostrar configuración actual en Hydra.")
                elif choice == '6':
                    print("¡Adiós!")
                    break
                else:
                    print("Opción inválida. Por favor, selecciona una opción válida (1-6).")
            except KeyboardInterrupt:
                print("\nPrograma cerrado.")
                break
            except FileNotFoundError:
                print("Error: Archivo no encontrado.")
            except Exception as e:
                print(f"Se produjo un error: {str(e)}")
    except KeyboardInterrupt:
        print("\nPrograma cerrado.")

if __name__ == "__main__":
    main()
