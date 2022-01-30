from tkinter import *
from tkinter import messagebox as mb
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, Date, create_engine, CheckConstraint, Index, DDL, event, Numeric
from sqlalchemy_utils import database_exists, create_database, drop_database
import re

root = Tk()
root.title("Physical development")
root.geometry("1555x720")  # размер окна

metadata = MetaData()
engine = None
url = None


def create_db(btn, entry):  # создание или присоединение к базе данных
    def changer():
        global metadata, engine, url
        if entry.get() == "":
            mb.showwarning("WARNING", message="Wrong DB name")
            return changer
        url = "postgresql+psycopg2://postgres:postgres@localhost:5432/" + str(entry.get())
        if not database_exists(url):
            create_database(url)
            mb.showinfo("Database creation", message="Created new database {}".format(str(entry.get())))
        else:
            mb.showinfo("Database creation", message="Connected to database {}".format(str(entry.get())))
        engine = create_engine(url, echo=False)
        metadata.bind = engine
        metadata.reflect()
    return changer


def insert_init_data(btn):
    def changer():
        global metadata, url
        if url is not None:
            metadata.drop_all()
            metadata.clear()
            customers_table = Table('Клиентская база', metadata,
                                    Column('Идентификатор', Integer, autoincrement=False, primary_key=True),
                                    Column('Фамилия', String),
                                    Column('Имя', String),
                                    Column('Отчество', String),
                                    extend_existing=True)

            customers_email_table = Table('Почты клиентов', metadata,
                                          Column('Идентификатор', Integer,
                                                 ForeignKey('Клиентская база.Идентификатор', onupdate='CASCADE',
                                                            ondelete='CASCADE'), primary_key=True),
                                          Column('Почта', String),
                                          extend_existing=True)

            provider_table = Table('Поставщики', metadata,
                                   Column('Наименование', String, primary_key=True),
                                   Column('Оценка', Integer, CheckConstraint('Оценка>=0 AND Оценка<=5')),
                                   extend_existing=True)

            subscribe_table = Table('Подписки', metadata,
                                    Column('Название', String, primary_key=True),
                                    Column('Описание', String),
                                    Column('Стоимость за день', Integer, nullable=False),
                                    Column('Поставщик', String,
                                           ForeignKey('Поставщики.Наименование', onupdate='CASCADE',
                                                      ondelete='CASCADE')),
                                    extend_existing=True)
            Index("description_index", subscribe_table.c.Описание)

            subscribe_contacts_table = Table('Контакты', metadata,
                                             Column('Название', String,
                                                    ForeignKey('Подписки.Название', onupdate='CASCADE',
                                                               ondelete='CASCADE'),
                                                    primary_key=True),
                                             Column('Почта', String),
                                             extend_existing=True)

            subscribe_var_table = Table('Варианты подписки', metadata,
                                        Column('Вариант', Integer, autoincrement=False, primary_key=True),
                                        Column('Наценка, %', Integer, nullable=False),
                                        extend_existing=True)

            contracts_table = Table('Договоры', metadata,
                                    Column('Номер', Integer, autoincrement=False, primary_key=True),
                                    Column('Идентификатор клиента', Integer,
                                           ForeignKey('Клиентская база.Идентификатор', onupdate='CASCADE',
                                                      ondelete='CASCADE')),
                                    Column('Название подписки', String,
                                           ForeignKey('Подписки.Название', onupdate='CASCADE', ondelete='CASCADE')),
                                    Column('Вариант подписки', Integer,
                                           ForeignKey('Варианты подписки.Вариант', onupdate='CASCADE',
                                                      ondelete='CASCADE')),
                                    Column('Дата заключения', Date, nullable=False),
                                    Column('Дата окончания', Date, nullable=False),
                                    extend_existing=True)

            sums_table = Table('Итоговая сумма', metadata,
                               Column('Номер договора', Integer,
                                      ForeignKey('Договоры.Номер', onupdate='CASCADE', ondelete='CASCADE'),
                                      primary_key=True),
                               Column('Оплаченная сумма', Numeric(10, 2), nullable=False),
                               extend_existing=True)

            metadata.create_all()

            # триггер
            # func = DDL(
            #     "CREATE OR REPLACE FUNCTION update_paid_amount()"
            #     " RETURNS trigger AS $$ "
            #     " BEGIN "
            #     " NEW.\"Вариант подписки\" := 3"
            #     " RETURN NEW; "
            #     " END; $$ LANGUAGE PLPGSQL"
            # )
            # global trigger
            # trigger = DDL("CREATE TRIGGER update_paid_amount AFTER UPDATE OR INSERT ON metadata.tables[Договоры]"
            #               " FOR EACH ROW EXECUTE PROCEDURE update_paid_amount();")
            # event.listen(
            #     metadata.tables["Договоры"],
            #     'after_create',
            #     func.execute_if(dialect='postgresql')
            # )
            # event.listen(
            #     metadata.tables["Договоры"],
            #     'after_create',
            #     trigger.execute_if(dialect='postgresql')
            # )

            # update table Договоры 1: "1" "IVI" "1" "1999-5-5" "1999-5-7"
            # update table Варианты подписки 3: "1000"
            # insert table Договоры 1: "21" "1" "IVI" "1" "1999-5-5" "1999-5-7"
            t1 = text("create or replace function sums_count_update() \
            returns trigger as \
            $$ \
            begin update \"Итоговая сумма\"\
            set \"Оплаченная сумма\" = (select (Договоры.\"Дата окончания\"::date - Договоры.\"Дата заключения\"::date) * Подписки.\"Стоимость за день\" * (100 + \"Варианты подписки\".\"Наценка, %\")/100) \
            from Договоры, Подписки, \"Варианты подписки\" where Подписки.Название = Договоры.\"Название подписки\" and \"Варианты подписки\".Вариант = Договоры.\"Вариант подписки\" and \"Итоговая сумма\".\"Номер договора\" = Договоры.Номер;\
            return new; \
            end; \
            $$ language plpgsql; \
            drop trigger if exists sums_update on \"Итоговая сумма\";\n\
            CREATE TRIGGER sums_update AFTER INSERT ON \"Итоговая сумма\" \
            FOR EACH ROW EXECUTE PROCEDURE sums_count_update();\n\
            drop trigger if exists contracts_update_sums on Договоры;\n\
            CREATE TRIGGER contracts_update_sums AFTER UPDATE ON Договоры \
            FOR EACH ROW EXECUTE PROCEDURE sums_count_update();\n\
            drop trigger if exists subscribe_var_update_sums on \"Варианты подписки\";\n\
            CREATE TRIGGER subscribe_var_update_sums AFTER UPDATE ON \"Варианты подписки\" \
            FOR EACH ROW EXECUTE PROCEDURE sums_count_update();\n\
            drop trigger if exists subscribe_update_sums on Подписки;\n\
            CREATE TRIGGER subscribe_update_sums AFTER UPDATE ON Подписки \
            FOR EACH ROW EXECUTE PROCEDURE sums_count_update();")
            metadata.bind.execute(t1)

            customers_insert = customers_table.insert()
            # print(customers_insert)
            customers_insert.compile()
            customers_insert.execute(
                [{'Идентификатор': 1, 'Фамилия': 'Степанова', 'Имя': 'Валерия', 'Отчество': 'Вячеславовна'},
                 {'Идентификатор': 2, 'Фамилия': 'Якушева', 'Имя': 'Алина', 'Отчество': 'Сергеевна'},
                 {'Идентификатор': 3, 'Фамилия': 'Соловьёв', 'Имя': 'Роман', 'Отчество': 'Геннадьевич'},
                 {'Идентификатор': 4, 'Фамилия': 'Иванов', 'Имя': 'Михаил', 'Отчество': 'Валерьевич'},
                 {'Идентификатор': 5, 'Фамилия': 'Кононова', 'Имя': 'Мария', 'Отчество': 'Дмитриевна'},
                 {'Идентификатор': 6, 'Фамилия': 'Мельников', 'Имя': 'Павел', 'Отчество': 'Алексеевич'},
                 {'Идентификатор': 7, 'Фамилия': 'Трофимова', 'Имя': 'Юлия', 'Отчество': 'Андреевна'},
                 {'Идентификатор': 8, 'Фамилия': 'Большакова', 'Имя': 'Татьяна', 'Отчество': 'Николаевна'},
                 {'Идентификатор': 9, 'Фамилия': 'Калинин', 'Имя': 'Антон', 'Отчество': 'Игоревич'},
                 {'Идентификатор': 10, 'Фамилия': 'Краснов', 'Имя': 'Дмитрий', 'Отчество': 'Андреевич'}])

            customers_email_insert = customers_email_table.insert()
            # print(customers_email_insert)
            customers_email_insert.compile()
            customers_email_insert.execute([{'Идентификатор': 1, 'Почта': 'vstep86@gmail.com'},
                                            {'Идентификатор': 2, 'Почта': 'yakusheva-5@mail.ru'},
                                            {'Идентификатор': 3, 'Почта': 'soloveiroman@yandex.ru'},
                                            {'Идентификатор': 4, 'Почта': 'ivanov_m@gmail.com'},
                                            {'Идентификатор': 5, 'Почта': 'marykononova3@yandex.ru'},
                                            {'Идентификатор': 6, 'Почта': 'pavelmel@mail.ru'},
                                            {'Идентификатор': 7, 'Почта': 'Julia9419@rambler.ru'},
                                            {'Идентификатор': 8, 'Почта': 'tatianabolsh@mail.ru'},
                                            {'Идентификатор': 9, 'Почта': 'kalininanton@list.ru'},
                                            {'Идентификатор': 10, 'Почта': 'krasnovdima@yandex.ru'}])

            provider_insert = provider_table.insert()
            # print(provider_insert)
            provider_insert.compile()
            provider_insert.execute([{'Наименование': 'Conde Nast Publications', 'Оценка': 3},
                                     {'Наименование': 'Hachette', 'Оценка': 4},
                                     {'Наименование': '20th Century Fox', 'Оценка': 5},
                                     {'Наименование': 'Lionsgate', 'Оценка': 4},
                                     {'Наименование': 'AAAS', 'Оценка': 5},
                                     {'Наименование': 'МФПУ Синергия', 'Оценка': 4},
                                     {'Наименование': 'Soundtrap', 'Оценка': 3},
                                     {'Наименование': 'Access Industries', 'Оценка': 3},
                                     {'Наименование': 'Google', 'Оценка': 5}])

            subscribe_insert = subscribe_table.insert()
            # print(subscribe_insert)
            subscribe_insert.compile()
            subscribe_insert.execute(
                [{'Название': 'Vogue', 'Описание': 'Журнал', 'Стоимость за день': 100,
                  'Поставщик': 'Conde Nast Publications'},
                 {'Название': 'GQ', 'Описание': 'Журнал', 'Стоимость за день': 300, 'Поставщик': 'Conde Nast Publications'},
                 {'Название': 'ELLE', 'Описание': 'Журнал', 'Стоимость за день': 400, 'Поставщик': 'Hachette'},
                 {'Название': 'Science', 'Описание': 'Журнал', 'Стоимость за день': 200, 'Поставщик': 'AAAS'},
                 {'Название': 'Прикладная информатика', 'Описание': 'Журнал', 'Стоимость за день': 100,
                  'Поставщик': 'МФПУ Синергия'},
                 {'Название': 'IVI', 'Описание': 'Онлайн-кинотеатр', 'Стоимость за день': 500,
                  'Поставщик': '20th Century Fox'},
                 {'Название': 'OKKO', 'Описание': 'Онлайн-кинотеатр', 'Стоимость за день': 900,
                  'Поставщик': '20th Century Fox'},
                 {'Название': 'Netflix', 'Описание': 'Стриминговый сервис фильмов и сериалов', 'Стоимость за день': 800,
                  'Поставщик': 'Lionsgate'},
                 {'Название': 'Spotify', 'Описание': 'Стриминговый музыкальный сервис', 'Стоимость за день': 300,
                  'Поставщик': 'Soundtrap'},
                 {'Название': 'Deezer', 'Описание': 'Стриминговый музыкальный сервис', 'Стоимость за день': 600,
                  'Поставщик': 'Access Industries'},
                 {'Название': 'SoundCloud', 'Описание': 'Стриминговый музыкальный сервис', 'Стоимость за день': 1000,
                  'Поставщик': 'Access Industries'},
                 {'Название': 'YouTube', 'Описание': 'Видеохостинг', 'Стоимость за день': 400, 'Поставщик': 'Google'}])

            subscribe_contacts_insert = subscribe_contacts_table.insert()
            # print(subscribe_contacts_insert)
            subscribe_contacts_insert.compile()
            subscribe_contacts_insert.execute([{'Название': 'Vogue', 'Почта': 'info@vogue.ru'},
                                               {'Название': 'GQ', 'Почта': 'web@gq.ru'},
                                               {'Название': 'ELLE', 'Почта': 'podpiska@hspub.ru'},
                                               {'Название': 'Science', 'Почта': 'bik@sfu-kras.ru'},
                                               {'Название': 'Прикладная информатика', 'Почта': 'arozantsev@synergy.ru'},
                                               {'Название': 'IVI', 'Почта': 'support@ivi.ru'},
                                               {'Название': 'OKKO', 'Почта': 'mail@okko.tv'},
                                               {'Название': 'Netflix', 'Почта': 'mail@okko.tv'},
                                               {'Название': 'Spotify', 'Почта': 'support@spotify.com'},
                                               {'Название': 'Deezer', 'Почта': 'support@deezer.com'},
                                               {'Название': 'SoundCloud', 'Почта': 'support@soundcloud.com'},
                                               {'Название': 'YouTube', 'Почта': 'legal@support.youtube.com'}])

            subscribe_var_insert = subscribe_var_table.insert()
            # print(subscribe_var_insert)
            subscribe_var_insert.compile()
            subscribe_var_insert.execute([{'Вариант': 1, 'Наценка, %': 0},
                                          {'Вариант': 2, 'Наценка, %': 25},
                                          {'Вариант': 3, 'Наценка, %': 50}])

            contracts_insert = contracts_table.insert()
            # print(contracts_insert)
            contracts_insert.compile()
            contracts_insert.execute(
                [{'Номер': 1, 'Идентификатор клиента': 1, 'Название подписки': 'ELLE', 'Вариант подписки': 1,
                  'Дата заключения': '2018-07-15', 'Дата окончания': '2020-04-20'},
                 {'Номер': 2, 'Идентификатор клиента': 2, 'Название подписки': 'IVI', 'Вариант подписки': 3,
                  'Дата заключения': '2018-11-15', 'Дата окончания': '2020-06-24'},
                 {'Номер': 3, 'Идентификатор клиента': 3, 'Название подписки': 'Spotify',
                  'Вариант подписки': 2, 'Дата заключения': '2019-04-09', 'Дата окончания': '2021-09-18'},
                 {'Номер': 4, 'Идентификатор клиента': 4, 'Название подписки': 'Netflix',
                  'Вариант подписки': 1, 'Дата заключения': '2019-04-15', 'Дата окончания': '2020-05-16'},
                 {'Номер': 5, 'Идентификатор клиента': 5, 'Название подписки': 'YouTube',
                  'Вариант подписки': 2, 'Дата заключения': '2019-05-04', 'Дата окончания': '2021-01-18'},
                 {'Номер': 6, 'Идентификатор клиента': 6, 'Название подписки': 'Science',
                  'Вариант подписки': 3, 'Дата заключения': '2019-06-05', 'Дата окончания': '2021-01-22'},
                 {'Номер': 7, 'Идентификатор клиента': 7, 'Название подписки': 'OKKO', 'Вариант подписки': 2,
                  'Дата заключения': '2019-07-14', 'Дата окончания': '2021-11-25'},
                 {'Номер': 8, 'Идентификатор клиента': 8, 'Название подписки': 'SoundCloud',
                  'Вариант подписки': 1, 'Дата заключения': '2019-10-17', 'Дата окончания': '2020-06-28'},
                 {'Номер': 9, 'Идентификатор клиента': 9, 'Название подписки': 'Vogue', 'Вариант подписки': 3,
                  'Дата заключения': '2020-02-10', 'Дата окончания': '2021-08-15'},
                 {'Номер': 10, 'Идентификатор клиента': 10, 'Название подписки': 'Deezer',
                  'Вариант подписки': 2, 'Дата заключения': '2020-02-19', 'Дата окончания': '2021-09-24'},
                 {'Номер': 11, 'Идентификатор клиента': 2, 'Название подписки': 'IVI', 'Вариант подписки': 3,
                  'Дата заключения': '2020-03-18', 'Дата окончания': '2021-02-17'},
                 {'Номер': 12, 'Идентификатор клиента': 5, 'Название подписки': 'Science',
                  'Вариант подписки': 1, 'Дата заключения': '2020-04-13', 'Дата окончания': '2020-10-15'},
                 {'Номер': 13, 'Идентификатор клиента': 7, 'Название подписки': 'Netflix',
                  'Вариант подписки': 2, 'Дата заключения': '2020-05-21', 'Дата окончания': '2021-08-13'},
                 {'Номер': 14, 'Идентификатор клиента': 6, 'Название подписки': 'Прикладная информатика',
                  'Вариант подписки': 1, 'Дата заключения': '2020-06-19', 'Дата окончания': '2021-11-11'},
                 {'Номер': 15, 'Идентификатор клиента': 9, 'Название подписки': 'YouTube',
                  'Вариант подписки': 1, 'Дата заключения': '2020-06-25', 'Дата окончания': '2021-06-25'},
                 {'Номер': 16, 'Идентификатор клиента': 10, 'Название подписки': 'Science',
                  'Вариант подписки': 3, 'Дата заключения': '2020-08-30', 'Дата окончания': '2021-05-27'},
                 {'Номер': 17, 'Идентификатор клиента': 1, 'Название подписки': 'GQ', 'Вариант подписки': 1,
                  'Дата заключения': '2020-10-19', 'Дата окончания': '2021-07-04'},
                 {'Номер': 18, 'Идентификатор клиента': 4, 'Название подписки': 'SoundCloud',
                  'Вариант подписки': 2, 'Дата заключения': '2020-11-09', 'Дата окончания': '2021-12-01'},
                 {'Номер': 19, 'Идентификатор клиента': 5, 'Название подписки': 'Spotify',
                  'Вариант подписки': 3, 'Дата заключения': '2020-12-12', 'Дата окончания': '2021-10-14'},
                 {'Номер': 20, 'Идентификатор клиента': 3, 'Название подписки': 'IVI', 'Вариант подписки': 1,
                  'Дата заключения': '2021-05-03', 'Дата окончания': '2021-09-23'}])

            sums_insert = sums_table.insert()
            # print(sums_insert)
            sums_insert.compile()
            sums_insert.execute([{'Номер договора': 1, 'Оплаченная сумма': 0},
                                 {'Номер договора': 2, 'Оплаченная сумма': 0},
                                 {'Номер договора': 3, 'Оплаченная сумма': 0},
                                 {'Номер договора': 4, 'Оплаченная сумма': 0},
                                 {'Номер договора': 5, 'Оплаченная сумма': 0},
                                 {'Номер договора': 6, 'Оплаченная сумма': 0},
                                 {'Номер договора': 7, 'Оплаченная сумма': 0},
                                 {'Номер договора': 8, 'Оплаченная сумма': 0},
                                 {'Номер договора': 9, 'Оплаченная сумма': 0},
                                 {'Номер договора': 10, 'Оплаченная сумма': 0},
                                 {'Номер договора': 11, 'Оплаченная сумма': 0},
                                 {'Номер договора': 12, 'Оплаченная сумма': 0},
                                 {'Номер договора': 13, 'Оплаченная сумма': 0},
                                 {'Номер договора': 14, 'Оплаченная сумма': 0},
                                 {'Номер договора': 15, 'Оплаченная сумма': 0},
                                 {'Номер договора': 16, 'Оплаченная сумма': 0},
                                 {'Номер договора': 17, 'Оплаченная сумма': 0},
                                 {'Номер договора': 18, 'Оплаченная сумма': 0},
                                 {'Номер договора': 19, 'Оплаченная сумма': 0},
                                 {'Номер договора': 20, 'Оплаченная сумма': 0}])
            mb.showinfo("Table creation", message="Created new tables")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


