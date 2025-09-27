import requests


class ProjectYouGile:
    def __init__(self, url) -> None:
        self.url = url
    # 1) Получить список проектов компании

    def get_project_list(self, login=None, password=None, companyID=None):
        if login and password:
            # Получаем токен и список проектов
            key = self.get_token(login=login, password=password,
                                 companyID=companyID)
            headers = {
                'Authorization': f'Bearer {key}',
                'Content-Type': 'application/json'
            }
            resp = requests.get(self.url + 'projects',
                                headers=headers, timeout=10)

            if resp.status_code == 200:
                # Проверяем что Content-Type содержит application/json
                content_type = resp.headers.get("Content-Type", "")
                assert "application/json" in content_type
                response_data = resp.json()
                # API возвращает данные в формате {'content': [...]}
                return response_data.get('content', [])
            else:
                raise ValueError(f"Ошибка получения проектов: {
                    resp.status_code} - {resp.text}")
        else:
            # Получаем список компаний, если не переданы параметры авторизации
            return self.get_companies(login=login, password=password)

    # 2) Получить ключ авторизации

    def get_token(self, login='v2084047@gmail.com', password='X3ap@fVRfRYyK6q',
                  companyID=None):
        # Если companyID не передан, получаем первую доступную компанию
        if companyID is None:
            companies = self.get_companies(login=login, password=password)
            if companies and len(companies) > 0:
                companyID = companies[0].get(
                    'id', '7343bfab-d07b-4e43-8be6-0958432ec1fa')
            else:
                companyID = '7343bfab-d07b-4e43-8be6-0958432ec1fa'  # fallback

        payload = {
            'login': login,
            'password': password,
            'companyId': companyID  # Попробуем с маленькой 'd'
        }
        # Попробуем отправить как form data
        resp = requests.post(self.url + 'auth/keys', data=payload, timeout=10)

        if resp.status_code != 201:
            raise ValueError(f"Ошибка авторизации: {
                resp.status_code} - {resp.text}")

        response_data = resp.json()
        # Проверяем что Content-Type содержит application/json
        # (может быть application/json; charset=utf-8)
        content_type = resp.headers.get("Content-Type", "")
        assert "application/json" in content_type

        # Извлекаем токен из ответа

        if 'key' in response_data:
            return response_data['key']
        else:
            raise ValueError("Токен не найден в ответе API")

    # Получить список компаний
    def get_companies(self, login, password):
        headers = {'Content-Type': 'application/json'}
        payload = {'login': login, 'password': password}
        resp = requests.post(self.url + 'auth/companies',
                             headers=headers, json=payload, timeout=10)

        if resp.status_code == 200:
            response_data = resp.json()
            # API возвращает данные в формате {'content': [...]}
            return response_data.get('content', [])
        else:
            print(f"Не удалось получить компании: {resp.status_code}")
            return []

    # 3) Создание проекта

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
                             json=project, timeout=10)

        assert resp.status_code == 201
        content_type = resp.headers.get("Content-Type", "")
        assert "application/json" in content_type
        return resp.json()

    # Альтернативное название для совместимости с тестами

    def create_proect(self, title, users=None, login=None, password=None,
                      companyID=None):
        return self.create_project(title=title, users=users, login=login,
                                   password=password, companyID=companyID)

    # 4) Получить проект по id

    def get_project_with_id(self, project_id, login=None, password=None,
                            companyID="7343bfab-d07b-4e43-8be6-0958432ec1fa"):
        key = self.get_token(login=login, password=password,
                             companyID=companyID)
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url + f'projects/{project_id}',
                            headers=headers, timeout=10)

        assert resp.status_code == 200
        content_type = resp.headers.get("Content-Type", "")
        assert "application/json" in content_type
        return resp.json()

    # Альтернативное название для совместимости с тестами

    def get_proget(self, project_id, login=None,
                   password=None, companyID=None):
        return self.get_project_with_id(project_id,
                                        login, password, companyID)

    # 5) Изменение проекта

    def edit_project(self, project_id, title=None, users=None, login=None,
                     password=None, companyID=None):
        key = self.get_token(login=login, password=password,
                             companyID=companyID)
        headers = {
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        }
        edit_data = {}
        if title:
            edit_data['title'] = title
        if users:
            edit_data['users'] = users

        resp = requests.put(self.url + f'projects/{project_id}',
                            headers=headers, json=edit_data, timeout=10)
        assert resp.status_code == 200
        content_type = resp.headers.get("Content-Type", "")
        assert "application/json" in content_type
        return resp.json()
