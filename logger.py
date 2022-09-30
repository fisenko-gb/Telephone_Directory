# Модуль осуществляет логирование всех действий в программе
from datetime import datetime as dt
from time import time

def m_delete_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('index.html', 'a') as file:
        file.write('{};delete;{}\n'
                    .format(time, data))

def m_adding_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('index.html', 'a') as file:
        file.write('{};add;{}\n'
                    .format(time, data))

def m_edit_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('index.html', 'a') as file:
        file.write('{};edit;{}\n'
                    .format(time, data))


def m_search_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('index.html', 'a') as file:
        file.write('{};search;{}\n'
                    .format(time, data))