def drop_db(btn):  # удаление базы данных
    def changer():
        global metadata, engine, url
        if url is not None:
            drop_database(url)
            metadata = MetaData()
            engine = None
            url = None
            mb.showinfo("Database drop", message="Database deleted")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


def drop_all_tables(btn):
    def changer():
        global metadata, url
        if url is not None:
            metadata.drop_all()
            metadata.clear()
            mb.showinfo("Tables drop", message="All tables deleted")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


# entry example "Итоговая сумма" "Контакты"
def clear_tables(btn, val, entry=""):  # для множественной очистки названия указывать в кавычках и через пробел
    def changer():
        global metadata, url
        if url is not None:
            if val.get() == 1:  # очистка всех таблиц
                for table in metadata.tables.keys():
                    metadata.tables[table].delete().execute()
                mb.showinfo("Tables clear", message="All tables cleared")
            else:
                tables = re.findall(r'"(.*?)"', entry.get())
                for table in tables:
                    metadata.tables[table].delete().execute()
                mb.showinfo("Tables clear", message="Cleared next tables: {}".format(tables))
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


def show_tables_names(btn, text_box):
    def changer():
        global metadata, url
        if url is not None:
            for name in metadata.tables:
                text_box.insert("end-1c", name + "\n")
            mb.showinfo("Tables names", message="Tables names displayed")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


