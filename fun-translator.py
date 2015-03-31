sorta_japanese = {
    "a": "ka",
    "b": "zu",
    "c": "mi",
    "d": "te",
    "e": "ku",
    "f": "lu",
    "g": "ji",
    "h": "ri",
    "i": "ki",
    "j": "zus",
    "k": "me",
    "l": "ta",
    "m": "rin",
    "n": "to",
    "o": "mo",
    "p": "no",
    "q": "ke",
    "r": "shi",
    "s": "ari",
    "t": "chi",
    "u": "do",
    "v": "ru",
    "w": "mei",
    "x": "na",
    "y": "fu",
    "z": "zi"
}

def populate_japanese_uppercase():
    uppercase_sorta_japanese = {}
    for english_letter, japanese_letter in sorta_japanese.items():
        if english_letter.islower():
            upper_english_letter = english_letter.upper()
            upper_japanese_letter = japanese_letter[0].upper() + japanese_letter[1:]
            uppercase_sorta_japanese[upper_english_letter] = upper_japanese_letter
    sorta_japanese_return = sorta_japanese.copy()
    sorta_japanese_return.update(uppercase_sorta_japanese)
    return sorta_japanese_return

def translate(text, translation_mappings):
    new_str = ""
    for char in text:
        if char in translation_mappings.keys():
            new_str += translation_mappings[char]
        else:
            new_str += char

    return new_str

def main():
    translation_mappings = populate_japanese_uppercase()
    text = input("message> ")
    print(translate(text, translation_mappings))
    
if __name__ == '__main__':
    main()
