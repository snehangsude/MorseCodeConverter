from data import morse


class MorseConverter:

    def __init__(self):
        self.output = []

    def text_morse(self, code):
        self.output.clear()
        text = list(code)
        for item in text:
            for data in morse:
                if item == data:
                    self.output.append(morse[data])
        return " ".join(self.output)

    def morse_text(self, code):
        self.output.clear()
        text = code.split()
        for item in text:
            for keys, values in morse.items():
                if item == values:
                    self.output.append(keys)
        return "".join(self.output)