def show_tables_content(btn, text_box):
    def changer():
        global metadata, url
        if url is not None:
            for table in metadata.tables.keys():
                text_box.insert("end-1c", "-----{}-----\n".format(table))
                for col in metadata.tables[table].columns.keys():
                    text_box.insert("end-1c", "{}    ".format(col))
                text_box.insert("end-1c", "\n")
                for row in metadata.tables[table].select().execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            mb.showinfo("Tables content", message="Tables content displayed")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


def show_table_content(btn, text_box):
    def changer():
        global metadata, url
        if url is not None:
            table = lst.get(lst.curselection())
            if table in ["Клиентская база", "Почты клиентов", "Поставщики", "Подписки", "Контакты", "Договоры",
                         "Варианты подписки", "Итоговая сумма"]:
                text_box.insert("end-1c", "-----{}-----\n".format(table))
                for col in metadata.tables[table].columns.keys():
                    text_box.insert("end-1c", "{}    ".format(col))
                text_box.insert("end-1c", "\n")
                for row in metadata.tables[table].select().execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            mb.showinfo("Tables content", message="Content of {} displayed".format(table))
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


# entry example Журнал
def find_by_description(btn, text_box, val):
    def changer():
        global metadata, url
        if url is not None:
            for row in metadata.tables["Подписки"].select().where(metadata.tables["Подписки"].columns["Описание"] == val.get()).execute():
                text_box.insert("end-1c", "{}\n".format(row))
            mb.showinfo("Find by description", message="Find completed")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


