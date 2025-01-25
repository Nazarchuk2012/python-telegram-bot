import random
import json

data = None

try:
    with open('text.txt','r') as file:
        data = file.read()
except FileNotFoundError:
    print('Створений новий файл ...')
    with open('text.txt', 'w') as file:
        file.write('По замовчуванню ...')
finally:
    if not data:
        with open('text.txt', 'r') as file:
            data = file.read()

print(data)
















