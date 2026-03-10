"""
Projeto: Analisador de Sentimentos
Autor: Pedro Henrique
Descrição:
Aplicação em Python que analisa o sentimento de frases digitadas
pelo usuário utilizando inteligência artificial.
"""

from textblob import TextBlob
import tkinter as tk
import matplotlib.pyplot as plt

positivos = 0
negativos = 0
neutros = 0


def analisar_sentimento():
    global positivos, negativos, neutros

    frase = entrada.get()

    if frase == "":
        resultado.config(text="Digite uma frase primeiro.", fg="orange")
        return

    analise = TextBlob(frase)
    sentimento = analise.sentiment.polarity

    if sentimento > 0:
        resultado.config(text="Sentimento positivo 😀", fg="#00ff9f")
        positivos += 1

    elif sentimento < 0:
        resultado.config(text="Sentimento negativo 😡", fg="#ff4c4c")
        negativos += 1

    else:
        resultado.config(text="Sentimento neutro 😐", fg="#ffd166")
        neutros += 1

    contador.config(
        text=f"Positivas: {positivos} | Negativas: {negativos} | Neutras: {neutros}"
    )

    entrada.delete(0, tk.END)


def mostrar_grafico():

    labels = ["Positivas", "Negativas", "Neutras"]
    valores = [positivos, negativos, neutros]

    plt.bar(labels, valores)

    plt.title("Resultado da Análise de Sentimentos")
    plt.ylabel("Quantidade de frases")

    plt.show()


janela = tk.Tk()
janela.title("Analisador de Sentimentos")
janela.geometry("420x320")
janela.resizable(False, False)

janela.configure(bg="#1e1e1e")


titulo = tk.Label(
    janela,
    text="ANALISADOR DE SENTIMENTOS",
    font=("Arial", 15, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=15)


entrada = tk.Entry(
    janela,
    width=40,
    font=("Arial", 11)
)

entrada.pack(pady=10)


botao = tk.Button(
    janela,
    text="Analisar",
    command=analisar_sentimento,
    bg="#4CAF50",
    fg="white",
    width=15
)

botao.pack(pady=5)


resultado = tk.Label(
    janela,
    text="Resultado aparecerá aqui",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 11)
)

resultado.pack(pady=10)


contador = tk.Label(
    janela,
    text="Positivas: 0 | Negativas: 0 | Neutras: 0",
    bg="#1e1e1e",
    fg="white"
)

contador.pack(pady=10)


botao_grafico = tk.Button(
    janela,
    text="Mostrar gráfico",
    command=mostrar_grafico,
    bg="#2196F3",
    fg="white",
    width=15
)

botao_grafico.pack(pady=10)


janela.mainloop()