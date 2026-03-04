import tkinter as tk

def clickar(numero):
    display.insert(tk.END, numero)
    

janela = tk.Tk()
janela.title('Calculadora Louca')

janela.geometry('320x400')

display = tk.Entry(janela, font=('Arial', 20), justify= 'right')
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

num = 1

for linha in range(3, 0, -1):
    for coluna in range(3):
        botao = tk.Button(
            janela,
            text=(num),
            font=('Arial', 18),
            width=6,
            height=1,
            command=lambda n=num: clickar(n)
        )
        botao.grid(row=4-linha, column=coluna, padx=5, pady=5)
        num += 1

botao0 = tk.Button(janela, text="0", font=('Arial', 18), width=5, command=lambda: clickar(0))
botao0.grid(row=4, column=1, padx=5, pady=5)   

janela.mainloop()