# entry example Журнал
def delete_by_description(btn, text_box, val):
    def changer():
        global metadata, url
        if url is not None:
            d = metadata.tables["Подписки"].delete().where(metadata.tables["Подписки"].columns["Описание"] == val.get())
            d.execute()
            mb.showinfo("Delete by description", message="Delete completed")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


# enter example for table Клиентская база 2: "15" "Пётр" "Петров" "Петрович" "16" "Иван" "Иванович" "Иваненко"
# enter example for table Договоры 1: "121" "1" "OKKO" "1" "2021-09-24" "2021-09-25"
def insert_data(btn, entry):
    def changer():
        global metadata, url
        if url is not None:
            rows, data = entry.get().split(':')
            rows = int(rows)
            table_name = lst.get(lst.curselection())
            data = re.findall(r'"(.*?)"', data)
            while rows > 0:
                if table_name == "Клиентская база":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Идентификатор': data.pop(0), 'Фамилия': data.pop(0), 'Имя': data.pop(0), 'Отчество': data.pop(0)})
                elif table_name == "Почты клиентов":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Идентификатор': data.pop(0), 'Почта': data.pop(0)})
                elif table_name == "Поставщики":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Наименование': data.pop(0), 'Оценка': data.pop(0)})
                elif table_name == "Подписки":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Название': data.pop(0), 'Описание': data.pop(0), 'Стоимость за день': data.pop(0), 'Поставщик': data.pop(0)})
                elif table_name == "Контакты":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Название': data.pop(0), 'Почта': data.pop(0)})
                elif table_name == "Договоры":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Номер': data.pop(0), 'Идентификатор клиента': data.pop(0), 'Название подписки': data.pop(0), 'Вариант подписки': data.pop(0), 'Дата заключения': data.pop(0), 'Дата окончания': data.pop(0)})
                elif table_name == "Варианты подписки":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Вариант': data.pop(0), 'Наценка, %': data.pop(0)})
                elif table_name == "Итоговая сумма":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Номер договора': data.pop(0), 'Оплаченная сумма': data.pop(0)})
                rows -= 1
            mb.showinfo("Data insert", message="Insert in {} completed".format(table_name))
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


