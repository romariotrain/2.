import requests as requests



URL = 'https://akabab.github.io/superhero-api/api'

superheroes_ids = {'Hulk': '332', 'Thanos': '655', 'Capitan America': '149'}

superheroes_stats = []

for id in superheroes_ids:
    response = requests.get(URL + '/powerstats/' + superheroes_ids[id] + '.json')
    superhero_stats = {id: response.json()}
    superheroes_stats.append(superhero_stats)

superheroes_int = []

for superhero in superheroes_stats:
    for stat in superhero:
        intelligence = superhero[stat]['intelligence']
        superhero_int = {stat: intelligence}
        superheroes_int.append(superhero_int)


genius_int = 0
for hero in superheroes_int:
    for int_ in hero:
        if hero[int_] > genius_int:
            genius_int = hero[int_]
            genius = int_
print(f' Самый умный {genius}')