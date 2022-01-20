import json

file = open('pokemon_full.json')
pokemon_string = file.read()
print('Количество символов в файле:', len(pokemon_string))

c = 0
for symvol in pokemon_string:
    if symvol.isalnum():
        c += 1
print('Количество символов в файле без пробелов и знаков препинания:', c)

pokemon_full_list = json.loads(pokemon_string)
max_lenght = 0
pokemon_name = ' '
for imya in pokemon_full_list:
    max_lenght = max(len(imya['description']), max_lenght)
    if len(imya['description']) == max_lenght:
        pokemon_name = imya['name']
print('Длина:', max_lenght, 'Покемон:', pokemon_name)
max_lenght = 0
max_ability = ' '
for abilities in pokemon_full_list:
    for ability in abilities['abilities']:
        max_lenght = max(len(ability.split()), max_lenght)
        if max_lenght == len(ability.split()):
            max_ability = ability
print('Умение: ', max_ability)
file.close()