def update_data(btn, entry):  # enter example for table Договоры 1: "1" "IVI" "1" "1999-5-5" "1999-6-6"
    def changer():
        global metadata, url
        if url is not None:
            ident, data = entry.get().split(':')
            table_name = lst.get(lst.curselection())
            data = re.findall(r'"(.*?)"', data)
            if table_name == "Клиентская база":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Идентификатор"] == ident).values({"Фамилия": data.pop(0), "Имя": data.pop(0), "Отчество": data.pop(0)})
                table_update.execute()
            elif table_name == "Почты клиентов":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Идентификатор"] == ident).values({"Почта": data.pop(0)})
                table_update.execute()
            elif table_name == "Поставщики":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Наименование"] == ident).values({"Оценка": data.pop(0)})
                table_update.execute()
            elif table_name == "Подписки":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Название"] == ident).values({"Описание": data.pop(0), "Стоимость за день": data.pop(0), "Поставщик": data.pop(0)})
                table_update.execute()
            elif table_name == "Контакты":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Название"] == ident).values({"Почта": data.pop(0)})
                table_update.execute()
            elif table_name == "Договоры":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Номер"] == ident).values({'Идентификатор клиента': data.pop(0), 'Название подписки': data.pop(0), 'Вариант подписки': data.pop(0), 'Дата заключения': data.pop(0), 'Дата окончания': data.pop(0)})
                table_update.execute()
            elif table_name == "Варианты подписки":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Вариант"] == ident).values({"Наценка, %": data.pop(0)})
                table_update.execute()
            elif table_name == "Итоговая сумма":
                table_update = metadata.tables[table_name].update().where(metadata.tables[table_name].c["Номер договора"] == ident).values({"Оплаченная сумма": data.pop(0)})
                table_update.execute()
            mb.showinfo("Data update", message="Update for {} completed".format(table_name))
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


