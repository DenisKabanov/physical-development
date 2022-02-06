from tkinter import *
from tkinter import messagebox as mb
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, Date, create_engine, CheckConstraint, \
    Index, DDL, event, Numeric
from sqlalchemy_utils import database_exists, create_database, drop_database
import re
import psycopg2

root = Tk()
root.title("Physical development")
root.geometry("1555x720")  # размер окна

metadata = MetaData()
engine = None
url = None


# 238 insert_data
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
        print(url)

    return changer


def insert_init_data(btn):
    def changer():
        global metadata, url
        if url is not None:
            metadata.drop_all()
            metadata.clear()
            patients = Table('Пациенты', metadata,
                             Column('Идентификатор', Integer, autoincrement=True, primary_key=True),
                             Column('Фамилия', String),
                             Column('Имя', String),
                             Column('Отчество', String),
                             Column('Пол', String, CheckConstraint('Пол=="М" OR Пол=="Ж"')),
                             Column('Дата рождения', Date, nullable=False),
                             Column('Дата осмотра', Date),
                             Column('Длина тела', Numeric(6, 2)),
                             Column('Масса тела', Numeric(6, 2)),
                             Column('Индекс Кетле', Numeric(6, 2)),
                             Column('Окружность грудной клетки', Numeric(6, 2)),
                             Column('Окружность талии', Numeric(6, 2)),
                             Column('Окружность правого плеча', Numeric(6, 2)),
                             Column('Окружность левого плеча', Numeric(6, 2)),
                             Column('Окружность бёдер', Numeric(6, 2)),
                             Column('Окружность шеи', Numeric(6, 2)),
                             Column('Окружность запястья', Numeric(6, 2)),
                             Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                             Column('Динамометрия правой кисти', Numeric(6, 2)),
                             Column('Динамометрия левой кисти', Numeric(6, 2)),
                             Column('Сист. артериальное давление', Numeric(6, 2)),
                             Column('Диаст. артериальное давление', Numeric(6, 2)),
                             Column('Частота сердечных сокращений', Numeric(6, 2)),
                             Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                             Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                             Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                             extend_existing=True)

            boy_3 = Table('Мальчики 3 года', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          extend_existing=True)


            boy_35 = Table('Мальчики, 3,5 года', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           extend_existing=True)

            boy_4 = Table('Мальчики, 4 года', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                          Column('Динамометрия правой кисти', Numeric(6, 2)),
                          Column('Динамометрия левой кисти', Numeric(6, 2)),
                          Column('Сист. артериальное давление', Numeric(6, 2)),
                          Column('Диаст. артериальное давление', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          extend_existing=True)

            boy_45 = Table('Мальчики, 4,5 года', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           extend_existing=True)

            boy_5 = Table('Мальчики, 5 года', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                          Column('Динамометрия правой кисти', Numeric(6, 2)),
                          Column('Динамометрия левой кисти', Numeric(6, 2)),
                          Column('Сист. артериальное давление', Numeric(6, 2)),
                          Column('Диаст. артериальное давление', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          extend_existing=True)

            boy_55 = Table('Мальчики, 5,5 года', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           extend_existing=True)

            boy_6 = Table('Мальчики, 6 лет', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                          Column('Динамометрия правой кисти', Numeric(6, 2)),
                          Column('Динамометрия левой кисти', Numeric(6, 2)),
                          Column('Сист. артериальное давление', Numeric(6, 2)),
                          Column('Диаст. артериальное давление', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          extend_existing=True)

            boy_65 = Table('Мальчики, 6,5 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           extend_existing=True)

            boy_7 = Table('Мальчики, 7 лет', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Индекс Кетле', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Окружность талии', Numeric(6, 2)),
                          Column('Окружность правого плеча', Numeric(6, 2)),
                          Column('Окружность левого плеча', Numeric(6, 2)),
                          Column('Окружность бёдер', Numeric(6, 2)),
                          Column('Окружность шеи', Numeric(6, 2)),
                          Column('Окружность запястья', Numeric(6, 2)),
                          Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                          Column('Динамометрия правой кисти', Numeric(6, 2)),
                          Column('Динамометрия левой кисти', Numeric(6, 2)),
                          Column('Сист. артериальное давление', Numeric(6, 2)),
                          Column('Диаст. артериальное давление', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                          Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                          Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                          extend_existing=True)

            boy_8 = Table('Мальчики, 8 лет', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Индекс Кетле', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Окружность талии', Numeric(6, 2)),
                          Column('Окружность правого плеча', Numeric(6, 2)),
                          Column('Окружность левого плеча', Numeric(6, 2)),
                          Column('Окружность бёдер', Numeric(6, 2)),
                          Column('Окружность шеи', Numeric(6, 2)),
                          Column('Окружность запястья', Numeric(6, 2)),
                          Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                          Column('Динамометрия правой кисти', Numeric(6, 2)),
                          Column('Динамометрия левой кисти', Numeric(6, 2)),
                          Column('Сист. артериальное давление', Numeric(6, 2)),
                          Column('Диаст. артериальное давление', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                          Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                          Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                          extend_existing=True)

            boy_9 = Table('Мальчики, 9 лет', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Индекс Кетле', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Окружность талии', Numeric(6, 2)),
                          Column('Окружность правого плеча', Numeric(6, 2)),
                          Column('Окружность левого плеча', Numeric(6, 2)),
                          Column('Окружность бёдер', Numeric(6, 2)),
                          Column('Окружность шеи', Numeric(6, 2)),
                          Column('Окружность запястья', Numeric(6, 2)),
                          Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                          Column('Динамометрия правой кисти', Numeric(6, 2)),
                          Column('Динамометрия левой кисти', Numeric(6, 2)),
                          Column('Сист. артериальное давление', Numeric(6, 2)),
                          Column('Диаст. артериальное давление', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                          Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                          Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                          extend_existing=True)

            boy_10 = Table('Мальчики, 10 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_11 = Table('Мальчики, 11 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_12 = Table('Мальчики, 12 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_13 = Table('Мальчики, 13 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_14 = Table('Мальчики, 14 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_15 = Table('Мальчики, 15 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_16 = Table('Мальчики, 16 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            boy_17 = Table('Мальчики, 17 лет', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Индекс Кетле', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Окружность талии', Numeric(6, 2)),
                           Column('Окружность правого плеча', Numeric(6, 2)),
                           Column('Окружность левого плеча', Numeric(6, 2)),
                           Column('Окружность бёдер', Numeric(6, 2)),
                           Column('Окружность шеи', Numeric(6, 2)),
                           Column('Окружность запястья', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
                           Column('Динамометрия правой кисти', Numeric(6, 2)),
                           Column('Динамометрия левой кисти', Numeric(6, 2)),
                           Column('Сист. артериальное давление', Numeric(6, 2)),
                           Column('Диаст. артериальное давление', Numeric(6, 2)),
                           Column('Частота сердечных сокращений', Numeric(6, 2)),
                           Column('Толщина жировой складки (живот)', Numeric(6, 2)),
                           Column('Толщина жировой складки (плечо)', Numeric(6, 2)),
                           Column('Толщина жировой складки (спина)', Numeric(6, 2)),
                           extend_existing=True)

            metadata.create_all()

            boy_3_insert = boy_3.insert()
            boy_3_insert.compile()
            boy_3_insert.execute(
                [{'Длина тела': 88.0, 'Масса тела': 12.0, 'Окружность грудной клетки': 48.0, 'Частота сердечных сокращений': 100},
                 {'Длина тела': 90.0, 'Масса тела': 12.85, 'Окружность грудной клетки': 49.0, 'Частота сердечных сокращений': 100},
                 {'Длина тела': 93.0, 'Масса тела': 13.6, 'Окружность грудной клетки': 50.0, 'Частота сердечных сокращений': 112},
                 {'Длина тела': 96.0, 'Масса тела': 14.95, 'Окружность грудной клетки': 53.0, 'Частота сердечных сокращений': 118},
                 {'Длина тела': 99.0, 'Масса тела': 16.0, 'Окружность грудной клетки': 54.0, 'Частота сердечных сокращений': 120},
                 {'Длина тела': 101.0, 'Масса тела': 16.9, 'Окружность грудной клетки': 56.0, 'Частота сердечных сокращений': 124},
                 {'Длина тела': 104.0, 'Масса тела': 18.0, 'Окружность грудной клетки': 57.0, 'Частота сердечных сокращений': 124}])

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
                    table_insert.execute({'Идентификатор': data.pop(0), 'Фамилия': data.pop(0), 'Имя': data.pop(0),
                                          'Отчество': data.pop(0)})
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
                    table_insert.execute(
                        {'Название': data.pop(0), 'Описание': data.pop(0), 'Стоимость за день': data.pop(0),
                         'Поставщик': data.pop(0)})
                elif table_name == "Контакты":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute({'Название': data.pop(0), 'Почта': data.pop(0)})
                elif table_name == "Договоры":
                    table_insert = metadata.tables[table_name].insert()
                    table_insert.compile()
                    table_insert.execute(
                        {'Номер': data.pop(0), 'Идентификатор клиента': data.pop(0), 'Название подписки': data.pop(0),
                         'Вариант подписки': data.pop(0), 'Дата заключения': data.pop(0),
                         'Дата окончания': data.pop(0)})
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
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Идентификатор"] == ident).values(
                    {"Фамилия": data.pop(0), "Имя": data.pop(0), "Отчество": data.pop(0)})
                table_update.execute()
            elif table_name == "Почты клиентов":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Идентификатор"] == ident).values({"Почта": data.pop(0)})
                table_update.execute()
            elif table_name == "Поставщики":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Наименование"] == ident).values({"Оценка": data.pop(0)})
                table_update.execute()
            elif table_name == "Подписки":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Название"] == ident).values(
                    {"Описание": data.pop(0), "Стоимость за день": data.pop(0), "Поставщик": data.pop(0)})
                table_update.execute()
            elif table_name == "Контакты":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Название"] == ident).values({"Почта": data.pop(0)})
                table_update.execute()
            elif table_name == "Договоры":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Номер"] == ident).values(
                    {'Идентификатор клиента': data.pop(0), 'Название подписки': data.pop(0),
                     'Вариант подписки': data.pop(0), 'Дата заключения': data.pop(0), 'Дата окончания': data.pop(0)})
                table_update.execute()
            elif table_name == "Варианты подписки":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Вариант"] == ident).values({"Наценка, %": data.pop(0)})
                table_update.execute()
            elif table_name == "Итоговая сумма":
                table_update = metadata.tables[table_name].update().where(
                    metadata.tables[table_name].c["Номер договора"] == ident).values({"Оплаченная сумма": data.pop(0)})
                table_update.execute()
            mb.showinfo("Data update", message="Update for {} completed".format(table_name))
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
                for row in metadata.tables[table_name].select().where(
                        metadata.tables[table_name].columns[ident] == val.pop(0)).execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            elif sign == ">":
                for row in metadata.tables[table_name].select().where(
                        metadata.tables[table_name].columns[ident] > val.pop(0)).execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            elif sign == "<":
                for row in metadata.tables[table_name].select().where(
                        metadata.tables[table_name].columns[ident] < val.pop(0)).execute():
                    text_box.insert("end-1c", "{}\n".format(row))
            mb.showinfo("Find by param", message="Find completed")
        else:
            mb.showwarning("WARNING", message="Firstly, connect to DB")

    return changer


#  поле для имени создаваемой/удаляемой базы данных
e1 = Entry(width=50)
e1.insert(0, "phys_dev")
e1.place(x=0, y=0)

# вывод нового окна
tb1 = Text(root, width=100, height=25)
tb1.place(x=0, y=300)

lst = Listbox()
for item in ["Клиентская база", "Почты клиентов", "Поставщики", "Подписки", "Контакты", "Договоры", "Варианты подписки",
             "Итоговая сумма"]:
    lst.insert(END, item)
lst.place(x=0, y=135)

# добавление scrollbar для listbox
# scroll = Scrollbar(command=tb1.yview)
# scroll.place(x=805, y=300)

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

# вывод содержимого таблиц
b6 = Button(text='Show tables content', width=15, height=1)
b6.config(command=show_tables_content(b6, tb1))
b6.place(x=140, y=50)

# очистка таблиц
b7 = Button(text='Clear tables', width=15, height=1)
b7.config(command=clear_tables(b7, value, e1))
b7.place(x=280, y=50)

# добавление новых данных
b10 = Button(text='Insert new data', width=15, height=1)
b10.config(command=insert_data(b10, e1))
b10.place(x=0, y=110)

# обновление кортежа
b11 = Button(text='Update data', width=15, height=1)
b11.config(command=update_data(b11, e1))
b11.place(x=140, y=110)

# вывод одной таблицы
b13 = Button(text='Show content of one table', width=20, height=1)
b13.config(command=show_table_content(b13, tb1))
b13.place(x=150, y=275)

# поиск по таблице
b14 = Button(text='Find by entry', width=20, height=1)
b14.config(command=select_data(b14, tb1, e1))
b14.place(x=340, y=275)

root.mainloop()
