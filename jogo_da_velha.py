import random
import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        self.criar_botoes()
        self.modo_jogo = "humano"  # Pode ser "humano" ou "maquina"

    def criar_botoes(self):
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.master, text=" ", font=("Arial", 20), width=5, height=2,
                                               command=lambda linha=i, coluna=j: self.jogar(linha, coluna))
                self.botoes[i][j].grid(row=i, column=j)

        self.modo_jogo_var = tk.StringVar(value="humano")
        tk.Radiobutton(self.master, text="Humano vs Humano", variable=self.modo_jogo_var, value="humano").grid(row=3, column=0)
        tk.Radiobutton(self.master, text="Humano vs Máquina", variable=self.modo_jogo_var, value="maquina").grid(row=3, column=1)
        tk.Button(self.master, text="Iniciar Jogo", command=self.iniciar_jogo).grid(row=4, column=0, columnspan=2)

    def iniciar_jogo(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=" ", state=tk.NORMAL)

    def jogar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.iniciar_jogo()
            elif all(cell != " " for row in self.tabuleiro for cell in row):
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.iniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
                if self.modo_jogo_var.get() == "maquina" and self.jogador_atual == "O":
                    self.jogar_maquina()

    def jogar_maquina(self):
        while True:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if self.tabuleiro[linha][coluna] == " ":
                self.jogar(linha, coluna)
                break

    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != " ":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != " ":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()