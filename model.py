from data import morse


class MorseConverter:

    def __init__(self):
        """Initilizes the list which the output would be returned"""
        self.output = []

    def text_morse(self, code):
        """Takes in the input and converts that to a morse code"""
        self.output.clear()
        text = list(code)
        for item in text:
            for data in morse:
                if item == data:
                    self.output.append(morse[data])
        return " ".join(self.output)

    def morse_text(self, code):
        """Takes in the morse input and converts that to text"""
        self.output.clear()
        text = code.split()
        for item in text:
            for keys, values in morse.items():
                if item == values:
                    self.output.append(keys)
        return "".join(self.output)
