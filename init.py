""" Quero criar um programa que me ajude a praticar meu inglês, vou tentar criar algo como um pergunta e resposta para testar """
import os
import random
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabeçalho():
    print("="*30)
    print("Practice your English!".center(30))
    print("="*30)
acertos = erros = 0



words = {'how': "como", 'are': 'são', 'have': 'ter', 'where': 'onde', 'when': 'quando'}
inverted_words ={v: k for k, v in words.items()}
items = list(words.items())
items_invertidos = list(inverted_words.items())
random.shuffle(items)
random.shuffle(items_invertidos)

print("Answer in Portuguese")
for k, v in items_invertidos:
    clear_screen()
    cabeçalho()
    print(f"{k}", end='')
    resp = str(input(": ")).lower()
    if resp in v:
        print("you are sure!")
        acertos +=1
        sleep(2)
    else:
        print("You are wrong!")
        erros += 1
        sleep(2)

print("="*30)
print("Results".center(30))
print("="*30)

print(f"Total questions: {len(items_invertidos)}\nAcertos: {acertos} \nErros: {erros} \n")
if acertos > erros:
    print("You passed!")
elif acertos == erros:
    print("It's not bad, but it's not good either!")
else:
    print("You need to study more!")
print("="*30)


#print(words.keys())