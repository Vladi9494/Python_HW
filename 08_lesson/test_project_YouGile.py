from project_YouGile import ProjectYouGile

api = ProjectYouGile('https://ru.yougile.com/api-v2/')


# получить проекты
def test_get_proects():
    body = api.get_project_list() # что значит ошибка нет атрибута?
    assert len(body) > 0


def test_create_project_():
    # количество проектов до
    login = "maximovvlad369@gmail.com"
    password = "Testing"
    companyID = 'c9b67574-af0e-4909-aba1-8a499c657e64'
    projects_before = api.get_project_list(login=login, # нет атрибута?
                                           password=password, companyID=companyID)
    len_before = len(projects_before)
    # создание проекта
    title = 'тест'
    users = {"c0504647-d568-41d5-8c03-2dfb89317907": "admin"}
    result = api.create_project(title, users, login, password, companyID)
    new_id = result['id']

    # обращаемся к проекту
    new_project = api.create_project(title, users, new_id)

    # проверим название нового проекта и user_id
    assert new_project['title'] == title
    assert new_project['users'] == users

    # количество проектов после
    projects_after = api.get_project_list(login=login,
                                          password=password)
    len_after = len(projects_after)

    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == title
    assert projects_after[-1]['id'] == new_id

    # получить проект по id


def test_get_progect_with_id():
    # создание проекта
    result = api.create_progect(title='тест', login='maximovvlad369@gmail.com', password='Testing', companyID='c9b67574-af0e-4909-aba1-8a499c657e64') # нет атрибута?
    progect_id = result['id']

    # обращаемся к проекту
    new_project = api.get_proget(progect_id)

    assert new_project['title'] == "тест"
    assert new_project['user'] == {"c0504647-d568-41d5-8c03-2dfb89317907"
                                   ":" "admin"}

    # изменить информацию о проекте


def test_edit():
    title = "новый тест"
    users = "c0504647-d568-41d5-8c03-2dfb8931790title7"
    result = api.create_proect(title=title, users=users) # нет атрибута?
    new_id = result["id"]

    new_title = "новый тест"
    users = "c0504647-d568-41d5-8c03-2dfb89317907"

    edited = api.edit_project(new_id, new_title, users)

    # Проверяем, что название проекта поменялось
    assert edited["title"] == new_title
    # Проверяем, что users не поменялся
    assert edited["users"] == users
