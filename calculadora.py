from tkinter import Tk, Entry, Button, StringVar

class Calculadora:
    def __init__(self, master):
        master.title('Calculadora')
        master.geometry('357x420+0+0')
        master.config(bg='#333')
        master.resizable(False, False)

        self.equacao = StringVar()  # Armazenar a equação
        self.valor_entrada = ''  # Armazenar oque o usuario digitar

        # Entrada
        self.entrada = Entry(master, width=15, bg='#343434', font=('Arial', 28), textvariable=self.equacao, bd=10, relief='flat', justify='right')
        self.entrada.place(x=0, y=0)

        # Botões da Calculadora

        self.criar_botao('(', 0, 50, lambda: self.mostrar('('))
        self.criar_botao(')', 90, 50, lambda: self.mostrar(')'))
        self.criar_botao('%', 180, 50, lambda: self.mostrar('%'))
        self.criar_botao('1', 0, 125, lambda: self.mostrar(1))
        self.criar_botao('2', 90, 125, lambda: self.mostrar(2))
        self.criar_botao('3', 180, 125, lambda: self.mostrar(3))
        self.criar_botao('4', 0, 200, lambda: self.mostrar(4))
        self.criar_botao('5', 90, 200, lambda: self.mostrar(5))
        self.criar_botao('6', 180, 200, lambda: self.mostrar(6))
        self.criar_botao('7', 0, 275, lambda: self.mostrar(7))
        self.criar_botao('8', 90, 275, lambda: self.mostrar(8))
        self.criar_botao('9', 180, 275, lambda: self.mostrar(9))
        self.criar_botao('0', 90, 350, lambda: self.mostrar(0))
        self.criar_botao('.', 180, 350, lambda: self.mostrar('.'))
        self.criar_botao('+', 270, 50, lambda: self.mostrar('+'))
        self.criar_botao('-', 270, 125, lambda: self.mostrar('-'))
        self.criar_botao('/', 270, 200, lambda: self.mostrar('/'))
        self.criar_botao('x', 270, 275, lambda: self.mostrar('*'))
        self.criar_botao('=', 270, 350, self.calcular, cor_bg='#4CAF50', cor_fg='#fff')
        self.criar_botao('C', 0, 350, self.limpar, cor_bg='#FF5722', cor_fg='#fff')

        self.criar_botao ('⌫', 180, 50, self.apagar_um_caractere, cor_bg = '#343434', cor_fg= '#000')

    def criar_botao(self, texto, x, y, comando, cor_bg='#343434', cor_fg='#000'):
        Button(self.entrada.master, 
               text=texto, 
               width=5, 
               height=2, 
               font=('Arial', 16), 
               bg=cor_bg, 
               fg=cor_fg, 
               relief='solid', 
               bd=5, 
               command=comando,
               highlightthickness=0,
               activebackground='#ccc',
               activeforeground='#000').place(x=x, y=y)

    def mostrar(self, valor):
        self.valor_entrada += str(valor) 
        self.equacao.set(self.valor_entrada) 



    def limpar(self):
        self.valor_entrada = ''  
        self.equacao.set(self.valor_entrada)

    # Calcular e exibir resultados / erros

    def calcular(self):
        try:
            resultado = eval(self.valor_entrada)
            self.equacao.set(resultado)
        except Exception as e:
            self.equacao.set("Erro") 

    def apagar_um_caractere (self):
        self.valor_entrada = self.valor_entrada[:-1]
        self.equacao.set(self.valor_entrada)

# Inicializar a Calculadora.
root = Tk()
calc = Calculadora(root)
root.mainloop()