# enter example for table Поставщики Оценка: "3"
def delete_data(btn, entry):
    def changer():
        global metadata, url
        if url is not None:
            ident, val = entry.get().split(':')
            table_name = lst.get(lst.curselection())
            val = re.findall(r'"(.*?)"', val)
            table_delete = metadata.tables[table_name].delete().where(metadata.tables[table_name].c[ident] == val[0])
            table_delete.execute()
            mb.showinfo("Data delete", message="Delete from {} completed".format(table_name))
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


# select enter example for table Подписки Стоимость за день: "=" "300"
def select_data(btn, text_box, entry):
    def changer():
        global metadata, url
        if url is not None:
            ident, val = entry.get().split(':')
            table_name = lst.get(lst.curselection())
            val = re.findall(r'"(.*?)"', val)
            sign = val.pop(0)
            if sign == "=":
                for row in metadata.tables[table_name].select().where(metadata.tables[table_name].columns[ident] == val.pop(0)).execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            elif sign == ">":
                for row in metadata.tables[table_name].select().where(metadata.tables[table_name].columns[ident] > val.pop(0)).execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            elif sign == "<":
                for row in metadata.tables[table_name].select().where(metadata.tables[table_name].columns[ident] < val.pop(0)).execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            mb.showinfo("Find by param", message="Find completed")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")
    return changer


