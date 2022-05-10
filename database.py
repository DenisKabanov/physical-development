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
# url = None
url = "postgresql+psycopg2://postgres:postgres@localhost:5432/physical_development"
if not database_exists(url):
    create_database(url)
engine = create_engine(url, echo=False)
metadata.bind = engine
metadata.reflect()



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

            boy_3 = Table('Мальчики, 3 года', metadata,
                          Column('Длина тела', Numeric(6, 2)),
                          Column('Масса тела', Numeric(6, 2)),
                          Column('Окружность грудной клетки', Numeric(6, 2)),
                          Column('Частота сердечных сокращений', Numeric(6, 2)),
                          extend_existing=True)

            girl_3 = Table('Девочки, 3 года', metadata,
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

            girl_35 = Table('Девочки, 3,5 года', metadata,
                           Column('Длина тела', Numeric(6, 2)),
                           Column('Масса тела', Numeric(6, 2)),
                           Column('Окружность грудной клетки', Numeric(6, 2)),
                           Column('Жизненная ёмкость лёгких', Numeric(6, 2)),
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

            girl_4 = Table('Девочки, 4 года', metadata,
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

            girl_45 = Table('Девочки, 4,5 года', metadata,
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

            girl_5 = Table('Девочки, 5 года', metadata,
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

            girl_55 = Table('Девочки, 5,5 года', metadata,
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

            girl_6 = Table('Девочки, 6 лет', metadata,
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

            girl_65 = Table('Девочки, 6,5 лет', metadata,
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

            girl_7 = Table('Девочки, 7 лет', metadata,
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

            girl_8 = Table('Девочки, 8 лет', metadata,
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

            girl_9 = Table('Девочки, 9 лет', metadata,
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

            girl_10 = Table('Девочки, 10 лет', metadata,
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

            girl_11 = Table('Девочки, 11 лет', metadata,
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

            girl_12 = Table('Девочки, 12 лет', metadata,
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

            girl_13 = Table('Девочки, 13 лет', metadata,
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

            girl_14 = Table('Девочки, 14 лет', metadata,
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

            girl_15 = Table('Девочки, 15 лет', metadata,
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

            girl_16 = Table('Девочки, 16 лет', metadata,
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

            girl_17 = Table('Девочки, 17 лет', metadata,
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

            boy_35_insert = boy_35.insert()
            boy_35_insert.compile()
            boy_35_insert.execute(
                [{'Длина тела': 91.0, 'Масса тела': 12.7, 'Окружность грудной клетки': 47.0, 'Жизненная ёмкость лёгких': 0.3, 'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 90},
                 {'Длина тела': 94.0, 'Масса тела': 13.6, 'Окружность грудной клетки': 51.0, 'Жизненная ёмкость лёгких': 0.3, 'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 90},
                 {'Длина тела': 96.5, 'Масса тела': 14.7, 'Окружность грудной клетки': 51.0, 'Жизненная ёмкость лёгких': 0.9, 'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 92},
                 {'Длина тела': 100.0, 'Масса тела': 16.0, 'Окружность грудной клетки': 53.0, 'Жизненная ёмкость лёгких': 0.9, 'Сист. артериальное давление': 79, 'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 100},
                 {'Длина тела': 103.0, 'Масса тела': 17.3, 'Окружность грудной клетки': 55.0, 'Жизненная ёмкость лёгких': 1.3, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 114},
                 {'Длина тела': 105.0, 'Масса тела': 18.8, 'Окружность грудной клетки': 57.0, 'Жизненная ёмкость лёгких': 1.3, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 116},
                 {'Длина тела': 108.0, 'Масса тела': 20.0, 'Окружность грудной клетки': 58.0, 'Жизненная ёмкость лёгких': 1.0, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 120}])

            boy_4_insert = boy_4.insert()
            boy_4_insert.compile()
            boy_4_insert.execute(
                [{'Длина тела': 94.0, 'Масса тела': 13.5, 'Окружность грудной клетки': 50.0, 'Жизненная ёмкость лёгких': 0.5, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1, 'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 45, 'Частота сердечных сокращений': 72},
                 {'Длина тела': 97.5, 'Масса тела': 14.0, 'Окружность грудной клетки': 50.0, 'Жизненная ёмкость лёгких': 0.6, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1, 'Сист. артериальное давление': 75, 'Диаст. артериальное давление': 45, 'Частота сердечных сокращений': 80},
                 {'Длина тела': 100.0, 'Масса тела': 15.0, 'Окружность грудной клетки': 53.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 2, 'Сист. артериальное давление': 76, 'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 93},
                 {'Длина тела': 103.0, 'Масса тела': 16.5, 'Окружность грудной клетки': 54.5, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 2, 'Сист. артериальное давление': 79, 'Диаст. артериальное давление': 56, 'Частота сердечных сокращений': 99},
                 {'Длина тела': 106.0, 'Масса тела': 18.0, 'Окружность грудной клетки': 56.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 108},
                 {'Длина тела': 108.0, 'Масса тела': 19.5, 'Окружность грудной клетки': 57.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 86, 'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 108},
                 {'Длина тела': 111.0, 'Масса тела': 21.0, 'Окружность грудной клетки': 58.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 86, 'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 108}])

            boy_45_insert = boy_45.insert()
            boy_45_insert.compile()
            boy_45_insert.execute(
                [{'Длина тела': 98.0, 'Масса тела': 14.2, 'Окружность грудной клетки': 51.0, 'Жизненная ёмкость лёгких': 0.7, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 2, 'Сист. артериальное давление': 70, 'Диаст. артериальное давление': 45, 'Частота сердечных сокращений': 84},
                 {'Длина тела': 101.0, 'Масса тела': 15.2, 'Окружность грудной клетки': 52.0, 'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 2, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 51, 'Частота сердечных сокращений': 90},
                 {'Длина тела': 103.5, 'Масса тела': 16.3, 'Окружность грудной клетки': 54.0, 'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 85, 'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 96},
                 {'Длина тела': 107.0, 'Масса тела': 17.8, 'Окружность грудной клетки': 55.0, 'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 4, 'Сист. артериальное давление': 85, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 100},
                 {'Длина тела': 110.0, 'Масса тела': 19.5, 'Окружность грудной клетки': 57.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 5, 'Сист. артериальное давление': 92, 'Диаст. артериальное давление': 64, 'Частота сердечных сокращений': 108},
                 {'Длина тела': 113.0, 'Масса тела': 21.1, 'Окружность грудной клетки': 58.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 6, 'Сист. артериальное давление': 96, 'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 112},
                 {'Длина тела': 118.0, 'Масса тела': 25.2, 'Окружность грудной клетки': 60.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 7, 'Динамометрия левой кисти': 7, 'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 66, 'Частота сердечных сокращений': 116}])

            boy_5_insert = boy_5.insert()
            boy_5_insert.compile()
            boy_5_insert.execute(
                [{'Длина тела': 102.0, 'Масса тела': 15.0, 'Окружность грудной клетки': 52.0, 'Жизненная ёмкость лёгких': 0.6, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 75, 'Диаст. артериальное давление': 40, 'Частота сердечных сокращений': 72},
                 {'Длина тела': 104.0, 'Масса тела': 16.0, 'Окружность грудной клетки': 52.0, 'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 40, 'Частота сердечных сокращений': 78},
                 {'Длина тела': 107.0, 'Масса тела': 17.0, 'Окружность грудной клетки': 54.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 85, 'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 90},
                 {'Длина тела': 110.0, 'Масса тела': 18.5, 'Окружность грудной клетки': 56.0, 'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 4, 'Сист. артериальное давление': 94, 'Диаст. артериальное давление': 55.5, 'Частота сердечных сокращений': 96},
                 {'Длина тела': 113.0, 'Масса тела': 20.1, 'Окружность грудной клетки': 58.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 6, 'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 108},
                 {'Длина тела': 115.0, 'Масса тела': 21.5, 'Окружность грудной клетки': 59.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 7, 'Сист. артериальное давление': 105, 'Диаст. артериальное давление': 68, 'Частота сердечных сокращений': 110},
                 {'Длина тела': 118.0, 'Масса тела': 24.0, 'Окружность грудной клетки': 64.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 8, 'Динамометрия левой кисти': 7, 'Сист. артериальное давление': 115, 'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 112}])

            boy_55_insert = boy_55.insert()
            boy_55_insert.compile()
            boy_55_insert.execute(
                [{'Длина тела': 104.0, 'Масса тела': 15.5, 'Окружность грудной клетки': 52.0, 'Жизненная ёмкость лёгких': 0.5, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1, 'Сист. артериальное давление': 75, 'Диаст. артериальное давление': 40, 'Частота сердечных сокращений': 70},
                 {'Длина тела': 107.0, 'Масса тела': 16.8, 'Окружность грудной клетки': 54.0, 'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 1, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 45, 'Частота сердечных сокращений': 72},
                 {'Длина тела': 110.0, 'Масса тела': 18.2, 'Окружность грудной клетки': 55.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 90},
                 {'Длина тела': 114.0, 'Масса тела': 19.5, 'Окружность грудной клетки': 57.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 5, 'Сист. артериальное давление': 87.5, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 96},
                 {'Длина тела': 117.0, 'Масса тела': 21.2, 'Окружность грудной клетки': 59.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 7, 'Динамометрия левой кисти': 7, 'Сист. артериальное давление': 95, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 102},
                 {'Длина тела': 120.0, 'Масса тела': 23.1, 'Окружность грудной клетки': 61.0, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 11, 'Динамометрия левой кисти': 9, 'Сист. артериальное давление': 102, 'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 120},
                 {'Длина тела': 124.0, 'Масса тела': 26.5, 'Окружность грудной клетки': 61.0, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 14, 'Динамометрия левой кисти': 12, 'Сист. артериальное давление': 110, 'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 120}])

            boy_6_insert = boy_6.insert()
            boy_6_insert.compile()
            boy_6_insert.execute(
                [{'Длина тела': 108.0, 'Масса тела': 16.4, 'Окружность грудной клетки': 52.0, 'Жизненная ёмкость лёгких': 0.6, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 40, 'Частота сердечных сокращений': 70},
                 {'Длина тела': 110.0, 'Масса тела': 17.7, 'Окружность грудной клетки': 54.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 46, 'Частота сердечных сокращений': 72},
                 {'Длина тела': 113.0, 'Масса тела': 19.0, 'Окружность грудной клетки': 56.0, 'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 4, 'Сист. артериальное давление': 85, 'Диаст. артериальное давление': 54, 'Частота сердечных сокращений': 78},
                 {'Длина тела': 117.0, 'Масса тела': 20.8, 'Окружность грудной клетки': 57.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 4, 'Сист. артериальное давление': 90, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 90},
                 {'Длина тела': 121.0, 'Масса тела': 22.6, 'Окружность грудной клетки': 59.0, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 7, 'Динамометрия левой кисти': 7, 'Сист. артериальное давление': 95, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 96},
                 {'Длина тела': 124.0, 'Масса тела': 25.0, 'Окружность грудной клетки': 61.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 11, 'Динамометрия левой кисти': 11, 'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 102},
                 {'Длина тела': 127.0, 'Масса тела': 27.1, 'Окружность грудной клетки': 63.0, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 12, 'Динамометрия левой кисти': 12, 'Сист. артериальное давление': 105, 'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 108}])

            boy_65_insert = boy_65.insert()
            boy_65_insert.compile()
            boy_65_insert.execute(
                [{'Длина тела': 111.0, 'Масса тела': 17.2, 'Окружность грудной клетки': 52.0, 'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 1, 'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 38, 'Частота сердечных сокращений': 70},
                 {'Длина тела': 114.0, 'Масса тела': 18.6, 'Окружность грудной клетки': 55.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 4, 'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 42, 'Частота сердечных сокращений': 72},
                 {'Длина тела': 117.0, 'Масса тела': 20.2, 'Окружность грудной клетки': 57.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 6, 'Сист. артериальное давление': 88, 'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 84},
                 {'Длина тела': 120.0, 'Масса тела': 22.4, 'Окружность грудной клетки': 59.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9, 'Динамометрия левой кисти': 9, 'Сист. артериальное давление': 92, 'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 92},
                 {'Длина тела': 124.0, 'Масса тела': 24.3, 'Окружность грудной клетки': 61.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 11, 'Динамометрия левой кисти': 11, 'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 100},
                 {'Длина тела': 127.0, 'Масса тела': 27.0, 'Окружность грудной клетки': 63.0, 'Жизненная ёмкость лёгких': 1.6, 'Динамометрия правой кисти': 13, 'Динамометрия левой кисти': 13, 'Сист. артериальное давление': 110, 'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 108},
                 {'Длина тела': 131.0, 'Масса тела': 30.0, 'Окружность грудной клетки': 65.0, 'Жизненная ёмкость лёгких': 1.9, 'Динамометрия правой кисти': 14, 'Динамометрия левой кисти': 14, 'Сист. артериальное давление': 110, 'Диаст. артериальное давление': 75, 'Частота сердечных сокращений': 116}])

            boy_7_insert = boy_7.insert()
            boy_7_insert.compile()
            boy_7_insert.execute(
                [{'Длина тела': 115.3, 'Масса тела': 19.0, 'Индекс Кетле': 13.2, 'Окружность грудной клетки': 54.0, 'Окружность талии': 48.0, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча':15.5, 'Окружность бёдер':58.5, 'Окружность шеи':25.0, 'Окружность запястья':12.2, 'Жизненная ёмкость лёгких': 0.9,  'Динамометрия правой кисти': 5.0,
                  'Динамометрия левой кисти': 4.0, 'Сист. артериальное давление': 90, 'Диаст. артериальное давление': 47, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.4,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 118.3, 'Масса тела': 19.78, 'Индекс Кетле': 14.1, 'Окружность грудной клетки': 55.4, 'Окружность талии': 49.9, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча': 16.0, 'Окружность бёдер': 61.0, 'Окружность шеи': 26.0, 'Окружность запястья': 12.4, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 6.0,
                  'Динамометрия левой кисти': 5.0, 'Сист. артериальное давление': 93, 'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 75,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 121.96, 'Масса тела': 21.9, 'Индекс Кетле': 14.5, 'Окружность грудной клетки': 57.4, 'Окружность талии': 52.7, 'Окружность правого плеча': 17.5,
                  'Окружность левого плеча': 17.5, 'Окружность бёдер': 62.0, 'Окружность шеи': 26.5, 'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 7.0,
                  'Динамометрия левой кисти': 6.0, 'Сист. артериальное давление': 96, 'Диаст. артериальное давление': 54, 'Частота сердечных сокращений': 81,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 125.8, 'Масса тела': 24.59, 'Индекс Кетле': 15.59, 'Окружность грудной клетки': 59.6, 'Окружность талии': 55.6, 'Окружность правого плеча': 18.5,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 64.0, 'Окружность шеи': 27.0, 'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 8.0,
                  'Динамометрия левой кисти': 7.0, 'Сист. артериальное давление': 102, 'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 90,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 128.7, 'Масса тела': 27.5, 'Индекс Кетле': 16.9, 'Окружность грудной клетки': 61.9, 'Окружность талии': 59.5, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 68.0, 'Окружность шеи': 28.0, 'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.6, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 108, 'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 96,
                  'Толщина жировой складки (живот)': 1.2,
                  'Толщина жировой складки (плечо)': 1.1,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 132.2, 'Масса тела': 31.25, 'Индекс Кетле': 18.1, 'Окружность грудной клетки': 65.5, 'Окружность талии': 62.6, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 73.0, 'Окружность шеи': 29.0, 'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 11.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 116, 'Диаст. артериальное давление': 69, 'Частота сердечных сокращений': 102,
                  'Толщина жировой складки (живот)': 1.4,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 134.5, 'Масса тела': 33.9, 'Индекс Кетле': 19.4, 'Окружность грудной клетки': 68.9, 'Окружность талии': 68.0, 'Окружность правого плеча': 24.0,
                  'Окружность левого плеча': 24.0, 'Окружность бёдер': 80.0, 'Окружность шеи': 30.5, 'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 13.0,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 122, 'Диаст. артериальное давление': 72, 'Частота сердечных сокращений': 111,
                  'Толщина жировой складки (живот)': 2.0,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.2}])

            boy_8_insert = boy_8.insert()
            boy_8_insert.compile()
            boy_8_insert.execute(
                [{'Длина тела': 119.1, 'Масса тела': 21.73, 'Индекс Кетле': 13.5, 'Окружность грудной клетки': 56.1,
                  'Окружность талии': 51.3, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча': 16.0, 'Окружность бёдер': 59.0, 'Окружность шеи': 25.5,
                  'Окружность запястья': 11.5, 'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 6.0,
                  'Динамометрия левой кисти': 5.0, 'Сист. артериальное давление': 92,
                  'Диаст. артериальное давление': 47, 'Частота сердечных сокращений': 74,
                  'Толщина жировой складки (живот)': 0.4,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 121.2, 'Масса тела': 22.9, 'Индекс Кетле': 14.3, 'Окружность грудной клетки': 57.5,
                  'Окружность талии': 52.2, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.0, 'Окружность бёдер': 62.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 7.0,
                  'Динамометрия левой кисти': 6.0, 'Сист. артериальное давление': 94,
                  'Диаст. артериальное давление': 49, 'Частота сердечных сокращений': 76,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 125.8, 'Масса тела': 24.3, 'Индекс Кетле': 14.9, 'Окружность грудной клетки': 59.0,
                  'Окружность талии': 52.7, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 17.5, 'Окружность бёдер': 64.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 8.0, 'Сист. артериальное давление': 98,
                  'Диаст. артериальное давление': 54, 'Частота сердечных сокращений': 80,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 129.8, 'Масса тела': 26.8, 'Индекс Кетле': 15.8, 'Окружность грудной клетки': 61.5,
                  'Окружность талии': 55.9, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 67.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 88,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 134.2, 'Масса тела': 29.9, 'Индекс Кетле': 17.4, 'Окружность грудной клетки': 64.5,
                  'Окружность талии': 59.3, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 71.25, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 12.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 110,
                  'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 96,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 1.1,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 137.9, 'Масса тела': 35.40, 'Индекс Кетле': 18.6, 'Окружность грудной клетки': 69.1,
                  'Окружность талии': 65.8, 'Окружность правого плеча': 22.5,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 77.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.2, 'Динамометрия правой кисти': 13.0,
                  'Динамометрия левой кисти': 13.0, 'Сист. артериальное давление': 117,
                  'Диаст. артериальное давление': 69, 'Частота сердечных сокращений': 105,
                  'Толщина жировой складки (живот)': 1.9,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.1},
                 {'Длина тела': 148.0, 'Масса тела': 41.8, 'Индекс Кетле': 21.5, 'Окружность грудной клетки': 73.6,
                  'Окружность талии': 74.0, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 25.0, 'Окружность бёдер': 82.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 14.0,
                  'Динамометрия левой кисти': 14.0, 'Сист. артериальное давление': 120,
                  'Диаст. артериальное давление': 73, 'Частота сердечных сокращений': 109,
                  'Толщина жировой складки (живот)': 2.6,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 1.8}])

            boy_9_insert = boy_9.insert()
            boy_9_insert.compile()
            boy_9_insert.execute(
                [{'Длина тела': 124.9, 'Масса тела': 22.9, 'Индекс Кетле': 14.2, 'Окружность грудной клетки': 55.9,
                  'Окружность талии': 51.0, 'Окружность правого плеча': 16.5,
                  'Окружность левого плеча': 16.5, 'Окружность бёдер': 62.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 6.0,
                  'Динамометрия левой кисти': 5.0, 'Сист. артериальное давление': 89,
                  'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 73,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 129.4, 'Масса тела': 24.78, 'Индекс Кетле': 15.0, 'Окружность грудной клетки': 59.8,
                  'Окружность талии': 52.9, 'Окружность правого плеча': 17.5,
                  'Окружность левого плеча': 17.5, 'Окружность бёдер': 64.0, 'Окружность шеи': 26.5,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 7.0, 'Сист. артериальное давление': 92,
                  'Диаст. артериальное давление': 52, 'Частота сердечных сокращений': 77,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 131.9, 'Масса тела': 27.9, 'Индекс Кетле': 15.4, 'Окружность грудной клетки': 61.9,
                  'Окружность талии': 55.5, 'Окружность правого плеча': 18.5,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 67.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 99,
                  'Диаст. артериальное давление': 54, 'Частота сердечных сокращений': 83,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 136.7, 'Масса тела': 30.75, 'Индекс Кетле': 16.6, 'Окружность грудной клетки': 65.3,
                  'Окружность талии': 58.7, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 71.0, 'Окружность шеи': 28.2,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 12.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 106,
                  'Диаст. артериальное давление': 61, 'Частота сердечных сокращений': 91,
                  'Толщина жировой складки (живот)': 1.15,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 140.9, 'Масса тела': 37.1, 'Индекс Кетле': 19.2, 'Окружность грудной клетки': 79.0,
                  'Окружность талии': 64.5, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 77.00, 'Окружность шеи': 30.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.1, 'Динамометрия правой кисти': 14.0,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 112,
                  'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 98,
                  'Толщина жировой складки (живот)': 1.9,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 145.2, 'Масса тела': 42.32, 'Индекс Кетле': 20.2, 'Окружность грудной клетки': 74.8,
                  'Окружность талии': 72.6, 'Окружность правого плеча': 24.0,
                  'Окружность левого плеча': 24.5, 'Окружность бёдер': 82.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 2.5, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 119,
                  'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 106,
                  'Толщина жировой складки (живот)': 2.4,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.5},
                 {'Длина тела': 149.0, 'Масса тела': 51.2, 'Индекс Кетле': 23.6, 'Окружность грудной клетки': 86.0,
                  'Окружность талии': 88.0, 'Окружность правого плеча': 27.0,
                  'Окружность левого плеча': 27.0, 'Окружность бёдер': 89.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.6, 'Динамометрия правой кисти': 17.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 123,
                  'Диаст. артериальное давление': 74, 'Частота сердечных сокращений': 114,
                  'Толщина жировой складки (живот)': 3.2,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 2.1}])

            boy_10_insert = boy_10.insert()
            boy_10_insert.compile()
            boy_10_insert.execute(
                [{'Длина тела': 130.9, 'Масса тела': 25.4, 'Индекс Кетле': 14.1, 'Окружность грудной клетки': 57.7,
                  'Окружность талии': 50.7, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.0, 'Окружность бёдер': 63.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 8.0,
                  'Динамометрия левой кисти': 8.0, 'Сист. артериальное давление': 89,
                  'Диаст. артериальное давление': 48, 'Частота сердечных сокращений': 67,
                  'Толщина жировой складки (живот)': 0.4,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 132.9, 'Масса тела': 26.98, 'Индекс Кетле': 15.0, 'Окружность грудной клетки': 60.7,
                  'Окружность талии': 53.4, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 66.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 92,
                  'Диаст. артериальное давление': 51, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 136.8, 'Масса тела': 29.6, 'Индекс Кетле': 15.6, 'Окружность грудной клетки': 62.9,
                  'Окружность талии': 56.3, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 69.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 12.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 97,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 77,
                  'Толщина жировой складки (живот)': 0.75,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 140.2, 'Масса тела': 32.8, 'Индекс Кетле': 16.8, 'Окружность грудной клетки': 65.9,
                  'Окружность талии': 59.7, 'Окружность правого плеча': 20.25,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 72.75, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 13.0,
                  'Динамометрия левой кисти': 13.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 87,
                  'Толщина жировой складки (живот)': 1.1,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 144.6, 'Масса тела': 39.1, 'Индекс Кетле': 18.7, 'Окружность грудной клетки': 69.9,
                  'Окружность талии': 64.9, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 77.00, 'Окружность шеи': 30.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 14.0, 'Сист. артериальное давление': 113,
                  'Диаст. артериальное давление': 64, 'Частота сердечных сокращений': 95,
                  'Толщина жировой складки (живот)': 1.7,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.1},
                 {'Длина тела': 147.7, 'Масса тела': 50.1, 'Индекс Кетле': 20.9, 'Окружность грудной клетки': 78.6,
                  'Окружность талии': 73.2, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 87.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.6, 'Динамометрия правой кисти': 17.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 118,
                  'Диаст. артериальное давление': 69, 'Частота сердечных сокращений': 102,
                  'Толщина жировой складки (живот)': 2.7,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.4},
                 {'Длина тела': 150.7, 'Масса тела': 56.6, 'Индекс Кетле': 24.9, 'Окружность грудной клетки': 87.3,
                  'Окружность талии': 84.0, 'Окружность правого плеча': 28.5,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 93.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.0, 'Динамометрия правой кисти': 18.0,
                  'Динамометрия левой кисти': 17.0, 'Сист. артериальное давление': 121,
                  'Диаст. артериальное давление': 73, 'Частота сердечных сокращений': 107,
                  'Толщина жировой складки (живот)': 4.0,
                  'Толщина жировой складки (плечо)': 2.2,
                  'Толщина жировой складки (спина)': 2.7}])

            boy_11_insert = boy_11.insert()
            boy_11_insert.compile()
            boy_11_insert.execute(
                [{'Длина тела': 134.0, 'Масса тела': 27.3, 'Индекс Кетле': 14.1, 'Окружность грудной клетки': 60.9,
                  'Окружность талии': 52.0, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.5, 'Окружность бёдер': 65.0, 'Окружность шеи': 25.5,
                  'Окружность запястья': 11.5, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 93,
                  'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 67,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 136.8, 'Масса тела': 29.33, 'Индекс Кетле': 15.3, 'Окружность грудной клетки': 62.6,
                  'Окружность талии': 54.9, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 67.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.6, 'Динамометрия правой кисти': 11.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 96,
                  'Диаст. артериальное давление': 53, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 142.6, 'Масса тела': 33.3, 'Индекс Кетле': 16.3, 'Окружность грудной клетки': 64.4,
                  'Окружность талии': 57.6, 'Окружность правого плеча': 19.5,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 71.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 13.0,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 101,
                  'Диаст. артериальное давление': 58, 'Частота сердечных сокращений': 79.5,
                  'Толщина жировой складки (живот)': 0.85,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 147.0, 'Масса тела': 38.4, 'Индекс Кетле': 17.8, 'Окружность грудной клетки': 69.0,
                  'Окружность талии': 61.8, 'Окружность правого плеча': 21.5,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 75.0, 'Окружность шеи': 29.5,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 14.0, 'Сист. артериальное давление': 109,
                  'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 87,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 150.3, 'Масса тела': 45.5, 'Индекс Кетле': 20.3, 'Окружность грудной клетки': 74.8,
                  'Окружность талии': 70.2, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 24.5, 'Окружность бёдер': 83.00, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 2.6, 'Динамометрия правой кисти': 17.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 114,
                  'Диаст. артериальное давление': 67.5, 'Частота сердечных сокращений': 96,
                  'Толщина жировой складки (живот)': 2.5,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.5},
                 {'Длина тела': 155.1, 'Масса тела': 53.70, 'Индекс Кетле': 22.4, 'Окружность грудной клетки': 83.2,
                  'Окружность талии': 77.8, 'Окружность правого плеча': 27.0,
                  'Окружность левого плеча': 27.0, 'Окружность бёдер': 89.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.9, 'Динамометрия правой кисти': 21.0,
                  'Динамометрия левой кисти': 19.0, 'Сист. артериальное давление': 121,
                  'Диаст. артериальное давление': 72, 'Частота сердечных сокращений': 104,
                  'Толщина жировой складки (живот)': 3.0,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 1.9},
                 {'Длина тела': 160.2, 'Масса тела': 63.4, 'Индекс Кетле': 24.6, 'Окружность грудной клетки': 90.0,
                  'Окружность талии': 85.6, 'Окружность правого плеча': 28.0,
                  'Окружность левого плеча': 28.5, 'Окружность бёдер': 92.0, 'Окружность шеи': 34.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.1, 'Динамометрия правой кисти': 22.0,
                  'Динамометрия левой кисти': 22.0, 'Сист. артериальное давление': 123,
                  'Диаст. артериальное давление': 75, 'Частота сердечных сокращений': 108,
                  'Толщина жировой складки (живот)': 4.1,
                  'Толщина жировой складки (плечо)': 2.2,
                  'Толщина жировой складки (спина)': 2.8}])

            boy_12_insert = boy_12.insert()
            boy_12_insert.compile()
            boy_12_insert.execute(
                [{'Длина тела': 137.6, 'Масса тела': 29.2, 'Индекс Кетле': 15.0, 'Окружность грудной клетки': 62.0,
                  'Окружность талии': 54.3, 'Окружность правого плеча': 18.5,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 68.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.65, 'Динамометрия правой кисти': 12.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 95,
                  'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 73,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.45,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 142.4, 'Масса тела': 32.37, 'Индекс Кетле': 15.9, 'Окружность грудной клетки': 64.4,
                  'Окружность талии': 57.0, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 71.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 14.0,
                  'Динамометрия левой кисти': 13.0, 'Сист. артериальное давление': 98,
                  'Диаст. артериальное давление': 53, 'Частота сердечных сокращений': 74,
                  'Толщина жировой складки (живот)': 0.75,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 146.5, 'Масса тела': 36.5, 'Индекс Кетле': 16.5, 'Окружность грудной клетки': 67.7,
                  'Окружность талии': 59.6, 'Окружность правого плеча': 20.5,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 74.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.2, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 105,
                  'Диаст. артериальное давление': 58, 'Частота сердечных сокращений': 79.0,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 151.5, 'Масса тела': 41.3, 'Индекс Кетле': 17.9, 'Окружность грудной клетки': 71.8,
                  'Окружность талии': 64.3, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 22.0, 'Окружность бёдер': 78.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.5, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 18.0, 'Сист. артериальное давление': 110,
                  'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 88,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 156.3, 'Масса тела': 50.6, 'Индекс Кетле': 21.3, 'Окружность грудной клетки': 77.9,
                  'Окружность талии': 69.8, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 25.5, 'Окружность бёдер': 86.00, 'Окружность шеи': 32.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.9, 'Динамометрия правой кисти': 22.0,
                  'Динамометрия левой кисти': 21.0, 'Сист. артериальное давление': 117,
                  'Диаст. артериальное давление': 67.0, 'Частота сердечных сокращений': 98,
                  'Толщина жировой складки (живот)': 2.3,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.5},
                 {'Длина тела': 161.4, 'Масса тела': 63.90, 'Индекс Кетле': 22.7, 'Окружность грудной клетки': 87.9,
                  'Окружность талии': 81.9, 'Окружность правого плеча': 28.0,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 91.0, 'Окружность шеи': 34.5,
                  'Окружность запястья': 16.5, 'Жизненная ёмкость лёгких': 3.3, 'Динамометрия правой кисти': 25.0,
                  'Динамометрия левой кисти': 23.0, 'Сист. артериальное давление': 124,
                  'Диаст. артериальное давление': 72, 'Частота сердечных сокращений': 104,
                  'Толщина жировой складки (живот)': 3.3,
                  'Толщина жировой складки (плечо)': 1.6,
                  'Толщина жировой складки (спина)': 2.0},
                 {'Длина тела': 164.4, 'Масса тела': 75.4, 'Индекс Кетле': 28.6, 'Окружность грудной клетки': 94.4,
                  'Окружность талии': 90.0, 'Окружность правого плеча': 31.0,
                  'Окружность левого плеча': 31.5, 'Окружность бёдер': 105.0, 'Окружность шеи': 35.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.55, 'Динамометрия правой кисти': 26.0,
                  'Динамометрия левой кисти': 25.0, 'Сист. артериальное давление': 133,
                  'Диаст. артериальное давление': 74, 'Частота сердечных сокращений': 109,
                  'Толщина жировой складки (живот)': 4.9,
                  'Толщина жировой складки (плечо)': 2.0,
                  'Толщина жировой складки (спина)': 3.3}])

            boy_13_insert = boy_13.insert()
            boy_13_insert.compile()
            boy_13_insert.execute(
                [{'Длина тела': 143.8, 'Масса тела': 31.9, 'Индекс Кетле': 14.9, 'Окружность грудной клетки': 64.0,
                  'Окружность талии': 53.8, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 18.5, 'Окружность бёдер': 70.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 14.0, 'Сист. артериальное давление': 96,
                  'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 65,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 146.6, 'Масса тела': 35.34, 'Индекс Кетле': 16.1, 'Окружность грудной клетки': 65.1,
                  'Окружность талии': 58.9, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 72.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 2.1, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 101,
                  'Диаст. артериальное давление': 53, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 151.9, 'Масса тела': 40.4, 'Индекс Кетле': 16.6, 'Окружность грудной клетки': 68.9,
                  'Окружность талии': 60.9, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 76.0, 'Окружность шеи': 29.5,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.5, 'Динамометрия правой кисти': 18.0,
                  'Динамометрия левой кисти': 18.0, 'Сист. артериальное давление': 106,
                  'Диаст. артериальное давление': 58, 'Частота сердечных сокращений': 78.0,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 159.3, 'Масса тела': 46.9, 'Индекс Кетле': 18.5, 'Окружность грудной клетки': 73.2,
                  'Окружность талии': 65.7, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 82.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 3.0, 'Динамометрия правой кисти': 22.0,
                  'Динамометрия левой кисти': 22.0, 'Сист. артериальное давление': 115,
                  'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 86,
                  'Толщина жировой складки (живот)': 1.2,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 164.6, 'Масса тела': 53.1, 'Индекс Кетле': 20.6, 'Окружность грудной клетки': 78.7,
                  'Окружность талии': 71.6, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 25.0, 'Окружность бёдер': 86.00, 'Окружность шеи': 33.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.5, 'Динамометрия правой кисти': 26.0,
                  'Динамометрия левой кисти': 25.0, 'Сист. артериальное давление': 121,
                  'Диаст. артериальное давление': 67.0, 'Частота сердечных сокращений': 95,
                  'Толщина жировой складки (живот)': 1.8,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 168.3, 'Масса тела': 62.15, 'Индекс Кетле': 21.8, 'Окружность грудной клетки': 83.6,
                  'Окружность талии': 77.3, 'Окружность правого плеча': 27.0,
                  'Окружность левого плеча': 27.0, 'Окружность бёдер': 92.0, 'Окружность шеи': 35.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 4.0, 'Динамометрия правой кисти': 32.0,
                  'Динамометрия левой кисти': 29.0, 'Сист. артериальное давление': 128,
                  'Диаст. артериальное давление': 72, 'Частота сердечных сокращений': 107,
                  'Толщина жировой складки (живот)': 2.3,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.6},
                 {'Длина тела': 172.2, 'Масса тела': 71.6, 'Индекс Кетле': 25.3, 'Окружность грудной клетки': 93.0,
                  'Окружность талии': 89.2, 'Окружность правого плеча': 29.5,
                  'Окружность левого плеча': 29.5, 'Окружность бёдер': 98.0, 'Окружность шеи': 36.0,
                  'Окружность запястья': 17.5, 'Жизненная ёмкость лёгких': 4.3, 'Динамометрия правой кисти': 35.0,
                  'Динамометрия левой кисти': 31.0, 'Сист. артериальное давление': 132,
                  'Диаст. артериальное давление': 77, 'Частота сердечных сокращений': 112,
                  'Толщина жировой складки (живот)': 3.6,
                  'Толщина жировой складки (плечо)': 1.9,
                  'Толщина жировой складки (спина)': 2.6}])

            boy_14_insert = boy_14.insert()
            boy_14_insert.compile()
            boy_14_insert.execute(
                [{'Длина тела': 151.1, 'Масса тела': 35.4, 'Индекс Кетле': 15.5, 'Окружность грудной клетки': 66.0,
                  'Окружность талии': 60.0, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 70.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 17.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 101,
                  'Диаст. артериальное давление': 53, 'Частота сердечных сокращений': 67,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 154.8, 'Масса тела': 41.15, 'Индекс Кетле': 16.6, 'Окружность грудной клетки': 70.6,
                  'Окружность талии': 61.5, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 76.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.6, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 18.0, 'Сист. артериальное давление': 106,
                  'Диаст. артериальное давление': 54, 'Частота сердечных сокращений': 69,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 159.9, 'Масса тела': 46.8, 'Индекс Кетле': 17.4, 'Окружность грудной клетки': 73.7,
                  'Окружность талии': 63.9, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 22.0, 'Окружность бёдер': 80.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 3.0, 'Динамометрия правой кисти': 22.0,
                  'Динамометрия левой кисти': 21.0, 'Сист. артериальное давление': 111,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 77.0,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 166.4, 'Масса тела': 54.2, 'Индекс Кетле': 19.3, 'Окружность грудной клетки': 78.7,
                  'Окружность талии': 68.5, 'Окружность правого плеча': 24.0,
                  'Окружность левого плеча': 24.0, 'Окружность бёдер': 86.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.5, 'Динамометрия правой кисти': 27.0,
                  'Динамометрия левой кисти': 25.0, 'Сист. артериальное давление': 117,
                  'Диаст. артериальное давление': 64, 'Частота сердечных сокращений': 85,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 172.0, 'Масса тела': 62.1, 'Индекс Кетле': 21.8, 'Окружность грудной клетки': 84.6,
                  'Окружность талии': 74.6, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 91.00, 'Окружность шеи': 34.0,
                  'Окружность запястья': 16.5, 'Жизненная ёмкость лёгких': 4.0, 'Динамометрия правой кисти': 32.0,
                  'Динамометрия левой кисти': 30.0, 'Сист. артериальное давление': 128,
                  'Диаст. артериальное давление': 70.0, 'Частота сердечных сокращений': 96,
                  'Толщина жировой складки (живот)': 1.8,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 177.9, 'Масса тела': 74.70, 'Индекс Кетле': 23.6, 'Окружность грудной клетки': 90.4,
                  'Окружность талии': 81.7, 'Окружность правого плеча': 28.5,
                  'Окружность левого плеча': 29.0, 'Окружность бёдер': 96.0, 'Окружность шеи': 36.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 4.6, 'Динамометрия правой кисти': 38.0,
                  'Динамометрия левой кисти': 36.0, 'Сист. артериальное давление': 136,
                  'Диаст. артериальное давление': 76, 'Частота сердечных сокращений': 106,
                  'Толщина жировой складки (живот)': 2.5,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.5},
                 {'Длина тела': 182.7, 'Масса тела': 88.4, 'Индекс Кетле': 28.4, 'Окружность грудной клетки': 101.0,
                  'Окружность талии': 94.7, 'Окружность правого плеча': 31.0,
                  'Окружность левого плеча': 32.0, 'Окружность бёдер': 109.0, 'Окружность шеи': 37.5,
                  'Окружность запястья': 18.0, 'Жизненная ёмкость лёгких': 5.0, 'Динамометрия правой кисти': 40.0,
                  'Динамометрия левой кисти': 40.0, 'Сист. артериальное давление': 142,
                  'Диаст. артериальное давление': 84, 'Частота сердечных сокращений': 110,
                  'Толщина жировой складки (живот)': 4.0,
                  'Толщина жировой складки (плечо)': 2.0,
                  'Толщина жировой складки (спина)': 2.8}])

            boy_15_insert = boy_15.insert()
            boy_15_insert.compile()
            boy_15_insert.execute(
                [{'Длина тела': 156.9, 'Масса тела': 41.8, 'Индекс Кетле': 16.5, 'Окружность грудной клетки': 71.0,
                  'Окружность талии': 63.0, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 76.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.5, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 20.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 67,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 163.8, 'Масса тела': 51.00, 'Индекс Кетле': 18.0, 'Окружность грудной клетки': 75.8,
                  'Окружность талии': 64.3, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 22.5, 'Окружность бёдер': 81.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.7, 'Динамометрия правой кисти': 24.0,
                  'Динамометрия левой кисти': 22.0, 'Сист. артериальное давление': 111,
                  'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 168.1, 'Масса тела': 53.7, 'Индекс Кетле': 18.5, 'Окружность грудной клетки': 78.6,
                  'Окружность талии': 67.3, 'Окружность правого плеча': 24.0,
                  'Окружность левого плеча': 24.0, 'Окружность бёдер': 86.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.3, 'Динамометрия правой кисти': 28.0,
                  'Динамометрия левой кисти': 27.0, 'Сист. артериальное давление': 118,
                  'Диаст. артериальное давление': 61, 'Частота сердечных сокращений': 78.0,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 171.8, 'Масса тела': 59.5, 'Индекс Кетле': 20.1, 'Окружность грудной клетки': 82.5,
                  'Окружность талии': 69.5, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 25.5, 'Окружность бёдер': 89.0, 'Окружность шеи': 34.5,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.8, 'Динамометрия правой кисти': 34.5,
                  'Динамометрия левой кисти': 32.0, 'Сист. артериальное давление': 124,
                  'Диаст. артериальное давление': 66, 'Частота сердечных сокращений': 85,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 176.3, 'Масса тела': 65.9, 'Индекс Кетле': 21.9, 'Окружность грудной клетки': 87.9,
                  'Окружность талии': 75.6, 'Окружность правого плеча': 28.0,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 93.00, 'Окружность шеи': 36.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 4.4, 'Динамометрия правой кисти': 40.0,
                  'Динамометрия левой кисти': 37.0, 'Сист. артериальное давление': 134,
                  'Диаст. артериальное давление': 71.0, 'Частота сердечных сокращений': 93,
                  'Толщина жировой складки (живот)': 1.85,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 180.5, 'Масса тела': 81.00, 'Индекс Кетле': 23.8, 'Окружность грудной клетки': 96.4,
                  'Окружность талии': 87.0, 'Окружность правого плеча': 30.0,
                  'Окружность левого плеча': 30.5, 'Окружность бёдер': 102.0, 'Окружность шеи': 38.0,
                  'Окружность запястья': 18.0, 'Жизненная ёмкость лёгких': 5.0, 'Динамометрия правой кисти': 42.0,
                  'Динамометрия левой кисти': 41.0, 'Сист. артериальное давление': 138,
                  'Диаст. артериальное давление': 76, 'Частота сердечных сокращений': 104,
                  'Толщина жировой складки (живот)': 2.3,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.3},
                 {'Длина тела': 183.6, 'Масса тела': 96.2, 'Индекс Кетле': 30.2, 'Окружность грудной клетки': 106.0,
                  'Окружность талии': 97.0, 'Окружность правого плеча': 33.0,
                  'Окружность левого плеча': 33.0, 'Окружность бёдер': 112.0, 'Окружность шеи': 40.0,
                  'Окружность запястья': 19.0, 'Жизненная ёмкость лёгких': 5.7, 'Динамометрия правой кисти': 46.0,
                  'Динамометрия левой кисти': 44.0, 'Сист. артериальное давление': 146,
                  'Диаст. артериальное давление': 77, 'Частота сердечных сокращений': 108,
                  'Толщина жировой складки (живот)': 3.8,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 2.8}])

            boy_16_insert = boy_16.insert()
            boy_16_insert.compile()
            boy_16_insert.execute(
                [{'Длина тела': 161.7, 'Масса тела': 47.4, 'Индекс Кетле': 17.1, 'Окружность грудной клетки': 73.4,
                  'Окружность талии': 63.2, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 21.5, 'Окружность бёдер': 81.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.2, 'Динамометрия правой кисти': 23.0,
                  'Динамометрия левой кисти': 22.0, 'Сист. артериальное давление': 109,
                  'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 67,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.3,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 165.4, 'Масса тела': 51.48, 'Индекс Кетле': 18.0, 'Окружность грудной клетки': 77.2,
                  'Окружность талии': 65.5, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 84.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.9, 'Динамометрия правой кисти': 26.0,
                  'Динамометрия левой кисти': 24.0, 'Сист. артериальное давление': 112,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 70,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 169.7, 'Масса тела': 54.9, 'Индекс Кетле': 18.5, 'Окружность грудной клетки': 80.9,
                  'Окружность талии': 67.9, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 24.5, 'Окружность бёдер': 87.0, 'Окружность шеи': 34.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.5, 'Динамометрия правой кисти': 31.0,
                  'Динамометрия левой кисти': 29.0, 'Сист. артериальное давление': 117,
                  'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 78.0,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 174.2, 'Масса тела': 60.2, 'Индекс Кетле': 20.1, 'Окружность грудной клетки': 83.4,
                  'Окружность талии': 70.8, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 91.0, 'Окружность шеи': 35.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 4.1, 'Динамометрия правой кисти': 36.5,
                  'Динамометрия левой кисти': 32.0, 'Сист. артериальное давление': 125,
                  'Диаст. артериальное давление': 68, 'Частота сердечных сокращений': 87,
                  'Толщина жировой складки (живот)': 1.1,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 178.8, 'Масса тела': 68.2, 'Индекс Кетле': 21.7, 'Окружность грудной клетки': 87.9,
                  'Окружность талии': 75.5, 'Окружность правого плеча': 28.0,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 94.0, 'Окружность шеи': 36.5,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 4.9, 'Динамометрия правой кисти': 40.0,
                  'Динамометрия левой кисти': 38.0, 'Сист. артериальное давление': 133,
                  'Диаст. артериальное давление': 73.0, 'Частота сердечных сокращений': 98,
                  'Толщина жировой складки (живот)': 1.8,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 182.3, 'Масса тела': 74.9, 'Индекс Кетле': 23.2, 'Окружность грудной клетки': 93.6,
                  'Окружность талии': 80.6, 'Окружность правого плеча': 30.0,
                  'Окружность левого плеча': 30.0, 'Окружность бёдер': 101.0, 'Окружность шеи': 38.0,
                  'Окружность запястья': 18.0, 'Жизненная ёмкость лёгких': 5.4, 'Динамометрия правой кисти': 44.0,
                  'Динамометрия левой кисти': 40.0, 'Сист. артериальное давление': 141,
                  'Диаст. артериальное давление': 80, 'Частота сердечных сокращений': 111,
                  'Толщина жировой складки (живот)': 2.2,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.6},
                 {'Длина тела': 186.6, 'Масса тела': 95.0, 'Индекс Кетле': 28.8, 'Окружность грудной клетки': 106.0,
                  'Окружность талии': 97.0, 'Окружность правого плеча': 33.0,
                  'Окружность левого плеча': 34.0, 'Окружность бёдер': 112.0, 'Окружность шеи': 40.0,
                  'Окружность запястья': 18.5, 'Жизненная ёмкость лёгких': 5.8, 'Динамометрия правой кисти': 46.0,
                  'Динамометрия левой кисти': 42.0, 'Сист. артериальное давление': 148,
                  'Диаст. артериальное давление': 82, 'Частота сердечных сокращений': 119,
                  'Толщина жировой складки (живот)': 3.7,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 2.5}])

            boy_17_insert = boy_17.insert()
            boy_17_insert.compile()
            boy_17_insert.execute(
                [{'Длина тела': 162.6, 'Масса тела': 46.3, 'Индекс Кетле': 17.1, 'Окружность грудной клетки': 75.0,
                  'Окружность талии': 64.0, 'Окружность правого плеча': 22.5,
                  'Окружность левого плеча': 22.0, 'Окружность бёдер': 84.0, 'Окружность шеи': 31.5,
                  'Окружность запястья': 15.1, 'Жизненная ёмкость лёгких': 3.1, 'Динамометрия правой кисти': 28.0,
                  'Динамометрия левой кисти': 25.0, 'Сист. артериальное давление': 111,
                  'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 64,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.3,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 168.0, 'Масса тела': 53.80, 'Индекс Кетле': 18.1, 'Окружность грудной клетки': 78.5,
                  'Окружность талии': 64.5, 'Окружность правого плеча': 24.0,
                  'Окружность левого плеча': 24.0, 'Окружность бёдер': 86.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.3, 'Динамометрия правой кисти': 30.0,
                  'Динамометрия левой кисти': 29.0, 'Сист. артериальное давление': 114,
                  'Диаст. артериальное давление': 61, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 171.2, 'Масса тела': 57.9, 'Индекс Кетле': 19.1, 'Окружность грудной клетки': 82.9,
                  'Окружность талии': 70.2, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 90.0, 'Окружность шеи': 34.5,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.9, 'Динамометрия правой кисти': 36.0,
                  'Динамометрия левой кисти': 32.0, 'Сист. артериальное давление': 123,
                  'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 76.0,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 175.5, 'Масса тела': 65.0, 'Индекс Кетле': 20.5, 'Окружность грудной клетки': 86.3,
                  'Окружность талии': 73.7, 'Окружность правого плеча': 27.5,
                  'Окружность левого плеча': 27.5, 'Окружность бёдер': 92.0, 'Окружность шеи': 36.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 4.6, 'Динамометрия правой кисти': 40.0,
                  'Динамометрия левой кисти': 38.0, 'Сист. артериальное давление': 130,
                  'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 87,
                  'Толщина жировой складки (живот)': 1.5,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 1.1},
                 {'Длина тела': 179.8, 'Масса тела': 72.1, 'Индекс Кетле': 23.1, 'Окружность грудной клетки': 90.8,
                  'Окружность талии': 80.4, 'Окружность правого плеча': 30.5,
                  'Окружность левого плеча': 29.5, 'Окружность бёдер': 99.0, 'Окружность шеи': 37.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 5.3, 'Динамометрия правой кисти': 45.0,
                  'Динамометрия левой кисти': 41.0, 'Сист. артериальное давление': 138,
                  'Диаст. артериальное давление': 76.0, 'Частота сердечных сокращений': 94,
                  'Толщина жировой складки (живот)': 2.4,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.6},
                 {'Длина тела': 183.3, 'Масса тела': 79.0, 'Индекс Кетле': 24.5, 'Окружность грудной клетки': 95.5,
                  'Окружность талии': 87.5, 'Окружность правого плеча': 32.0,
                  'Окружность левого плеча': 31.0, 'Окружность бёдер': 105.0, 'Окружность шеи': 39.0,
                  'Окружность запястья': 18.0, 'Жизненная ёмкость лёгких': 5.6, 'Динамометрия правой кисти': 50.0,
                  'Динамометрия левой кисти': 47.0, 'Сист. артериальное давление': 147,
                  'Диаст. артериальное давление': 79, 'Частота сердечных сокращений': 107,
                  'Толщина жировой складки (живот)': 3.1,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 2.1},
                 {'Длина тела': 187.9, 'Масса тела': 93.7, 'Индекс Кетле': 26.8, 'Окружность грудной клетки': 100.9,
                  'Окружность талии': 99.0, 'Окружность правого плеча': 34.0,
                  'Окружность левого плеча': 33.0, 'Окружность бёдер': 116.0, 'Окружность шеи': 40.0,
                  'Окружность запястья': 19.0, 'Жизненная ёмкость лёгких': 5.8, 'Динамометрия правой кисти': 52.0,
                  'Динамометрия левой кисти': 48.0, 'Сист. артериальное давление': 151,
                  'Диаст. артериальное давление': 81, 'Частота сердечных сокращений': 110,
                  'Толщина жировой складки (живот)': 4.2,
                  'Толщина жировой складки (плечо)': 1.8,
                  'Толщина жировой складки (спина)': 2.7}])

            girl_3_insert = girl_3.insert()
            girl_3_insert.compile()
            girl_3_insert.execute(
                [{'Длина тела': 86.0, 'Масса тела': 11.3, 'Окружность грудной клетки': 48.0,
                  'Частота сердечных сокращений': 92},
                 {'Длина тела': 89.0, 'Масса тела': 12.1, 'Окружность грудной клетки': 49.0,
                  'Частота сердечных сокращений': 92},
                 {'Длина тела': 92.0, 'Масса тела': 13.0, 'Окружность грудной клетки': 50.0,
                  'Частота сердечных сокращений': 95},
                 {'Длина тела': 95.0, 'Масса тела': 14.15, 'Окружность грудной клетки': 52.0,
                  'Частота сердечных сокращений': 112},
                 {'Длина тела': 98.0, 'Масса тела': 15.5, 'Окружность грудной клетки': 54.0,
                  'Частота сердечных сокращений': 114},
                 {'Длина тела': 102.5, 'Масса тела': 16.9, 'Окружность грудной клетки': 55.0,
                  'Частота сердечных сокращений': 128},
                 {'Длина тела': 107.0, 'Масса тела': 19.8, 'Окружность грудной клетки': 55.0,
                  'Частота сердечных сокращений': 128}])

            girl_35_insert = girl_35.insert()
            girl_35_insert.compile()
            girl_35_insert.execute(
                [{'Длина тела': 91.0, 'Масса тела': 12.7, 'Окружность грудной клетки': 47.0,
                  'Жизненная ёмкость лёгких': 0.6,  'Частота сердечных сокращений': 88},
                 {'Длина тела': 94.0, 'Масса тела': 13.5, 'Окружность грудной клетки': 50.0,
                  'Жизненная ёмкость лёгких': 0.6,  'Частота сердечных сокращений': 90},
                 {'Длина тела': 96.0, 'Масса тела': 14.0, 'Окружность грудной клетки': 52.0,
                  'Жизненная ёмкость лёгких': 0.6, 'Частота сердечных сокращений': 98},
                 {'Длина тела': 19.0, 'Масса тела': 15.25, 'Окружность грудной клетки': 53.0,
                  'Жизненная ёмкость лёгких': 0.8,  'Частота сердечных сокращений': 104},
                 {'Длина тела': 102.0, 'Масса тела': 16.5, 'Окружность грудной клетки': 54.0,
                  'Жизненная ёмкость лёгких': 0.8,  'Частота сердечных сокращений': 108},
                 {'Длина тела': 104.0, 'Масса тела': 18.0, 'Окружность грудной клетки': 56.0,
                  'Жизненная ёмкость лёгких': 0.8,  'Частота сердечных сокращений': 120},
                 {'Длина тела': 107.0, 'Масса тела': 19.8, 'Окружность грудной клетки': 58.0,
                  'Жизненная ёмкость лёгких': 0.8,  'Частота сердечных сокращений': 140}])

            girl_4_insert = girl_4.insert()
            girl_4_insert.compile()
            girl_4_insert.execute(
                [{'Длина тела': 94.0, 'Масса тела': 12.5, 'Окружность грудной клетки': 47.0,
                  'Жизненная ёмкость лёгких': 0.7, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 40,
                  'Частота сердечных сокращений': 84},
                 {'Длина тела': 98.0, 'Масса тела': 14.0, 'Окружность грудной клетки': 50.0,
                  'Жизненная ёмкость лёгких': 0.7, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 40,
                  'Частота сердечных сокращений': 88},
                 {'Длина тела': 100.0, 'Масса тела': 15.05, 'Окружность грудной клетки': 52.0,
                  'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 55,
                  'Частота сердечных сокращений': 92},
                 {'Длина тела': 103.0, 'Масса тела': 16.5, 'Окружность грудной клетки': 54.0,
                  'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 3,
                  'Сист. артериальное давление': 84, 'Диаст. артериальное давление': 62,
                  'Частота сердечных сокращений': 100},
                 {'Длина тела': 106.75, 'Масса тела': 18.0, 'Окружность грудной клетки': 55.0,
                  'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 4,
                  'Сист. артериальное давление': 92, 'Диаст. артериальное давление': 68,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 109.5, 'Масса тела': 19.5, 'Окружность грудной клетки': 57.0,
                  'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 5,
                  'Сист. артериальное давление': 104, 'Диаст. артериальное давление': 74,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 112.0, 'Масса тела': 22.0, 'Окружность грудной клетки': 60.0,
                  'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 5,
                  'Сист. артериальное давление': 104, 'Диаст. артериальное давление': 74,
                  'Частота сердечных сокращений': 108}])

            girl_45_insert = girl_45.insert()
            girl_45_insert.compile()
            girl_45_insert.execute(
                [{'Длина тела': 97.0, 'Масса тела': 13.7, 'Окружность грудной клетки': 49.0,
                  'Жизненная ёмкость лёгких': 0.7, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 50,
                  'Частота сердечных сокращений': 84},
                 {'Длина тела': 100.0, 'Масса тела': 14.6, 'Окружность грудной клетки': 52.0,
                  'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 50,
                  'Частота сердечных сокращений': 84},
                 {'Длина тела': 103.0, 'Масса тела': 16.0, 'Окружность грудной клетки': 53.0,
                  'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 52.5,
                  'Частота сердечных сокращений': 96},
                 {'Длина тела': 106.0, 'Масса тела': 17.1, 'Окружность грудной клетки': 54.0,
                  'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 84.5, 'Диаст. артериальное давление': 60,
                  'Частота сердечных сокращений': 102},
                 {'Длина тела': 110.0, 'Масса тела': 18.6, 'Окружность грудной клетки': 56.0,
                  'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 3.5, 'Динамометрия левой кисти': 3,
                  'Сист. артериальное давление': 92, 'Диаст. артериальное давление': 64,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 112.0, 'Масса тела': 20.4, 'Окружность грудной клетки': 58.0,
                  'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 4,
                  'Сист. артериальное давление': 96, 'Диаст. артериальное давление': 70,
                  'Частота сердечных сокращений': 116},
                 {'Длина тела': 116.0, 'Масса тела': 22.2, 'Окружность грудной клетки': 59.0,
                  'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 8, 'Динамометрия левой кисти': 8,
                  'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 72,
                  'Частота сердечных сокращений': 120}])

            girl_5_insert = girl_5.insert()
            girl_5_insert.compile()
            girl_5_insert.execute(
                [{'Длина тела': 102.0, 'Масса тела': 14.5, 'Окружность грудной клетки': 50.0,
                  'Жизненная ёмкость лёгких': 0.6, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 40,
                  'Частота сердечных сокращений': 72},
                 {'Длина тела': 104.0, 'Масса тела': 15.4, 'Окружность грудной клетки': 51.0,
                  'Жизненная ёмкость лёгких': 0.7, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 44,
                  'Частота сердечных сокращений': 78},
                 {'Длина тела': 107.0, 'Масса тела': 17.8, 'Окружность грудной клетки': 53.0,
                  'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 3,
                  'Сист. артериальное давление': 84, 'Диаст. артериальное давление': 50,
                  'Частота сердечных сокращений': 84},
                 {'Длина тела': 111.0, 'Масса тела': 18.5, 'Окружность грудной клетки': 55.0,
                  'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 4,
                  'Сист. артериальное давление': 90, 'Диаст. артериальное давление': 60.0,
                  'Частота сердечных сокращений': 96},
                 {'Длина тела': 114.0, 'Масса тела': 20.0, 'Окружность грудной клетки': 56.0,
                  'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 4,
                  'Сист. артериальное давление': 95, 'Диаст. артериальное давление': 65,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 116.0, 'Масса тела': 21.5, 'Окружность грудной клетки': 59.0,
                  'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 4,
                  'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 70,
                  'Частота сердечных сокращений': 118},
                 {'Длина тела': 119.0, 'Масса тела': 23.3, 'Окружность грудной клетки': 62.0,
                  'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 7, 'Динамометрия левой кисти': 5,
                  'Сист. артериальное давление': 105, 'Диаст. артериальное давление': 70,
                  'Частота сердечных сокращений': 120}])

            girl_55_insert = girl_55.insert()
            girl_55_insert.compile()
            girl_55_insert.execute(
                [{'Длина тела': 104.0, 'Масса тела': 15.3, 'Окружность грудной клетки': 51.0,
                  'Жизненная ёмкость лёгких': 0.6, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 40,
                  'Частота сердечных сокращений': 78},
                 {'Длина тела': 108.0, 'Масса тела': 16.2, 'Окружность грудной клетки': 52.0,
                  'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 1.5,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 50,
                  'Частота сердечных сокращений': 84},
                 {'Длина тела': 111.0, 'Масса тела': 17.7, 'Окружность грудной клетки': 54.0,
                  'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 50,
                  'Частота сердечных сокращений': 90},
                 {'Длина тела': 113.0, 'Масса тела': 19.5, 'Окружность грудной клетки': 56.0,
                  'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 4,
                  'Сист. артериальное давление': 90.0, 'Диаст. артериальное давление': 56,
                  'Частота сердечных сокращений': 96},
                 {'Длина тела': 117.0, 'Масса тела': 21.0, 'Окружность грудной клетки': 57.0,
                  'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 5,
                  'Сист. артериальное давление': 95, 'Диаст. артериальное давление': 60,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 121.0, 'Масса тела': 23.5, 'Окружность грудной клетки': 60.0,
                  'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 8, 'Динамометрия левой кисти': 8,
                  'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 70,
                  'Частота сердечных сокращений': 114},
                 {'Длина тела': 123.0, 'Масса тела': 27.0, 'Окружность грудной клетки': 64.0,
                  'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 8, 'Динамометрия левой кисти': 9,
                  'Сист. артериальное давление': 105, 'Диаст. артериальное давление': 70,
                  'Частота сердечных сокращений': 120}])

            girl_6_insert = girl_6.insert()
            girl_6_insert.compile()
            girl_6_insert.execute(
                [{'Длина тела': 107.0, 'Масса тела': 16.0, 'Окружность грудной клетки': 50.0,
                  'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 1, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 75, 'Диаст. артериальное давление': 40,
                  'Частота сердечных сокращений': 64},
                 {'Длина тела': 110.0, 'Масса тела': 17.2, 'Окружность грудной клетки': 53.0,
                  'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 44,
                  'Частота сердечных сокращений': 70},
                 {'Длина тела': 113.0, 'Масса тела': 18.45, 'Окружность грудной клетки': 54.0,
                  'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 4, 'Динамометрия левой кисти': 3,
                  'Сист. артериальное давление': 80, 'Диаст. артериальное давление': 50,
                  'Частота сердечных сокращений': 80},
                 {'Длина тела': 117.0, 'Масса тела': 20.3, 'Окружность грудной клетки': 55.0,
                  'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 5, 'Динамометрия левой кисти': 5,
                  'Сист. артериальное давление': 90, 'Диаст. артериальное давление': 60,
                  'Частота сердечных сокращений': 90},
                 {'Длина тела': 120.0, 'Масса тела': 22.1, 'Окружность грудной клетки': 58.0,
                  'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 8, 'Динамометрия левой кисти': 7,
                  'Сист. артериальное давление': 92, 'Диаст. артериальное давление': 60,
                  'Частота сердечных сокращений': 100},
                 {'Длина тела': 123.0, 'Масса тела': 24.3, 'Окружность грудной клетки': 61.0,
                  'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9, 'Динамометрия левой кисти': 9,
                  'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 65,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 126.0, 'Масса тела': 27.0, 'Окружность грудной клетки': 65.0,
                  'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 9, 'Динамометрия левой кисти': 10,
                  'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 68,
                  'Частота сердечных сокращений': 113}])

            girl_65_insert = girl_65.insert()
            girl_65_insert.compile()
            girl_65_insert.execute(
                [{'Длина тела': 111.0, 'Масса тела': 16.5, 'Окружность грудной клетки': 51.0,
                  'Жизненная ёмкость лёгких': 0.8, 'Динамометрия правой кисти': 2, 'Динамометрия левой кисти': 1,
                  'Сист. артериальное давление': 70, 'Диаст. артериальное давление': 38,
                  'Частота сердечных сокращений': 70},
                 {'Длина тела': 114.0, 'Масса тела': 17.9, 'Окружность грудной клетки': 52.0,
                  'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 3, 'Динамометрия левой кисти': 2,
                  'Сист. артериальное давление': 78, 'Диаст. артериальное давление': 42,
                  'Частота сердечных сокращений': 72},
                 {'Длина тела': 116.0, 'Масса тела': 19.5, 'Окружность грудной клетки': 54.0,
                  'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 6, 'Динамометрия левой кисти': 5,
                  'Сист. артериальное давление': 82, 'Диаст. артериальное давление': 48,
                  'Частота сердечных сокращений': 84},
                 {'Длина тела': 120.0, 'Масса тела': 21.2, 'Окружность грудной клетки': 56.0,
                  'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9, 'Динамометрия левой кисти': 8,
                  'Сист. артериальное давление': 90, 'Диаст. артериальное давление': 55,
                  'Частота сердечных сокращений': 94},
                 {'Длина тела': 123.0, 'Масса тела': 23.7, 'Окружность грудной клетки': 58.0,
                  'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 10, 'Динамометрия левой кисти': 10,
                  'Сист. артериальное давление': 95, 'Диаст. артериальное давление': 60,
                  'Частота сердечных сокращений': 101},
                 {'Длина тела': 126.0, 'Масса тела': 26.2, 'Окружность грудной клетки': 62.0,
                  'Жизненная ёмкость лёгких': 1.6, 'Динамометрия правой кисти': 11, 'Динамометрия левой кисти': 11,
                  'Сист. артериальное давление': 100, 'Диаст. артериальное давление': 60,
                  'Частота сердечных сокращений': 108},
                 {'Длина тела': 130.0, 'Масса тела': 29.7, 'Окружность грудной клетки': 65.0,
                  'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 13, 'Динамометрия левой кисти': 12,
                  'Сист. артериальное давление': 104, 'Диаст. артериальное давление': 70,
                  'Частота сердечных сокращений': 110}])

            girl_7_insert = girl_7.insert()
            girl_7_insert.compile()
            girl_7_insert.execute(
                [{'Длина тела': 113.6, 'Масса тела': 17.3, 'Индекс Кетле': 12.8, 'Окружность грудной клетки': 52.2,
                  'Окружность талии': 46.0, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча': 16.0, 'Окружность бёдер': 59.0, 'Окружность шеи': 24.1,
                  'Окружность запястья': 11.5, 'Жизненная ёмкость лёгких': 0.7, 'Динамометрия правой кисти': 4.0,
                  'Динамометрия левой кисти': 3.0, 'Сист. артериальное давление': 87,
                  'Диаст. артериальное давление': 47, 'Частота сердечных сокращений': 75,
                  'Толщина жировой складки (живот)': 0.4,
                  'Толщина жировой складки (плечо)': 0.4,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 117.7, 'Масса тела': 19.23, 'Индекс Кетле': 13.9, 'Окружность грудной клетки': 53.5,
                  'Окружность талии': 48.9, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча': 16.5, 'Окружность бёдер': 60.0, 'Окружность шеи': 25.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 5.0,
                  'Динамометрия левой кисти': 4.0, 'Сист. артериальное давление': 91,
                  'Диаст. артериальное давление': 49, 'Частота сердечных сокращений': 79,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 120.8, 'Масса тела': 21.7, 'Индекс Кетле': 14.4, 'Окружность грудной клетки': 55.7,
                  'Окружность талии': 51.9, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.5, 'Окружность бёдер': 63.0, 'Окружность шеи': 25.5,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 6.0,
                  'Динамометрия левой кисти': 5.0, 'Сист. артериальное давление': 97,
                  'Диаст. артериальное давление': 53, 'Частота сердечных сокращений': 86,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 124.6, 'Масса тела': 24.2, 'Индекс Кетле': 15.5, 'Окружность грудной клетки': 57.9,
                  'Окружность талии': 54.7, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 66.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 7.0,
                  'Динамометрия левой кисти': 7.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 95,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 127.9, 'Масса тела': 26.2, 'Индекс Кетле': 16.7, 'Окружность грудной клетки': 60.8,
                  'Окружность талии': 58.9, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 68.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 8.0, 'Сист. артериальное давление': 110,
                  'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 102,
                  'Толщина жировой складки (живот)': 1.35,
                  'Толщина жировой складки (плечо)': 1.1,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 130.6, 'Масса тела': 29.58, 'Индекс Кетле': 17.6, 'Окружность грудной клетки': 63.9,
                  'Окружность талии': 63.5, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 72.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 118,
                  'Диаст. артериальное давление': 71, 'Частота сердечных сокращений': 111,
                  'Толщина жировой складки (живот)': 1.7,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 132.9, 'Масса тела': 33.8, 'Индекс Кетле': 18.9, 'Окружность грудной клетки': 73.0,
                  'Окружность талии': 74.0, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 25.5, 'Окружность бёдер': 83.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 1.6, 'Динамометрия правой кисти': 11.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 122,
                  'Диаст. артериальное давление': 76, 'Частота сердечных сокращений': 116,
                  'Толщина жировой складки (живот)': 2.3,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 1.7}])

            girl_8_insert = girl_8.insert()
            girl_8_insert.compile()
            girl_8_insert.execute(
                [{'Длина тела': 119.3, 'Масса тела': 19.5, 'Индекс Кетле': 13.2, 'Окружность грудной клетки': 52.6,
                  'Окружность талии': 47.0, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча': 16.0, 'Окружность бёдер': 59.0, 'Окружность шеи': 24.0,
                  'Окружность запястья': 11.5, 'Жизненная ёмкость лёгких': 0.85, 'Динамометрия правой кисти': 5.0,
                  'Динамометрия левой кисти': 4.0, 'Сист. артериальное давление': 89,
                  'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 74,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 121.7, 'Масса тела': 21.36, 'Индекс Кетле': 13.9, 'Окружность грудной клетки': 54.9,
                  'Окружность талии': 49.1, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.0, 'Окружность бёдер': 61.0, 'Окружность шеи': 25.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 6.0,
                  'Динамометрия левой кисти': 5.0, 'Сист. артериальное давление': 91,
                  'Диаст. артериальное давление': 52, 'Частота сердечных сокращений': 77,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 125.6, 'Масса тела': 23.4, 'Индекс Кетле': 14.5, 'Окружность грудной клетки': 57.1,
                  'Окружность талии': 50.4, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 64.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.1, 'Динамометрия правой кисти': 7.0,
                  'Динамометрия левой кисти': 6.0, 'Сист. артериальное давление': 97,
                  'Диаст. артериальное давление': 56, 'Частота сердечных сокращений': 83,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 129.6, 'Масса тела': 26.2, 'Индекс Кетле': 15.7, 'Окружность грудной клетки': 59.7,
                  'Окружность талии': 54.0, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 67.0, 'Окружность шеи': 26.5,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 8.0, 'Сист. артериальное давление': 103,
                  'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 92,
                  'Толщина жировой складки (живот)': 1.1,
                  'Толщина жировой складки (плечо)': 0.95,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 132.7, 'Масса тела': 29.7, 'Индекс Кетле': 17.4, 'Окружность грудной клетки': 63.5,
                  'Окружность талии': 57.9, 'Окружность правого плеча': 20.5,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 72.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 110,
                  'Диаст. артериальное давление': 65, 'Частота сердечных сокращений': 101,
                  'Толщина жировой складки (живот)': 1.7,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 135.7, 'Масса тела': 35.3, 'Индекс Кетле': 18.6, 'Окружность грудной клетки': 68.6,
                  'Окружность талии': 64.4, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 77.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 11.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 115,
                  'Диаст. артериальное давление': 69, 'Частота сердечных сокращений': 109,
                  'Толщина жировой складки (живот)': 2.0,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.4},
                 {'Длина тела': 141.1, 'Масса тела': 46.2, 'Индекс Кетле': 22.9, 'Окружность грудной клетки': 79.2,
                  'Окружность талии': 76.0, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 86.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 1.9, 'Динамометрия правой кисти': 13.0,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 119,
                  'Диаст. артериальное давление': 71, 'Частота сердечных сокращений': 111,
                  'Толщина жировой складки (живот)': 2.8,
                  'Толщина жировой складки (плечо)': 1.8,
                  'Толщина жировой складки (спина)': 2.1}])

            girl_9_insert = girl_9.insert()
            girl_9_insert.compile()
            girl_9_insert.execute(
                [{'Длина тела': 122.8, 'Масса тела': 21.9, 'Индекс Кетле': 13.3, 'Окружность грудной клетки': 53.8,
                  'Окружность талии': 49.0, 'Окружность правого плеча': 16.0,
                  'Окружность левого плеча': 16.5, 'Окружность бёдер': 62.0, 'Окружность шеи': 25.0,
                  'Окружность запястья': 11.5, 'Жизненная ёмкость лёгких': 0.9, 'Динамометрия правой кисти': 7.0,
                  'Динамометрия левой кисти': 5.0, 'Сист. артериальное давление': 91,
                  'Диаст. артериальное давление': 49, 'Частота сердечных сокращений': 73,
                  'Толщина жировой складки (живот)': 0.5,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.3},
                 {'Длина тела': 127.2, 'Масса тела': 24.08, 'Индекс Кетле': 14.3, 'Окружность грудной клетки': 56.6,
                  'Окружность талии': 49.8, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.0, 'Окружность бёдер': 64.0, 'Окружность шеи': 25.75,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 8.0,
                  'Динамометрия левой кисти': 6.0, 'Сист. артериальное давление': 93,
                  'Диаст. артериальное давление': 52, 'Частота сердечных сокращений': 75,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 129.9, 'Масса тела': 25.7, 'Индекс Кетле': 14.9, 'Окружность грудной клетки': 59.0,
                  'Окружность талии': 52.0, 'Окружность правого плеча': 18.75,
                  'Окружность левого плеча': 18.5, 'Окружность бёдер': 67.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 8.0, 'Сист. артериальное давление': 98,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 82,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 133.4, 'Масса тела': 28.7, 'Индекс Кетле': 16.1, 'Окружность грудной клетки': 61.8,
                  'Окружность талии': 54.8, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 70.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 90,
                  'Толщина жировой складки (живот)': 1.1,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 137.7, 'Масса тела': 31.9, 'Индекс Кетле': 17.7, 'Окружность грудной клетки': 65.2,
                  'Окружность талии': 59.6, 'Окружность правого плеча': 21.25,
                  'Окружность левого плеча': 21.25, 'Окружность бёдер': 74.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 12.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 111,
                  'Диаст. артериальное давление': 66, 'Частота сердечных сокращений': 98,
                  'Толщина жировой складки (живот)': 1.7,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 142.8, 'Масса тела': 38.98, 'Индекс Кетле': 18.9, 'Окружность грудной клетки': 71.0,
                  'Окружность талии': 64.8, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 79.0, 'Окружность шеи': 29.25,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 14.0,
                  'Динамометрия левой кисти': 13.0, 'Сист. артериальное давление': 119,
                  'Диаст. артериальное давление': 73, 'Частота сердечных сокращений': 105,
                  'Толщина жировой складки (живот)': 2.0,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 146.7, 'Масса тела': 43.4, 'Индекс Кетле': 20.9, 'Окружность грудной клетки': 76.2,
                  'Окружность талии': 68.8, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 25.0, 'Окружность бёдер': 84.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.2, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 125,
                  'Диаст. артериальное давление': 76, 'Частота сердечных сокращений': 112,
                  'Толщина жировой складки (живот)': 2.7,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 2.0}])

            girl_10_insert = girl_10.insert()
            girl_10_insert.compile()
            girl_10_insert.execute(
                [{'Длина тела': 129.0, 'Масса тела': 24.4, 'Индекс Кетле': 13.7, 'Окружность грудной клетки': 55.6,
                  'Окружность талии': 50.2, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 17.0, 'Окружность бёдер': 65.0, 'Окружность шеи': 25.5,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 7.0,
                  'Динамометрия левой кисти': 6.0, 'Сист. артериальное давление': 89,
                  'Диаст. артериальное давление': 47, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 0.6,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.4},
                 {'Длина тела': 132.2, 'Масса тела': 25.84, 'Индекс Кетле': 14.7, 'Окружность грудной клетки': 59.4,
                  'Окружность талии': 51.9, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 67.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 8.0,
                  'Динамометрия левой кисти': 7.0, 'Сист. артериальное давление': 93,
                  'Диаст. артериальное давление': 50, 'Частота сердечных сокращений': 74,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 135.6, 'Масса тела': 28.9, 'Индекс Кетле': 15.3, 'Окружность грудной клетки': 61.2,
                  'Окружность талии': 54.5, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 69.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.4, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 9.0, 'Сист. артериальное давление': 99,
                  'Диаст. артериальное давление': 56, 'Частота сердечных сокращений': 82,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 140.2, 'Масса тела': 33.4, 'Индекс Кетле': 16.7, 'Окружность грудной клетки': 64.9,
                  'Окружность талии': 58.5, 'Окружность правого плеча': 20.5,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 73.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 11.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 105,
                  'Диаст. артериальное давление': 61, 'Частота сердечных сокращений': 93,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 145.3, 'Масса тела': 38.2, 'Индекс Кетле': 18.7, 'Окружность грудной клетки': 69.8,
                  'Окружность талии': 62.6, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 22.5, 'Окружность бёдер': 79.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 13.0,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 112,
                  'Диаст. артериальное давление': 66, 'Частота сердечных сокращений': 99,
                  'Толщина жировой складки (живот)': 1.9,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 148.7, 'Масса тела': 43.82, 'Индекс Кетле': 20.2, 'Окружность грудной клетки': 74.7,
                  'Окружность талии': 66.1, 'Окружность правого плеча': 24.0,
                  'Окружность левого плеча': 24.0, 'Окружность бёдер': 83.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 14.0, 'Сист. артериальное давление': 119,
                  'Диаст. артериальное давление': 70, 'Частота сердечных сокращений': 108,
                  'Толщина жировой складки (живот)': 2.5,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.6},
                 {'Длина тела': 152.8, 'Масса тела': 53.8, 'Индекс Кетле': 23.7, 'Окружность грудной клетки': 81.8,
                  'Окружность талии': 80.0, 'Окружность правого плеча': 27.5,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 91.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.7, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 123,
                  'Диаст. артериальное давление': 75, 'Частота сердечных сокращений': 115,
                  'Толщина жировой складки (живот)': 3.6,
                  'Толщина жировой складки (плечо)': 2.1,
                  'Толщина жировой складки (спина)': 2.3}])

            girl_11_insert = girl_11.insert()
            girl_11_insert.compile()
            girl_11_insert.execute(
                [{'Длина тела': 130.7, 'Масса тела': 23.3, 'Индекс Кетле': 13.5, 'Окружность грудной клетки': 57.4,
                  'Окружность талии': 52.0, 'Окружность правого плеча': 16.5,
                  'Окружность левого плеча': 17.0, 'Окружность бёдер': 63.0, 'Окружность шеи': 25.0,
                  'Окружность запястья': 11.5, 'Жизненная ёмкость лёгких': 1.0, 'Динамометрия правой кисти': 8.0,
                  'Динамометрия левой кисти': 6.0, 'Сист. артериальное давление': 91,
                  'Диаст. артериальное давление': 49, 'Частота сердечных сокращений': 75,
                  'Толщина жировой складки (живот)': 0.7,
                  'Толщина жировой складки (плечо)': 0.5,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 137.3, 'Масса тела': 27.7, 'Индекс Кетле': 14.5, 'Окружность грудной клетки': 59.9,
                  'Окружность талии': 52.7, 'Окружность правого плеча': 18.0,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 67.0, 'Окружность шеи': 26.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.2, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 8.0, 'Сист. артериальное давление': 95,
                  'Диаст. артериальное давление': 52, 'Частота сердечных сокращений': 78,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 141.2, 'Масса тела': 31.6, 'Индекс Кетле': 15.2, 'Окружность грудной клетки': 63.0,
                  'Окружность талии': 55.3, 'Окружность правого плеча': 19.5,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 72.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 98,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 84.0,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 146.5, 'Масса тела': 36.4, 'Индекс Кетле': 17.0, 'Окружность грудной клетки': 66.6,
                  'Окружность талии': 58.8, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 75.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 13.5,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 105,
                  'Диаст. артериальное давление': 61, 'Частота сердечных сокращений': 92,
                  'Толщина жировой складки (живот)': 1.4,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 151.3, 'Масса тела': 41.9, 'Индекс Кетле': 19.2, 'Окружность грудной клетки': 72.6,
                  'Окружность талии': 63.9, 'Окружность правого плеча': 23.5,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 81.0, 'Окружность шеи': 29.5,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 113,
                  'Диаст. артериальное давление': 65.0, 'Частота сердечных сокращений': 101,
                  'Толщина жировой складки (живот)': 2.2,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.3},
                 {'Длина тела': 154.5, 'Масса тела': 49.75, 'Индекс Кетле': 20.1, 'Окружность грудной клетки': 79.3,
                  'Окружность талии': 69.5, 'Окружность правого плеча': 25.5,
                  'Окружность левого плеча': 25.0, 'Окружность бёдер': 86.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.7, 'Динамометрия правой кисти': 18.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 120,
                  'Диаст. артериальное давление': 71, 'Частота сердечных сокращений': 108,
                  'Толщина жировой складки (живот)': 2.6,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.8},
                 {'Длина тела': 157.8, 'Масса тела': 56.8, 'Индекс Кетле': 23.4, 'Окружность грудной клетки': 84.0,
                  'Окружность талии': 77.6, 'Окружность правого плеча': 28.0,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 94.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 2.9, 'Динамометрия правой кисти': 19.0,
                  'Динамометрия левой кисти': 19.0, 'Сист. артериальное давление': 122,
                  'Диаст. артериальное давление': 75, 'Частота сердечных сокращений': 112,
                  'Толщина жировой складки (живот)': 3.8,
                  'Толщина жировой складки (плечо)': 1.8,
                  'Толщина жировой складки (спина)': 2.6}])

            girl_12_insert = girl_12.insert()
            girl_12_insert.compile()
            girl_12_insert.execute(
                [{'Длина тела': 140.9, 'Масса тела': 31.2, 'Индекс Кетле': 14.5, 'Окружность грудной клетки': 64.0,
                  'Окружность талии': 53.9, 'Окружность правого плеча': 17.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 68.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.3, 'Динамометрия правой кисти': 9.0,
                  'Динамометрия левой кисти': 10.0, 'Сист. артериальное давление': 98,
                  'Диаст. артериальное давление': 52, 'Частота сердечных сокращений': 73,
                  'Толщина жировой складки (живот)': 0.8,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.5},
                 {'Длина тела': 144.3, 'Масса тела': 32.8, 'Индекс Кетле': 15.5, 'Окружность грудной клетки': 65.0,
                  'Окружность талии': 54.7, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 72.0, 'Окружность шеи': 27.5,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.6, 'Динамометрия правой кисти': 10.0,
                  'Динамометрия левой кисти': 11.0, 'Сист. артериальное давление': 100,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 79,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 147.9, 'Масса тела': 36.3, 'Индекс Кетле': 16.1, 'Окружность грудной клетки': 67.7,
                  'Окружность талии': 57.9, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 75.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 1.9, 'Динамометрия правой кисти': 14.0,
                  'Динамометрия левой кисти': 13.0, 'Сист. артериальное давление': 102,
                  'Диаст. артериальное давление': 58, 'Частота сердечных сокращений': 84.0,
                  'Толщина жировой складки (живот)': 1.1,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 151.7, 'Масса тела': 41.9, 'Индекс Кетле': 17.9, 'Окружность грудной клетки': 71.5,
                  'Окружность талии': 61.4, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 22.0, 'Окружность бёдер': 80.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.2, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 110,
                  'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 91,
                  'Толщина жировой складки (живот)': 1.5,
                  'Толщина жировой складки (плечо)': 1.1,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 156.7, 'Масса тела': 50.5, 'Индекс Кетле': 20.9, 'Окружность грудной клетки': 75.2,
                  'Окружность талии': 68.5, 'Окружность правого плеча': 24.5,
                  'Окружность левого плеча': 25.0, 'Окружность бёдер': 87.00, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.7, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 19.0, 'Сист. артериальное давление': 118,
                  'Диаст. артериальное давление': 69.0, 'Частота сердечных сокращений': 101,
                  'Толщина жировой складки (живот)': 2.4,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.5},
                 {'Длина тела': 161.8, 'Масса тела': 58.5, 'Индекс Кетле': 22.6, 'Окружность грудной клетки': 84.9,
                  'Окружность талии': 76.0, 'Окружность правого плеча': 28.0,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 94.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.0, 'Динамометрия правой кисти': 24.0,
                  'Динамометрия левой кисти': 22.5, 'Сист. артериальное давление': 125,
                  'Диаст. артериальное давление': 75, 'Частота сердечных сокращений': 110,
                  'Толщина жировой складки (живот)': 3.0,
                  'Толщина жировой складки (плечо)': 1.6,
                  'Толщина жировой складки (спина)': 1.9},
                 {'Длина тела': 165.8, 'Масса тела': 77.1, 'Индекс Кетле': 26.7, 'Окружность грудной клетки': 96.0,
                  'Окружность талии': 87.0, 'Окружность правого плеча': 30.0,
                  'Окружность левого плеча': 30.5, 'Окружность бёдер': 105.0, 'Окружность шеи': 34.5,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.2, 'Динамометрия правой кисти': 27.0,
                  'Динамометрия левой кисти': 24.0, 'Сист. артериальное давление': 131,
                  'Диаст. артериальное давление': 78, 'Частота сердечных сокращений': 113,
                  'Толщина жировой складки (живот)': 4.4,
                  'Толщина жировой складки (плечо)': 2.1,
                  'Толщина жировой складки (спина)': 2.7}])

            girl_13_insert = girl_13.insert()
            girl_13_insert.compile()
            girl_13_insert.execute(
                [{'Длина тела': 144.4, 'Масса тела': 32.7, 'Индекс Кетле': 15.1, 'Окружность грудной клетки': 62.8,
                  'Окружность талии': 53.8, 'Окружность правого плеча': 18.5,
                  'Окружность левого плеча': 18.0, 'Окружность бёдер': 69.0, 'Окружность шеи': 27.0,
                  'Окружность запястья': 12.0, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 14.0,
                  'Динамометрия левой кисти': 12.0, 'Сист. артериальное давление': 100,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 72,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 150.4, 'Масса тела': 37.5, 'Индекс Кетле': 16.3, 'Окружность грудной клетки': 65.6,
                  'Окружность талии': 56.3, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 19.5, 'Окружность бёдер': 75.5, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 14.0, 'Сист. артериальное давление': 103,
                  'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 74,
                  'Толщина жировой складки (живот)': 1.1,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.7},
                 {'Длина тела': 154.2, 'Масса тела': 42.6, 'Индекс Кетле': 16.9, 'Окружность грудной клетки': 70.5,
                  'Окружность талии': 59.5, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 81.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 2.1, 'Динамометрия правой кисти': 18.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 109,
                  'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 83.0,
                  'Толщина жировой складки (живот)': 1.4,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 158.0, 'Масса тела': 48.4, 'Индекс Кетле': 19.1, 'Окружность грудной клетки': 75.9,
                  'Окружность талии': 63.0, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 85.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.6, 'Динамометрия правой кисти': 21.0,
                  'Динамометрия левой кисти': 20.0, 'Сист. артериальное давление': 114,
                  'Диаст. артериальное давление': 66, 'Частота сердечных сокращений': 90,
                  'Толщина жировой складки (живот)': 1.8,
                  'Толщина жировой складки (плечо)': 1.1,
                  'Толщина жировой складки (спина)': 1.1},
                 {'Длина тела': 163.3, 'Масса тела': 54.0, 'Индекс Кетле': 21.3, 'Окружность грудной клетки': 80.0,
                  'Окружность талии': 68.6, 'Окружность правого плеча': 25.5,
                  'Окружность левого плеча': 25.0, 'Окружность бёдер': 91.5, 'Окружность шеи': 31.5,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.0, 'Динамометрия правой кисти': 25.0,
                  'Динамометрия левой кисти': 22.0, 'Сист. артериальное давление': 119,
                  'Диаст. артериальное давление': 71.0, 'Частота сердечных сокращений': 101,
                  'Толщина жировой складки (живот)': 2.1,
                  'Толщина жировой складки (плечо)': 1.4,
                  'Толщина жировой складки (спина)': 1.5},
                 {'Длина тела': 168.5, 'Масса тела': 62.1, 'Индекс Кетле': 22.3, 'Окружность грудной клетки': 85.5,
                  'Окружность талии': 72.6, 'Окружность правого плеча': 27.0,
                  'Окружность левого плеча': 27.0, 'Окружность бёдер': 96.5, 'Окружность шеи': 33.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.5, 'Динамометрия правой кисти': 27.0,
                  'Динамометрия левой кисти': 24.0, 'Сист. артериальное давление': 125,
                  'Диаст. артериальное давление': 73, 'Частота сердечных сокращений': 109,
                  'Толщина жировой складки (живот)': 2.4,
                  'Толщина жировой складки (плечо)': 1.6,
                  'Толщина жировой складки (спина)': 1.9},
                 {'Длина тела': 172.5, 'Масса тела': 69.8, 'Индекс Кетле': 25.3, 'Окружность грудной клетки': 89.5,
                  'Окружность талии': 82.0, 'Окружность правого плеча': 30.0,
                  'Окружность левого плеча': 30.0, 'Окружность бёдер': 103.0, 'Окружность шеи': 34.5,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.8, 'Динамометрия правой кисти': 30.0,
                  'Динамометрия левой кисти': 25.0, 'Сист. артериальное давление': 128,
                  'Диаст. артериальное давление': 77, 'Частота сердечных сокращений': 113,
                  'Толщина жировой складки (живот)': 3.7,
                  'Толщина жировой складки (плечо)': 1.9,
                  'Толщина жировой складки (спина)': 2.6}])

            girl_14_insert = girl_14.insert()
            girl_14_insert.compile()
            girl_14_insert.execute(
            [{'Длина тела': 151.3, 'Масса тела': 38.3, 'Индекс Кетле': 15.5, 'Окружность грудной клетки': 65.8,
                  'Окружность талии': 55.3, 'Окружность правого плеча': 19.0,
                  'Окружность левого плеча': 19.0, 'Окружность бёдер': 74.5, 'Окружность шеи': 27.5,
                  'Окружность запястья': 12.5, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 13.0, 'Сист. артериальное давление': 101,
                  'Диаст. артериальное давление': 55, 'Частота сердечных сокращений': 72,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.6,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 154.4, 'Масса тела': 42.1, 'Индекс Кетле': 16.9, 'Окружность грудной клетки': 69.4,
                  'Окружность талии': 58.4, 'Окружность правого плеча': 20.5,
                  'Окружность левого плеча': 20.5, 'Окружность бёдер': 79.0, 'Окружность шеи': 28.5,
                  'Окружность запястья': 13.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 103,
                  'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 76,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 157.9, 'Масса тела': 46.4, 'Индекс Кетле': 17.9, 'Окружность грудной клетки': 73.8,
                  'Окружность талии': 61.4, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 22.0, 'Окружность бёдер': 83.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.5, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 18.0, 'Сист. артериальное давление': 108,
                  'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 83.0,
                  'Толщина жировой складки (живот)': 1.5,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 161.9, 'Масса тела': 51.7, 'Индекс Кетле': 19.3, 'Окружность грудной клетки': 78.7,
                  'Окружность талии': 64.3, 'Окружность правого плеча': 23.5,
                  'Окружность левого плеча': 23.5, 'Окружность бёдер': 89.0, 'Окружность шеи': 30.5,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.8, 'Динамометрия правой кисти': 22.0,
                  'Динамометрия левой кисти': 21.0, 'Сист. артериальное давление': 114,
                  'Диаст. артериальное давление': 67, 'Частота сердечных сокращений': 92.5,
                  'Толщина жировой складки (живот)': 1.9,
                  'Толщина жировой складки (плечо)': 1.2,
                  'Толщина жировой складки (спина)': 1.2},
                 {'Длина тела': 165.9, 'Масса тела': 56.9, 'Индекс Кетле': 21.8, 'Окружность грудной клетки': 82.9,
                  'Окружность талии': 65.7, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 93.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.2, 'Динамометрия правой кисти': 26.0,
                  'Динамометрия левой кисти': 24.0, 'Сист. артериальное давление': 121,
                  'Диаст. артериальное давление': 71.0, 'Частота сердечных сокращений': 99.5,
                  'Толщина жировой складки (живот)': 2.5,
                  'Толщина жировой складки (плечо)': 1.6,
                  'Толщина жировой складки (спина)': 1.7},
                 {'Длина тела': 168.4, 'Масса тела': 65.5, 'Индекс Кетле': 23.9, 'Окружность грудной клетки': 87.9,
                  'Окружность талии': 76.6, 'Окружность правого плеча': 28.5,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 99.0, 'Окружность шеи': 33.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.5, 'Динамометрия правой кисти': 30.0,
                  'Динамометрия левой кисти': 26.0, 'Сист. артериальное давление': 129,
                  'Диаст. артериальное давление': 74, 'Частота сердечных сокращений': 108,
                  'Толщина жировой складки (живот)': 3.0,
                  'Толщина жировой складки (плечо)': 1.8,
                  'Толщина жировой складки (спина)': 2.2},
                 {'Длина тела': 173.8, 'Масса тела': 75.4, 'Индекс Кетле': 26.8, 'Окружность грудной клетки': 93.0,
                  'Окружность талии': 83.5, 'Окружность правого плеча': 30.0,
                  'Окружность левого плеча': 30.0, 'Окружность бёдер': 103.0, 'Окружность шеи': 35.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.7, 'Динамометрия правой кисти': 31.0,
                  'Динамометрия левой кисти': 28.0, 'Сист. артериальное давление': 132,
                  'Диаст. артериальное давление': 78, 'Частота сердечных сокращений': 114,
                  'Толщина жировой складки (живот)': 3.6,
                  'Толщина жировой складки (плечо)': 2.1,
                  'Толщина жировой складки (спина)': 2.8}])

            girl_15_insert = girl_15.insert()
            girl_15_insert.compile()
            girl_15_insert.execute(
                [{'Длина тела': 151.5, 'Масса тела': 39.2, 'Индекс Кетле': 16.1, 'Окружность грудной клетки': 68.5,
                  'Окружность талии': 56.7, 'Окружность правого плеча': 20.0,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 80.0, 'Окружность шеи': 28.0,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 16.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 100,
                  'Диаст. артериальное давление': 57, 'Частота сердечных сокращений': 70,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 153.9, 'Масса тела': 43.9, 'Индекс Кетле': 17.6, 'Окружность грудной клетки': 72.9,
                  'Окружность талии': 59.7, 'Окружность правого плеча': 21.25,
                  'Окружность левого плеча': 21.25, 'Окружность бёдер': 83.25, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.9, 'Динамометрия правой кисти': 18.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 103,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 74,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 0.8,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 157.8, 'Масса тела': 47.4, 'Индекс Кетле': 18.3, 'Окружность грудной клетки': 76.3,
                  'Окружность талии': 62.3, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 87.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.3, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 19.0, 'Сист. артериальное давление': 109,
                  'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 81.0,
                  'Толщина жировой складки (живот)': 1.5,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 161.8, 'Масса тела': 53.4, 'Индекс Кетле': 20.1, 'Окружность грудной клетки': 79.3,
                  'Окружность талии': 65.7, 'Окружность правого плеча': 24.5,
                  'Окружность левого плеча': 24.0, 'Окружность бёдер': 91.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.7, 'Динамометрия правой кисти': 24.0,
                  'Динамометрия левой кисти': 21.0, 'Сист. артериальное давление': 116,
                  'Диаст. артериальное давление': 68, 'Частота сердечных сокращений': 92,
                  'Толщина жировой складки (живот)': 1.9,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.3},
                 {'Длина тела': 166.9, 'Масса тела': 59.3, 'Индекс Кетле': 22.2, 'Окружность грудной клетки': 83.2,
                  'Окружность талии': 70.5, 'Окружность правого плеча': 26.0,
                  'Окружность левого плеча': 26.0, 'Окружность бёдер': 96.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.2, 'Динамометрия правой кисти': 27.0,
                  'Динамометрия левой кисти': 25.0, 'Сист. артериальное давление': 122,
                  'Диаст. артериальное давление': 73.0, 'Частота сердечных сокращений': 99,
                  'Толщина жировой складки (живот)': 2.6,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.8},
                 {'Длина тела': 171.8, 'Масса тела': 67.1, 'Индекс Кетле': 23.6, 'Окружность грудной клетки': 87.1,
                  'Окружность талии': 77.6, 'Окружность правого плеча': 29.0,
                  'Окружность левого плеча': 29.0, 'Окружность бёдер': 100.25, 'Окружность шеи': 34.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.6, 'Динамометрия правой кисти': 29.0,
                  'Динамометрия левой кисти': 27.0, 'Сист. артериальное давление': 130,
                  'Диаст. артериальное давление': 78, 'Частота сердечных сокращений': 106,
                  'Толщина жировой складки (живот)': 3.2,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 2.1},
                 {'Длина тела': 175.5, 'Масса тела': 78.5, 'Индекс Кетле': 26.3, 'Окружность грудной клетки': 97.0,
                  'Окружность талии': 92.1, 'Окружность правого плеча': 33.0,
                  'Окружность левого плеча': 33.0, 'Окружность бёдер': 110.0, 'Окружность шеи': 35.0,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 3.7, 'Динамометрия правой кисти': 30.0,
                  'Динамометрия левой кисти': 29.0, 'Сист. артериальное давление': 136,
                  'Диаст. артериальное давление': 82, 'Частота сердечных сокращений': 112,
                  'Толщина жировой складки (живот)': 4.2,
                  'Толщина жировой складки (плечо)': 2.1,
                  'Толщина жировой складки (спина)': 2.8}])

            girl_16_insert = girl_16.insert()
            girl_16_insert.compile()
            girl_16_insert.execute(
                [{'Длина тела': 152.9, 'Масса тела': 40.9, 'Индекс Кетле': 16.4, 'Окружность грудной клетки': 71.5,
                  'Окружность талии': 55.9, 'Окружность правого плеча': 20.5,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 80.0, 'Окружность шеи': 29.0,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 1.5, 'Динамометрия правой кисти': 18.0,
                  'Динамометрия левой кисти': 16.0, 'Сист. артериальное давление': 100,
                  'Диаст. артериальное давление': 58, 'Частота сердечных сокращений': 69,
                  'Толщина жировой складки (живот)': 0.9,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.6},
                 {'Длина тела': 156.9, 'Масса тела': 44.7, 'Индекс Кетле': 18.0, 'Окружность грудной клетки': 75.1,
                  'Окружность талии': 60.4, 'Окружность правого плеча': 22.0,
                  'Окружность левого плеча': 22.0, 'Окружность бёдер': 84.0, 'Окружность шеи': 29.5,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 1.8, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 18.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 73,
                  'Толщина жировой складки (живот)': 1.4,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 159.4, 'Масса тела': 49.8, 'Индекс Кетле': 18.7, 'Окружность грудной клетки': 77.6,
                  'Окружность талии': 63.0, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 88.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.4, 'Динамометрия правой кисти': 22.0,
                  'Динамометрия левой кисти': 20.0, 'Сист. артериальное давление': 110,
                  'Диаст. артериальное давление': 62, 'Частота сердечных сокращений': 83.0,
                  'Толщина жировой складки (живот)': 1.6,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 1.0},
                 {'Длина тела': 163.1, 'Масса тела': 54.0, 'Индекс Кетле': 19.9, 'Окружность грудной клетки': 80.4,
                  'Окружность талии': 66.3, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 24.75, 'Окружность бёдер': 93.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 2.9, 'Динамометрия правой кисти': 25.0,
                  'Динамометрия левой кисти': 23.0, 'Сист. артериальное давление': 115,
                  'Диаст. артериальное давление': 67, 'Частота сердечных сокращений': 92,
                  'Толщина жировой складки (живот)': 1.9,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.3},
                 {'Длина тела': 167.7, 'Масса тела': 59.6, 'Индекс Кетле': 21.9, 'Окружность грудной клетки': 84.0,
                  'Окружность талии': 70.0, 'Окружность правого плеча': 27.0,
                  'Окружность левого плеча': 26.5, 'Окружность бёдер': 97.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.4, 'Динамометрия правой кисти': 28.0,
                  'Динамометрия левой кисти': 26.0, 'Сист. артериальное давление': 120.5,
                  'Диаст. артериальное давление': 71.0, 'Частота сердечных сокращений': 100,
                  'Толщина жировой складки (живот)': 2.4,
                  'Толщина жировой складки (плечо)': 1.5,
                  'Толщина жировой складки (спина)': 1.7},
                 {'Длина тела': 170.9, 'Масса тела': 64.9, 'Индекс Кетле': 23.3, 'Окружность грудной клетки': 87.9,
                  'Окружность талии': 74.9, 'Окружность правого плеча': 29.0,
                  'Окружность левого плеча': 28.0, 'Окружность бёдер': 100.0, 'Окружность шеи': 34.0,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.7, 'Динамометрия правой кисти': 30.0,
                  'Динамометрия левой кисти': 28.0, 'Сист. артериальное давление': 128,
                  'Диаст. артериальное давление': 76, 'Частота сердечных сокращений': 108,
                  'Толщина жировой складки (живот)': 2.9,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 1.9},
                 {'Длина тела': 176.5, 'Масса тела': 75.0, 'Индекс Кетле': 25.8, 'Окружность грудной клетки': 96.0,
                  'Окружность талии': 86.0, 'Окружность правого плеча': 30.0,
                  'Окружность левого плеча': 30.0, 'Окружность бёдер': 104.0, 'Окружность шеи': 34.5,
                  'Окружность запястья': 17.0, 'Жизненная ёмкость лёгких': 4.3, 'Динамометрия правой кисти': 31.0,
                  'Динамометрия левой кисти': 30.0, 'Сист. артериальное давление': 131,
                  'Диаст. артериальное давление': 78, 'Частота сердечных сокращений': 113,
                  'Толщина жировой складки (живот)': 3.5,
                  'Толщина жировой складки (плечо)': 1.9,
                  'Толщина жировой складки (спина)': 2.7}])

            girl_17_insert = girl_17.insert()
            girl_17_insert.compile()
            girl_17_insert.execute(
                [{'Длина тела': 151.1, 'Масса тела': 40.4, 'Индекс Кетле': 16.5, 'Окружность грудной клетки': 72.6,
                  'Окружность талии': 56.6, 'Окружность правого плеча': 20.5,
                  'Окружность левого плеча': 20.0, 'Окружность бёдер': 81.0, 'Окружность шеи': 28.5,
                  'Окружность запястья': 13.5, 'Жизненная ёмкость лёгких': 1.7, 'Динамометрия правой кисти': 15.0,
                  'Динамометрия левой кисти': 15.0, 'Сист. артериальное давление': 101,
                  'Диаст. артериальное давление': 59, 'Частота сердечных сокращений': 66,
                  'Толщина жировой складки (живот)': 1.0,
                  'Толщина жировой складки (плечо)': 0.7,
                  'Толщина жировой складки (спина)': 0.8},
                 {'Длина тела': 155.1, 'Масса тела': 45.2, 'Индекс Кетле': 18.1, 'Окружность грудной клетки': 74.3,
                  'Окружность талии': 58.8, 'Окружность правого плеча': 21.0,
                  'Окружность левого плеча': 21.0, 'Окружность бёдер': 85.5, 'Окружность шеи': 29.0,
                  'Окружность запястья': 14.0, 'Жизненная ёмкость лёгких': 2.0, 'Динамометрия правой кисти': 20.0,
                  'Динамометрия левой кисти': 18.0, 'Сист. артериальное давление': 104,
                  'Диаст. артериальное давление': 60, 'Частота сердечных сокращений': 71,
                  'Толщина жировой складки (живот)': 1.3,
                  'Толщина жировой складки (плечо)': 0.9,
                  'Толщина жировой складки (спина)': 0.9},
                 {'Длина тела': 160.3, 'Масса тела': 49.8, 'Индекс Кетле': 18.8, 'Окружность грудной клетки': 77.3,
                  'Окружность талии': 62.8, 'Окружность правого плеча': 23.0,
                  'Окружность левого плеча': 23.0, 'Окружность бёдер': 88.0, 'Окружность шеи': 30.0,
                  'Окружность запястья': 14.5, 'Жизненная ёмкость лёгких': 2.5, 'Динамометрия правой кисти': 23.0,
                  'Динамометрия левой кисти': 21.0, 'Сист. артериальное давление': 109,
                  'Диаст. артериальное давление': 63, 'Частота сердечных сокращений': 78.0,
                  'Толщина жировой складки (живот)': 1.5,
                  'Толщина жировой складки (плечо)': 1.0,
                  'Толщина жировой складки (спина)': 1.1},
                 {'Длина тела': 164.0, 'Масса тела': 55.6, 'Индекс Кетле': 20.4, 'Окружность грудной клетки': 80.8,
                  'Окружность талии': 65.9, 'Окружность правого плеча': 25.0,
                  'Окружность левого плеча': 24.5, 'Окружность бёдер': 93.0, 'Окружность шеи': 31.0,
                  'Окружность запястья': 15.0, 'Жизненная ёмкость лёгких': 3.0, 'Динамометрия правой кисти': 26.0,
                  'Динамометрия левой кисти': 24.0, 'Сист. артериальное давление': 116,
                  'Диаст. артериальное давление': 67, 'Частота сердечных сокращений': 86,
                  'Толщина жировой складки (живот)': 1.7,
                  'Толщина жировой складки (плечо)': 1.3,
                  'Толщина жировой складки (спина)': 1.3},
                 {'Длина тела': 168.3, 'Масса тела': 61.5, 'Индекс Кетле': 22.3, 'Окружность грудной клетки': 84.8,
                  'Окружность талии': 70.6, 'Окружность правого плеча': 27.0,
                  'Окружность левого плеча': 27.0, 'Окружность бёдер': 98.0, 'Окружность шеи': 32.0,
                  'Окружность запястья': 15.5, 'Жизненная ёмкость лёгких': 3.6, 'Динамометрия правой кисти': 29.0,
                  'Динамометрия левой кисти': 27.0, 'Сист. артериальное давление': 122,
                  'Диаст. артериальное давление': 71.0, 'Частота сердечных сокращений': 99,
                  'Толщина жировой складки (живот)': 2.4,
                  'Толщина жировой складки (плечо)': 1.6,
                  'Толщина жировой складки (спина)': 1.7},
                 {'Длина тела': 173.3, 'Масса тела': 67.9, 'Индекс Кетле': 23.6, 'Окружность грудной клетки': 88.4,
                  'Окружность талии': 74.8, 'Окружность правого плеча': 29.0,
                  'Окружность левого плеча': 29.0, 'Окружность бёдер': 102.0, 'Окружность шеи': 33.5,
                  'Окружность запястья': 16.0, 'Жизненная ёмкость лёгких': 3.9, 'Динамометрия правой кисти': 31.0,
                  'Динамометрия левой кисти': 30.0, 'Сист. артериальное давление': 128,
                  'Диаст. артериальное давление': 78, 'Частота сердечных сокращений': 110,
                  'Толщина жировой складки (живот)': 3.0,
                  'Толщина жировой складки (плечо)': 1.7,
                  'Толщина жировой складки (спина)': 1.9},
                 {'Длина тела': 177.4, 'Масса тела': 78.9, 'Индекс Кетле': 27.5, 'Окружность грудной клетки': 94.7,
                  'Окружность талии': 84.0, 'Окружность правого плеча': 36.0,
                  'Окружность левого плеча': 36.0, 'Окружность бёдер': 109.5, 'Окружность шеи': 36.0,
                  'Окружность запястья': 17.5, 'Жизненная ёмкость лёгких': 4.4, 'Динамометрия правой кисти': 34.0,
                  'Динамометрия левой кисти': 33.0, 'Сист. артериальное давление': 132,
                  'Диаст. артериальное давление': 82, 'Частота сердечных сокращений': 122,
                  'Толщина жировой складки (живот)': 3.7,
                  'Толщина жировой складки (плечо)': 2.1,
                  'Толщина жировой складки (спина)': 2.7}])



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
