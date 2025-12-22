def read_write_files():
    with open("python/files/Alice.txt", "r") as file:
        text = file.read()
        print(len(text))
        cleaned_text = ""
        for char in text:
            if char.isalpha() or char.isspace():
                cleaned_text += char
    return cleaned_text

def count_words(cleaned_text):
    dict_words = {}
    for word in cleaned_text.split():
        clean = word.lower()
        if clean in dict_words:
            dict_words[clean] += 1
        else:
            dict_words[clean] = 1
    return dict_words

def find_most_common_word(dict_words):
    word, amount = "", 0 
    for words, count in dict_words.items():
        if count > amount:
            word, amount = words, count
    print(f"The most common word is '{word}' which appears {amount} times.") 

def main():
    cleaned_text = read_write_files()
    dict_words = count_words(cleaned_text)
    find_most_common_word(dict_words)