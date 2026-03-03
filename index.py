import tkinter as tk

janela = tk.Tk()
janela.title('Calculadora Louca')

janela.geometry('300x400')

display = tk.Entry(janela, font=('Arial', 20), justify= 'right')

botao1= tk.Button(janela, text=('1'), font=('Arial', 18))

janela.mainloop()