from tkinter import *
from translate import Translator 


screen = Tk()
screen.title("Language Translator")

InputLangChoice = StringVar()
TransLangChoice = StringVar()

LangChoice = {'English' , 'Spanish' , 'French' , 'German' , 'Japanese'}
InputLangChoice.set('English')
TransLangChoice.set('French')

def Translate():
    translator = Translator(from_lang = InputLangChoice.get(), to_lang = TransLangChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

InputLangChoiceM = OptionMenu(screen , InputLangChoice , *LangChoice)
Label(screen , text = "Choose Language").grid(row=0,column=1)
InputLangChoiceM.grid(row=1,column=1)

NewLangChoiceM = OptionMenu(screen , TransLangChoice , *LangChoice)
Label(screen , text="Translated Language").grid(row=0,column=2)
NewLangChoiceM.grid(row=1,column=2)

Label(screen, text="Enter Text").grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(screen, textvariable=TextVar, width=50).grid(row=2, column=1, columnspan=3)

Label(screen, text="Output Text").grid(row=3, column=0)
OutputVar = StringVar()
TextBox = Entry(screen, textvariable=OutputVar, width=50).grid(row=3, column=1, columnspan=3)

B = Button(screen, text="Translate", command=Translate, relief=GROOVE).grid(row=4, column=1, columnspan=3)

mainloop()