l1 = Label(text="1)To create/connect to database enter the name of database, then click on button \"Create DB\"\n"
                "2)To fill the database with init data press button \"Fill DB\"\n"
                "3)To drop database press \"Drop DB\"\n"
                "4)To drop all tables from database click \"Drop all tables\"\n"
                "5)To show the names of the tables that exist in the database press \"Show tables names\"\n"
                "6)To show content of tables in database press button \"Show tables content\"\n"
                "7)To clear tables enter sequence like \"Варианты подписки\" \"Подписки\" and press \"Clear tables\", "
                "to clear all tables mark \"Clear all tables\"\n"
                "8)To use custom find by index (records in Подписки with mentioned Описание) enter description value and press \"Find subscription by description\" button\n"
                "9)To delete by prepared field enter enter description for table \"Подписки\" and press \"Delete subscription by description\" button\n"
                "10)To insert new data enter string \'number of rows: \"data1\" \"data2\" ...\'\n"
                "exmaple for table \"Клиентская база\" 2: \"15\" \"Петров\" \"Пётр\" \"Петрович\" \"16\" \"Иваненко\" \"Иван\" \"Иванович\" and select table from list\n"
                "11)To update data from existing table, set string of \'pkey_value: \"new value1\" \"new value2\" \'\n"
                "example for table \"Договоры\" 1: \"1\" \"IVI\" \"1\" \"1999-5-5\" \"1999-6-6\"\n"
                "12)To delete data from table, enter \'field: \"value1\" \'\n"
                "example for table \"Поставщики\" Оценка: \"3\"\n"
                "13)To show content of one table, select table from list and click \"Show content of one table\"\n"
                "14)To find by entry, enter sting like \'coll: \"sign\" \"value\" \', select table from list and then press button \"Find by entry\"", font="Arial 11")
