import tkinter





button_vallues = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols =  ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]


row_count = len(button_vallues) #5
column_count = len(button_vallues[0]) #4

yellow = '#fbd026'
dark_blue = '#12282d'
green = '#8ad157'
light_gray = '#D4D4D2'
dark_gray = '#505050'
white = 'white'

#window

janela = tkinter.Tk() #cria a janela
janela.title("Calculadora Louca")
janela.resizable(False, False)

quadro = tkinter.Frame(janela)
visor =tkinter.Label(quadro, text="0", font=("Arial", 45), background=dark_blue,
                     foreground=white, anchor="e", width=column_count)

visor.grid(row=0, column=0, columnspan=column_count, sticky="we")


for row in range(row_count):
    for column in range(column_count):
        value = button_vallues[row][column]
        button = tkinter.Button(quadro, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        button.grid(row=row+1, column=column)
        
        if value in top_symbols:
            button.config(foreground=white, background=green)
        elif value in right_symbols:
            button.config(foreground=white, background=yellow)
        else:
            button.config(foreground=white, background=dark_gray)


        button.grid(row=row+1, column=column)
        


quadro.pack()

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, visor, A, B, operator

    if value in right_symbols:
        if value == '=':
            if A is not None and operator is not None:
                B = visor["text"] 
                numA = float(A)
                numB = float(B)

                if operator == '+':
                    visor["text"] = remove_zero_decimal(numA + numB)
                
                elif operator == '×':
                    visor["text"] = remove_zero_decimal(numA * numB)

                elif operator == '-':
                    visor["text"] = remove_zero_decimal(numA - numB)

                elif operator == '÷':
                    visor["text"] = remove_zero_decimal(numA / numB)

                clear_all()



        elif value in "÷×-+=":
            if operator is None:
                A = visor["text"]
                visor["text"] = '0'
                B = "0"

            operator = value

    if value in top_symbols:
        if value == "AC":
            clear_all()
            visor["text"] = '0'

        elif value == "+/-":
            result = float(visor["text"]) * -1
            visor["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(visor["text"]) / 100
            visor["text"] = remove_zero_decimal(result)
            

    else: #digito ou .
        if value == ".":
            if value not in visor["text"]:
                visor["text"] += value
        elif value in "0123456789":
            if visor["text"] == "0":
                visor["text"] = value
            
            else:
                visor["text"] += value


#center window
janela.update() #atualiza a janela com as dimensões corretas
janela_width = janela.winfo_width()
janela_height = janela.winfo_height()
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

janela_x = int((screen_width/2) - (janela_width/2))
janela_y = int((screen_height/2) - (janela_height/2))

janela.geometry(f"{janela_width}x{janela_height}+{janela_x}+{janela_y}")

janela.mainloop()

