import tkinter as tk

def clickar(numero):
    display.insert(tk.END, numero)


    

janela = tk.Tk()
janela.title('Calculadora Louca')

janela.geometry('325x390')

display = tk.Entry(janela, font=('Arial', 20), justify= 'right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

num = 1

for linha in range(0, 3):
    for coluna in range(3):
        botao = tk.Button(
            janela,
            text=(num),
            font=('Arial', 14),
            width=6,
            height=2,
            command=lambda n=num: clickar(n)
        )
        botao.grid(row=4-linha, column=coluna)
        num += 1

botao0 = tk.Button(janela, text="0", font=('Arial', 14), width=6, height=2, command=lambda: clickar(0))
botao0.grid(row=6, column=1, padx=3, pady=3)  

botaoIgual = tk.Button(janela, text="=", font=("Arial", 14), width=6, height=2, command=lambda: clickar('='))
botaoIgual.grid(row=6, column=3)

botaoDiv = tk.Button(janela, text="/", font=("Arial", 14), width=6, height=2, command=lambda: clickar('/'))
botaoDiv.grid(row=6, column=3)

botaoSoma = tk.Button(janela, text="+", font=("Arial", 14), width=6, height=2, command=lambda: clickar('+'))
botaoSoma.grid(row=4, column=3)

botaoSubt = tk.Button(janela, text="-", font=("Arial", 14), width=6, height=2, command=lambda: clickar('-'))
botaoSubt.grid(row=3, column=3)

botaoMult = tk.Button(janela, text="x", font=("Arial", 14), width=6, height=2, command=lambda: clickar('x'))
botaoMult.grid(row=2, column=3)
botaoCelan = tk.Button(janela, text="c", font=("Arial", 14), width=6, height=2, command=lambda: clickar('c'))
botaoCelan.grid(row=1, column=3)


 

janela.mainloop()