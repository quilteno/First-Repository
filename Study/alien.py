enemies = []

#  add 30 enemies
for enemy_number in range(30):
    new_enemy = {'color': 'green', 'points': 5, 'speed': 'slow'}
    enemies.append(new_enemy)

#  change 0 to 9 of list value
for enemy in enemies[:10]:
    if enemy['color'] == 'green':
        enemy['color'] = 'red'
        enemy['points'] = 10
        enemy['speed'] = 'midium'

for enemy in enemies:
    #  plus .values or .keys after dictionarys
    for value in enemy.values():
        if value == 'green':
            print("you get 5 points")
