enemies = []

for enemy_number in range(30):
    new_enemy = {'color': 'green', 'points': 5, 'speed': 'slow'}
    enemies.append(new_enemy)

for enemy in enemies[:10]:
    if enemy['color'] == 'green':
        enemy['color'] = 'red'
        enemy['points'] = 10
        enemy['speed'] = 'midium'

for enemy in enemies[0:30]:
    print(enemy)
