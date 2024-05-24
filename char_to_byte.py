def char_to_byte(char):
    """Convierte un carácter a su representación en byte (binario)."""
    return format(ord(char), '08b')

if __name__ == "__main__":
    char = input("Ingrese un carácter valido para poder realizar el procedimiento : ")
    print(f"La representación en byte de '{char}' es: {char_to_byte(char)}")
