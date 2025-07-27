import requests

# Данные
base_url = 'https://api.pokemonbattle.ru/v2'
trainer_token = 'e43b7b0db79f687c93a5d956e8a213d1'
trainer_id = 37877

headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

# 1. POST /pokemons — создание покемона
create_payload = {
    "name": "11111",
    "photo_id": 17
}

response_create = requests.post(f'{base_url}/pokemons', json=create_payload, headers=headers)
response_json = response_create.json()
print("Создание покемона:\n", response_json)

# Проверка наличия ID
if 'id' in response_json:
    pokemon_id = response_json['id']
else:
    print(response_json)

    exit()

# 2. PUT /pokemons — смена имени покемона
update_payload = {
    "pokemon_id": pokemon_id,
    "name": "333333",
    "photo_id": 5
}

response_update = requests.put(f'{base_url}/pokemons', json=update_payload, headers=headers)
print(response_update.json())

# 3. POST /trainers/add_pokeball — поймать покемона
catch_payload = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(f'{base_url}/trainers/add_pokeball', json=catch_payload, headers=headers)
print("\nПоймать в покебол :\n", response_catch.json())
