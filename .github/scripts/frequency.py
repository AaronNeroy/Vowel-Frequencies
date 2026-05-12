import sys
from collections import Counter

def count_vowels(file_path):
    vowels = "aeiou"
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read().lower()
            text = ''.join(char for char in text if char.isalpha() or char == ' ')
        counts = Counter(char for char in text if char in vowels)
        return counts
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 frequency.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    counts = count_vowels(file_path)
    output = ', '.join(f"{v}:{counts[v]}" for v in 'aeiou' if v in counts)
    print(output)
