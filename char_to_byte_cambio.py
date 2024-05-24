def char_to_byte(char):
    """Convierte un carácter a su representación en byte (binario)."""
    return format(ord(char), '08b')

if __name__ == "__main__":
    char = input("Añada un carácter: ")
    print(f"el caracter en byte de '{char}' es: {char_to_byte(char)}")
