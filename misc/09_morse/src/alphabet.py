
__all__ = ["eng", "rus"]

nums = {
    "1": ".----", "2": "..___", "3": "...__", "4": "...._",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----",
}

eng = {
    "a": ".-",   "b": "-...", "c": "-.-.", "d": "-..",
    "e": ".",    "f": "..-.", "g": "--.",  "h": "....",
    "i": "..",   "j": ".---", "k": "-.-",  "l": ".-..",
    "m": "--",   "n": "-.",   "o": "---",  "p": ".--.",
    "q": "--.-", "r": ".-.",  "s": "...",  "t": "-",
    "u": "..-",  "v": "...-", "w": ".--",  "x": "-..-",
    "y": "-.--", "z": "--..",
}

rus = {
    "а": ".-",   "б": "-...",    "в": ".--",    "г": "--.",
    "д": "-..",  "е": ".",       "ж": "...-",   "з": "--..",
    "и": "..",   "й": ".---",    "к": "-.-",    "л": ".-..",
    "м": "--",   "н": "-.",      "о": "---",    "п": ".--.",
    "р": ".-.",  "с": "...",     "т": "-",      "у": "..-",
    "ф": "..-.", "х": "....",    "ц": "-.-.",   "ч": "---.",
    "ш": "----", "щ": "--.-",    "ъ": ".--.-.", "ы": "-.--",
    "ь": "-..-", "э": "...-...", "ю": "..--",   "я": ".-.-",
}

eng.update(nums)
rus.update(nums)