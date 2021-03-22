CHAR_SEP = " "
WORD_SEP = " " * 3


def decodeMorse(morseCode):
    return " ".join(
        "".join(MORSE_CODE[c] for c in word.split(CHAR_SEP))
        for word in morseCode.strip().split(WORD_SEP)
    )


decodeMorse(".... . -.--   .--- ..- -.. .")