l1.config(bg="#fffaaa")
l1.place(x=550, y=0)

#  поле для имени создаваемой/удаляемой базы данных
e1 = Entry(width=50)
e1.insert(0, "phys_dev")
e1.place(x=0, y=0)

# вывод нового окна
tb1 = Text(root, width=100, height=25)
tb1.place(x=0, y=300)

lst = Listbox()
for item in ["Клиентская база", "Почты клиентов", "Поставщики", "Подписки", "Контакты", "Договоры", "Варианты подписки", "Итоговая сумма"]:
    lst.insert(END, item)
lst.place(x=0, y=135)

# добавление scrollbar для listbox
#scroll = Scrollbar(command=tb1.yview)
#scroll.place(x=805, y=300)

# очистка таблиц
value = IntVar()
ch = Checkbutton(text="Clear all tables", variable=value, onvalue=1, offvalue=0)
ch.place(x=420, y=50)

# кнопка для создания базы данных
b1 = Button(text='Create DB', width=10, height=1)
b1.config(command=create_db(b1, e1))
b1.place(x=0, y=20)

# кнопка для заполнения базы данных
b2 = Button(text='Fill DB', width=10, height=1)
b2.config(command=insert_init_data(b2))
b2.place(x=100, y=20)

# кнопка для удаления базы данных
b3 = Button(text='Drop DB', width=10, height=1)
b3.config(command=drop_db(b3))
b3.place(x=200, y=20)

# кнопка для удаления базы данных
b4 = Button(text='Drop all tables', width=10, height=1)
b4.config(command=drop_all_tables(b4))
b4.place(x=300, y=20)

# вывод названий таблиц
b5 = Button(text='Show tables names', width=15, height=1)
b5.config(command=show_tables_names(b5, tb1))
b5.place(x=0, y=50)

# вывод содержимого таблиц
b6 = Button(text='Show tables content', width=15, height=1)
b6.config(command=show_tables_content(b6, tb1))
b6.place(x=140, y=50)

# очистка таблиц
b7 = Button(text='Clear tables', width=15, height=1)
b7.config(command=clear_tables(b7, value, e1))
b7.place(x=280, y=50)

# поиск по текстовому полю
b8 = Button(text='Find subscription by description', width=25, height=1)
b8.config(command=find_by_description(b8, tb1, e1))
b8.place(x=0, y=80)

# удаление по текстовому полю
b9 = Button(text='Delete subscription by description', width=25, height=1)
b9.config(command=delete_by_description(b9, tb1, e1))
b9.place(x=210, y=80)

# добавление новых данных
b10 = Button(text='Insert new data', width=15, height=1)
b10.config(command=insert_data(b10, e1))
b10.place(x=0, y=110)

# обновление кортежа
b11 = Button(text='Update data', width=15, height=1)
b11.config(command=update_data(b11, e1))
b11.place(x=140, y=110)

# удаление конкретной записи
b12 = Button(text='Delete data', width=15, height=1)
b12.config(command=delete_data(b12, e1))
b12.place(x=280, y=110)

# вывод одной таблицы
b13 = Button(text='Show content of one table', width=20, height=1)
b13.config(command=show_table_content(b13, tb1))
b13.place(x=150, y=275)

# поиск по таблице
b14 = Button(text='Find by entry', width=20, height=1)
b14.config(command=select_data(b14, tb1, e1))
b14.place(x=340, y=275)

root.mainloop()
