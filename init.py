""" Quero criar um programa que me ajude a praticar meu inglês, vou tentar criar algo como um pergunta e resposta para testar """
import os
from random import choice
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("="*30)
print("Pratique seu inglês!".center(30))
print("="*30)

words = {'how': "como", 'are': 'são'}

print("Responda em Portuguese")
for k, v in words.items():
    clear_screen()
    print(f"{k}", end='')
    resp = str(input(": ")).lower()
    if resp in v:
        print("Você acertou!")
        sleep(2)
    else:
        print("Incorreto!")
        sleep(2)


#print(words.keys())