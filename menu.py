xfrom char_to_byte import char_to_byte
from word_to_bytes import word_to_bytes
from byte_to_ascii import byte_to_ascii

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Generar la representación en byte de un carácter")
        print("2. Generar la representación en byte de una palabra")
        print("3. Generar la representación ASCII de un byte")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == '1':
            char = input("Ingrese un carácter: ")
            if len(char) == 1:
                print(f"La representación en byte de '{char}' es: {char_to_byte(char)}")
            else:
                print("Por favor, ingrese un solo carácter.")

        elif option == '2':
            word = input("Ingrese una palabra: ")
            print(f"La representación en byte de '{word}' es: {word_to_bytes(word)}")

        elif option == '3':
            byte_str = input("Ingrese una representación en byte (8 bits): ")
            if len(byte_str) == 8 and all(bit in '01' for bit in byte_str):
                print(f"La representación ASCII de '{byte_str}' es: {byte_to_ascii(byte_str)}")
            else:
                print("Por favor, ingrese una representación válida en byte (8 bits).")

        elif option == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    menu()
