# -*- coding: utf-8 -*-
"""primitivo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u6n5oR7wPHhWadzRasoTm-v-2LtXj60U
"""

a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a)) #mostra o tipo primitivo da variavel a "str"
print("Tem espaços? ", a.isspace()) #detecta quando vc dá espaço no campo
print("É um numero? ", a.isnumeric()) #detecta se é númerico
print("É alfabetico? ", a.isalpha()) #detecta se é alfabético
print("É alfanumerico? ", a.isalnum()) #detecta se é alfanumerico
print("Está em maiusculos? ", a.isupper()) #detecta se está em maiusculo
print("Está em minusculo? ", a.islower()) #detecta se está minusculo
print("Está capitalizada? ? ", a.istitle()) #detecta se está capitalizada ex: Python, João, Pedro