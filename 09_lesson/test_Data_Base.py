from sqlalchemy import create_engine, text


# В консоле DBeaver:
# SELECT subject_id, subject_title FROM public.subject;
# INSERT INTO public.subjet(subjet_id, subjet_title)
# VALUES (16, 'Gastronomy');
# UPDATE public.subjet SET subject_id=16,
# subjet_title='Astronomy' where subject_id=16;
# DELETE FROM public.subjet where subject_id=16
# and subject_title='Astronomy';

db_connection_string = "postgresql://postgres:MAK@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    names = db.table_names()
    assert names[1] == 'subject'


def connection():
    conn = db.connect()
    trans = conn.begin()  # Рачинаем транзакцию
    yield conn
    trans.commit()  # Откатываем изменения после теста
    conn.close()

    # Добавить предмет


def test_insert_subject():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO public.subject(\"subject_id\", \"subject_title\")"
               "VALUES (:id, :title)")
    my_params = {
        "id": 16,
        "title": 'Gastronomy'
    }

    result = db.execute(sql, my_params)
    rows = result
    print(rows)
    # db.commit() # Сохраняем изменения

    # Проверка, что предмет был добавлен
    result = db.execute(text("SELECT subject_title FROM subject"
                             " WHERE subject_id = :id"), {"id": 16})
    title = result.fetchone()
    assert title[0] == 'Gastronomy'  # Проверяем что предмет был добавлен

    # Обновление записи предмета


def test_update_subject_title():
    db = create_engine(db_connection_string)
    sql = text("UPDATE subject SET subject_title = :title "
               "WHERE subject_id= :id")
    db.execute(sql, {"title": 'Astronomy', "id": 16})
    # db.commit() # Сохраняем изменения

    # Проверка, что запись предмета была обновлена
    result = db.execute(text("SELECT subject_title FROM subject "
                             "WHERE subject_id=subject_id"), {"id": 16})
    title = result.fetchone()
    assert title[0] == 'Astronomy'  # Проверяем, что запись обновлена

    # Удаление записи предмета


def test_delete_subject():
    db = create_engine(db_connection_string)
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, {"id": 16})

    # Проверка, что запись была удалена
    result = db.execute(text("SELECT subject_title FROM subject "
                             "WHERE subject_id = :id"), {"id": 16})
    title = result.fetchone()
    assert title is None
