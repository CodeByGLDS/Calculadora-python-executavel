import mainbackend
import customtkinter as ctk

# Configurações do tema
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

# Criando interface
interface = ctk.CTk()
interface.geometry("280x440")
interface.title("Calculadora")

# Variáveis do backend
num1 = ""
num2 = ""
operador = ""
etapa = "num1"

# Display (readonly)
display = ctk.CTkEntry(interface, width=260, height=50, font=("Arial", 24), state="readonly")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Função para atualizar display com readonly
def atualizar_display(texto):
    display.configure(state="normal")
    display.delete(0, ctk.END)
    display.insert(0, texto)
    display.configure(state="readonly")

# Mapa de operadores para o backend
mapa_operacoes = {
    "+": "soma",
    "-": "subtracao",
    "*": "multiplicacao",
    "/": "divisao",
    "**": "potencia",
    "%": "resto"
}

# Função principal dos botões
def botao_clicado(valor):
    global num1, num2, operador, etapa

    # Limpar
    if valor == "C":
        num1 = ""
        num2 = ""
        operador = ""
        etapa = "num1"
        atualizar_display("")
        return

    # Igual
    if valor == "=":
        if num1 and num2 and operador:
            # Converter números conforme a operação
            if operador == "/":
                n1 = float(num1)
                n2 = float(num2)
            else:
                n1 = int(num1)
                n2 = int(num2)

            # Chama a função do backend
            resultado = mainbackend.calculo(n1, n2, mapa_operacoes[operador])

            # Atualiza o display
            atualizar_display(str(resultado))

            # Permite continuar calculando
            num1 = str(resultado)
            num2 = ""
            operador = ""
            etapa = "num1"
        return

    # Operadores
    if valor in mapa_operacoes:
        operador = valor
        etapa = "num2"
        atualizar_display(display.get() + valor)
        return

    # Números ou vírgula
    if valor == ",":
        valor = "."

    if etapa == "num1":
        num1 += str(valor)
    else:
        num2 += str(valor)

    atualizar_display(display.get() + str(valor))

# ------------------- Botões -------------------

# Topo
topo = ["%", "**", "+"]
for col, valor in enumerate(topo):
    botao = ctk.CTkButton(
        interface, text=valor, width=60, height=60,
        command=lambda v=valor: botao_clicado(v)
    )
    botao.grid(row=1, column=col+1, padx=5, pady=5)

# Números
numeros = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
]

for linha, linha_valores in enumerate(numeros):
    for coluna, valor in enumerate(linha_valores):
        botao = ctk.CTkButton(
            interface, text=str(valor), width=60, height=60,
            command=lambda v=valor: botao_clicado(v)
        )
        botao.grid(row=linha+2, column=coluna, padx=5, pady=5)

# Lado direito
direita = ["-", "*", "/"]
for linha, valor in enumerate(direita):
    botao = ctk.CTkButton(
        interface, text=valor, width=60, height=60,
        command=lambda v=valor: botao_clicado(v)
    )
    botao.grid(row=linha+2, column=3, padx=5, pady=5)

# Última linha
ultimo = ["C", 0, ",", "="]
for coluna, valor in enumerate(ultimo):
    botao = ctk.CTkButton(
        interface, text=str(valor), width=60, height=60,
        command=lambda v=valor: botao_clicado(v)
    )
    botao.grid(row=5, column=coluna, padx=5, pady=5)

# ------------------- Mainloop -------------------
interface.mainloop()
