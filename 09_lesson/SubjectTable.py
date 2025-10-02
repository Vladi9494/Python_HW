from sqlalchemy import create_engine
from sqlalchemy.sql import text
import requests


class SubjectTable:
    scripts = {
        "select": text("SELECT * FROM public.subject"
                       "WHERE deleted_at IS NULL"),
        "select_active": text("SELECT * FROM public.subject "
                              "WHERE \"is_active\" = true"
                              "AND deleted_at IS NULL"),
        "delete_by_id": text("DELETE FROM public.subject "
                             "WHERE id = :id_to_delete"),
        "insert_new": text("INSERT INTO public.subject"
                           "(\"subject_id, subject_title\")"
                           "values (:new_subject_id, :new_subject_title)"),
        "get_max_id": text("SELECT MAX(\"id\") FROM subject"
                           "WHERE deleted_at IS NULL"),
        "select by id": text("SELECT * FROM subject "
                             "WHERE id =:select_id AND deleted_at IS NULL")
        }


def __init__(self, connection_string):
    self.__db = create_engine(connection_string)


def get_subjects(self):
    return self.__db.execute(self.__scripts["select"]).fetchall()


def get_active_subjects(self):
    return self.__db.execute(self.__scripts["select_active"]).fetchall()


def delete(self, id):
    self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)


def create(self, subject_id, subject_title):
    self.__db.execute(self.__scripts[
                       "insert_new"], new_subject_id=subject_id,
                      new_subject_title=subject_title)


def get_max_id(self):
    return self.__db.execute(self.__scripts[
                        "get_max_id"]).fetchall()[0][0]


def get_subject_by_id(self, id):
    return self.__db.execute(self.__scripts[
                        "select by id"], select_id=id).fetchall()


def set_active_state(self, id, is_active):
    client_token = self.get_token()

    url_with_token = f"{self.url}/subject/status_update/{
                        id}?client_token={client_token}"
    resp = requests.patch(url_with_token,
                          json={"is_active": is_active})
    return resp.json()
