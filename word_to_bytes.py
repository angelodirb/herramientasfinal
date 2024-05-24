def word_to_bytes(word):
    """Convierte una palabra a su representación en bytes (binarios)."""
    return ' '.join(format(ord(char), '08b') for char in word)

if __name__ == "__main__":
    word = input("Ingrese una palabra: ")
    print(f"La representación en byte de '{word}' es: {word_to_bytes(word)}")
