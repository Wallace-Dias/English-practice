""" Quero criar um programa que me ajude a praticar meu inglês, vou tentar criar algo como um pergunta e resposta para testar """

from random import choice

print("="*30)
print("Pratique seu inglês!".center(30))
print("="*30)

words = {'how': "como", 'are': 'são'}

""" resp = 'sã'.lower()

if resp in words.values():
    print("Certo")
else:
    print("Errado") """

print("Responda em Portuguese")
for k, v in words.items():
    print(f"{k}", end='')
    resp = str(input(": ")).lower()
    if resp in v:
        print("Você acertou!")
    else:
        print("Incorreto!")


#print(words.keys())