import requests


def test_put_complet_true():
    """Создать задачу, проставить отметку о выполнении и проверить что completed ==True"""
    body = {"title": "ck", "completed": False}
    # Создаём задачу
    response = requests.post(url="https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    # Редактируем созданную ранее задачу
    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200

    # Проверяем что completed ==True после изменения
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['completed'] == True, f'На самом деле значение {response.json()['completed']}'
