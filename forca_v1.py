# -*- coding: utf-8 -*-

# Hangman Game (jogo da forca)
# Programação Orientada a Objetos

#Importando o módulo random
import random

# Board (Tabuleiro)
board = ['''
<><><><><><><><> Hangman <><><><><><><><> \n
  +----+
  |    | 
       | 
       |
       |
       |
  ==========''','''

  +----+
  |    | 
  O    | 
       |
       |
       |
  ==========''','''

  +----+
  |    | 
  O    | 
  |    |
       |
       |
  ==========''','''

  +----+
  |    | 
  O    | 
 /|    |
       |
       |
  ==========''','''

  +----+
  |    | 
  O    | 
 /|\   |
       |
       |
  ==========''','''

  +----+
  |    | 
  O    | 
 /|\   |
 /     |
       |
  ==========''','''

  +----+
  |    | 
  O    | 
 /|\   |
 / \   |
       |
  ==========''','''

  +----+
  |    | 
  º    | 
 /|\   |
 / \   |
       |
  ==========''']

#Classe
class Hangman:
    #Metodo construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []#Lista para as letras erradas
        self.guessed_letters = []#Lista para as letras corretas

    #Metodo para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    #Metodo para verificar se o jogo terminou
    def hangman_over (self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    #Metodo para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    #Metodo para não mostrar a letra no board
    def hide_word(self):
        rtn =' '
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    #Metodo para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])#len é o comprimento da lista
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ',)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print('Letras corretas: ',)
        for letter in self.guessed_letters:
            print(letter,)
            print()


#Função para ler uma palavra de forma aleatoria do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
            bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip() #Strip remove os espaços em branco no inicio e fim da palavra

#Função Main - Execução do Programa
def main():
    #Objeto
    game = Hangman(rand_word())

    #Enquanto o jogo não terminar, print do status,solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    #Verifica o status do jogo
    game.print_game_status()

    #De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print("\nParabéns! Você venceu!!!")
    else:
        print("\nGame Over! Você perdeu!")
        print("A palavra era "+ game.word)

    print("\nfoi bom jogar com você!\n")

#Executa o programa
if __name__ == "__main__":
    main()