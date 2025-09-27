from project_YouGile import ProjectYouGile


api = ProjectYouGile('https://ru.yougile.com/api-v2/')

# получить проекты


def test_get_proects():
    login = "v2084047@gmail.com"
    password = "X3ap@fVRfRYyK6q"

    # Сначала получаем список компаний
    companies = api.get_companies(login=login, password=password)
    if companies and len(companies) > 0:
        companyID = companies[0].get('id')
    else:
        companyID = None

    # Теперь получаем проекты
    body = api.get_project_list(login=login, password=password,
                                companyID=companyID)
    assert isinstance(body, list)  # Должен быть список
    assert len(body) >= 0  # Список может быть пустой


def test_create_project_():
    # количество проектов до
    login = "v2084047@gmail.com"
    password = "X3ap@fVRfRYyK6q"
    companyID = '7343bfab-d07b-4e43-8be6-0958432ec1fa'
    projects_before = api.get_project_list(login=login,
                                           password=password,
                                           companyID=companyID)
    len_before = len(projects_before)
    # создание проекта
    title = 'тест'
    users = {"f1146319-e7ea-4050-9cb7-56dc40f4e0cb": "admin"}
    result = api.create_project(title, users, login,
                                password, companyID)
    new_id = result['id']

    # получаем созданный проект

    new_project = api.get_project_with_id(new_id, login,
                                          password, companyID)

    # проверим название нового проекта и user_id
    assert new_project['title'] == title
    assert new_project['users'] == users

    # количество проектов после
    projects_after = api.get_project_list(login=login,
                                          password=password,
                                          companyID=companyID)
    len_after = len(projects_after)

    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == title
    assert projects_after[-1]['id'] == new_id

    # получить проект по id


def test_get_progect_with_id():
    # создание проекта
    title = 'тест'
    users = {"f1146319-e7ea-4050-9cb7-56dc40f4e0cb": "admin"}
    login = 'v2084047@gmail.com'
    password = 'X3ap@fVRfRYyK6q'
    companyID = '7343bfab-d07b-4e43-8be6-0958432ec1fa'
    result = api.create_proect(title=title, users=users,
                               login=login, password=password,
                               companyID=companyID)
    progect_id = result['id']

    # обращаемся к проекту
    new_project = api.get_proget(progect_id, login=login,
                                 password=password,
                                 companyID=companyID)

    assert new_project['title'] == "тест"
    assert new_project['users'] == {
        "f1146319-e7ea-4050-9cb7-56dc40f4e0cb": "admin"}

    # изменить информацию о проекте


def test_edit():
    title = "тест для изменения"
    users = {"f1146319-e7ea-4050-9cb7-56dc40f4e0cb": "admin"}
    login = 'v2084047@gmail.com'
    password = 'X3ap@fVRfRYyK6q'
    companyID = '7343bfab-d07b-4e43-8be6-0958432ec1fa'
    result = api.create_proect(title=title, users=users, login=login,
                               password=password, companyID=companyID)
    new_id = result["id"]

    new_title = "новый тест"
    new_users = {"f1146319-e7ea-4050-9cb7-56dc40f4e0cb": "admin"}

    edited = api.edit_project(new_id, title=new_title, users=new_users,
                              login=login, password=password,
                              companyID=companyID)

    # Проверим, что операция редактирования вернула результат
    assert edited is not None
    assert "id" in edited

    # Теперь получим обновленный проект для проверки
    updated_project = api.get_project_with_id(new_id, login=login,
                                              password=password,
                                              companyID=companyID)

    # Проверяем, что название проекта поменялось
    assert updated_project["title"] == new_title
    # Проверяем, что users не поменялся
    assert updated_project["users"] == new_users
