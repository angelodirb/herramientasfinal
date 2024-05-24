xdef byte_to_ascii(byte_str):
    """Convierte una representación en byte (binario) a su valor ASCII."""
    ascii_char = chr(int(byte_str, 2))
    ascii_value = ord(ascii_char)
    return f'{ascii_char}-{ascii_value:02x}'

if __name__ == "__main__":
    byte_str = input("Ingrese una representación en byte (8 bits): ")
    if len(byte_str) == 8 and all(bit in '01' for bit in byte_str):
        print(f"La representación ASCII de '{byte_str}' es: {byte_to_ascii(byte_str)}")
    else:
        print("Por favor, ingrese una representación válida en byte (8 bits).")
