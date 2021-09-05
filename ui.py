from tkinter import *
from model import MorseConverter

THEME = "#444444"


class MorseInterface:
    """class contains methods to launch the Caesar GUI"""

    def __init__(self):
        """
        Initializes the interface of the application
        """
        self.morse = MorseConverter()
        self.window = Tk()
        self.window.title('Morse Converter')
        self.window.config(bg=THEME, padx=50, pady=50)

        # Initializing the note on top
        self.note = Label(text="Type the text you'd like to convert", font=("Bookman Old Style", 18, "bold underline"),
                          bg=THEME, fg='#B2B1B9', )
        self.note.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Initializing the hints section
        self.hint = Label(text="Rule 1: Each morse letter is separated by space.\n\n"
                               "Rule 2: Space between words is represented by '~'.\n\n"
                               "Rule 3: During decrypt please follow the above two rules.",
                          font=('Helvetica', 10, "bold"), bg=THEME, fg='#FF4848')
        self.hint.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        # Initializing Input Text space
        self.input = Text(width=30, height=3, font=("Bookman Old Style", 15, "bold"), bg=THEME,
                          fg='grey70', wrap='word', )
        self.input.focus()
        self.input.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

        # Initializing choices as buttons
        self.decrypt = Button(bd=-2, highlightthickness=0, text='To Text', bg=THEME, padx=2, pady=2,
                              font=("Tahoma", 17, "bold"), fg="#D79771", command=self.decrypt_msg)
        self.decrypt.grid(row=4, column=3, rowspan=2)

        self.encrypt = Button(bd=-2, highlightthickness=0, text='To Morse', bg=THEME, padx=2, pady=2,
                              font=("Tahoma", 17, "bold"), fg="#71EFA3", command=self.encrypt_msg)
        self.encrypt.grid(row=4, column=1, rowspan=2)

        # Initializing Result space
        self.result = Text(width=30, height=3, font=("Tahoma", 15, "bold"), bg=THEME, fg='grey70', wrap='word', )
        self.result.grid(row=6, column=1, columnspan=3, padx=10, pady=10)

        # Initializing the Clear button
        self.clear = Button(bd=-2, highlightthickness=0, text='Clear', bg=THEME, padx=2, pady=2,
                            font=("Tahoma", 17, "bold"), fg="#FDE49C", command=self.delete)
        self.clear.grid(row=4, column=2, rowspan=2)

        self.window.mainloop()

    def encrypt_msg(self):
        """Function bind with the Encrypt button in the GUI to encrypt the text"""
        text1 = self.input.get("1.0", END).upper()
        message = self.morse.text_morse(text1)
        self.note.config(text="Please clear box after each output")
        self.result.insert(END, message)

    def decrypt_msg(self):
        """Function bind with the Decrypt button in the GUI to decrypt the text"""
        text = self.input.get("1.0", END)
        answer = self.morse.morse_text(text)
        self.note.config(text="Please clear box after each output")
        self.result.insert(END, answer)

    def delete(self):
        """Clears the output box"""
        self.input.delete(1.0, END)
        self.result.delete(1.0, END)
        self.note.config(text="Type the text you'd like to convert")
