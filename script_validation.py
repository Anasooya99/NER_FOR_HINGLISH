from indic_transliteration import sanscript

def is_devanagari(word):
    try:
        # Attempt to transliterate the word to Devanagari
        _ = sanscript.transliterate(word, sanscript.IAST, sanscript.DEVANAGARI)
        return True
    except ValueError:
        return False

def filter_devanagari_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        words = input_file.read().split()

    devanagari_words = [word for word in words if is_devanagari(word)]

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(" ".join(devanagari_words))

if __name__ == "__main__":
    input_filename = "data_0.txt"
    output_filename = "devanagari_words.txt"

    filter_devanagari_words(input_filename, output_filename)
