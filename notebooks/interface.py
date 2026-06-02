import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from graficos import (
    grafico_cancelamentos,
    grafico_duracao,
    grafico_idade,
    grafico_assinatura,
    grafico_sexo,
    grafico_callcenter
)


class Dashboard:

    def __init__(self, root):

        self.root = root
        self.root.title("Dashboard de Cancelamentos")
        self.root.geometry("1200x800")

        # Menu lateral
        menu = tk.Frame(root, bg="#2c3e50", width=250)
        menu.pack(side="left", fill="y")

        # Área do gráfico
        self.area = tk.Frame(root)
        self.area.pack(side="right", fill="both", expand=True)


        botoes = [
            ("Cancel em Geral", grafico_cancelamentos),
            ("Cancel Duração Contrato", grafico_duracao),
            ("Cancel por Idade", grafico_idade),
            ("Cancel tipo Assinatura", grafico_assinatura),
            ("Cancel por Sexo", grafico_sexo),
            ("Cancel ligações", grafico_callcenter)
        ]

        for texto, funcao in botoes:
            tk.Button(
                menu,
                text=texto,
                width=25,
                height=2,
                command=lambda f=funcao: self.mostrar_grafico(f)
            ).pack(pady=5)

    def mostrar_grafico(self, funcao):

    # limpa tela
        for widget in self.area.winfo_children():
            widget.destroy()

        fig = funcao()

        canvas = FigureCanvasTkAgg(fig, master=self.area)
        canvas.draw()

        canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()