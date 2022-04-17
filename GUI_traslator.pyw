from tkinter import *
from translate import Translator 
import sys

def tran():
	text = t.get('1.0', END)
	a = translator.translate(text)
	t1.delete('1.0', END)
	t1.insert('1.0', a)
def tran2():
	text1 = t.get('1.0', END)
	a1 = translator1.translate(text1)
	t1.delete('1.0', END)
	t1.insert('1.0', a1)
def tran3():
	t.delete('1.0', END)
	t1.delete('1.0', END)
def tran4():
	sys.exit()	
	
root = Tk()
root.geometry('236x230')
root.title('Переводчик')
root.configure(bg='black')

translator = Translator(from_lang = 'ru', to_lang = 'pl')
translator1 = Translator(from_lang = 'pl', to_lang = 'ru')

t = Text(root, width=25, height=5,bg = 'white',fg='black')
t.place(relx=0.07, rely=0.02)

t1 = Text(root, width=25, height=5,bg = 'white',fg='black')
t1.place(relx=0.07, rely=0.52)

b = Button(root, text='Перевести',bg = 'white',fg='black', command=tran)
b.place(relx=0.15, rely=0.4)

b1 = Button(root, text='Tłumaczyć',bg = 'white',fg='black', command=tran2)
b1.place(relx=0.57, rely=0.4)

b2 = Button(root, text='Clean',bg = 'white',fg='black', command=tran3)
b2.place(relx=0.2, rely=0.9)

b3 = Button(root, text='Exit',bg = 'white',fg='black', command=tran4)
b3.place(relx=0.65, rely=0.9)

root.mainloop()