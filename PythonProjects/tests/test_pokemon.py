import requests

# Данные
base_url = 'https://api.pokemonbattle.ru/v2'  
trainer_token = 'e43b7bbdb79f687c93a5d956e8a213d1'  # токен тренера
trainer_id = 37877  # ID тренера
trainer_name = "TobiBobi"  # имя тренера

headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

# 1. Проверка, что GET /trainers возвращает код 200
def test_get_trainers_status_code():
    response = requests.get(f'{base_url}/trainers')
    assert response.status_code == 200

# 2. Проверка, что имя тренера есть в ответе GET /trainers
def test_get_trainers_contains_my_name():
    response = requests.get(f'{base_url}/trainers', params={"trainer_id": trainer_id})
    assert response.status_code == 200

    trainer_data = response.json()
    print(trainer_data)  

    # Проверка, что имя тренера соответствует ожидаемому
    assert trainer_data["data"][0]["trainer_name"] == trainer_name
