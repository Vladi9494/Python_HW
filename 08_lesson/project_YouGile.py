import requests


class ProjectYouGile:
    def __init__(self, url) -> None:
        self.url = url

# 1) Получить список проектов компании (получить id компании)


def get_project_list(self, login, password): 
    headers = {'Content-Type': 'application/json'}
    payload = {'login': login, 'password': password}
    resp = requests.post(self.url + 'auth/companies',
                         headers=headers, json=payload)
    resp = resp.json()

    assert resp.headers["Content-Type"] == "application/json"
    assert resp.status_code == 200

    # 2) Получить ключ авторизации


def get_token(self, login='maximovvlad369@gmail.com', password='Testing',
              companyID='c9b67574-af0e-4909-aba1-8a499c657e64'):
    payload = {
        'login': login,
        'password': password,
        'companyID': companyID
    }
    resp = requests.post(self.url + 'auth/keys', json=payload)
    responce_data = resp.json()

    assert resp.status_code == 201
    assert resp.json()["user_token"] is not None
    assert resp.headers["Content-Type"] == "application/json"

    # Извлекаем токен из ответа
    if 'key' in responce_data:
        return responce_data['key']
    else:
        raise ValueError("Токен не найден в ответе API")

    # 3 Создание проекта


def create_project(self, title, users, login, password, companyID):
    key = self.get_token(login=login, password=password,
                         companyID=companyID)
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    project = {
        'title': title,
        'users': users
    }
    resp = requests.post(self.url + 'projects',
                         headers=headers,
                         json=project)
    key = resp.json()
    assert resp.status_code == 201
    assert resp.headers["Content-Type"] == "application/json"
    assert resp.json()["user_token"] is not None

# 4) Получить проект по id


def get_project_with_id(self, project_id, login, password,
                        companyID="ed03f3ea-61df-40fd-9177-0c47f554604f"):
    key = self.get_token(login=login, password=password,
                         companyID=companyID)
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    resp = requests.get(self.url + f'progects/{project_id}',
                        headers=headers)
    key = resp.json()

    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    assert resp.json()["user_token"] is not None


# 5) Изменение проекта
def edit_project(self, project_id, login, password, companyID):
    key = self.get_token(login=login, password=password, companyID=companyID)
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    edit_project = {
        'title': "новый тест",
        'users': {"c0504647-d568-41d5-8c03-2dfb89317907": "admin"}
    }
    resp = requests.put(self.url + f'progects/{project_id}',
                        headers=headers, json=edit_project)
    key = resp.json()

    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    assert edit_project["title"] == "новый тест"
