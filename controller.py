# Модуль осуществляет управление логикой программы

import ui
import check
import methods

inp_user = ui.ui_menu()
# Тут мне не понятно как будет работать ui_menu, пусть он проверяет введеную цифру и возвращает ее в int

def # get, set, action   -get получить выбор пользователя, и данные
                        # set - отправляет данные 
                        # action - вся работа
                        # convert - конвертирует строку в словарь(питон, dict)
if "1" == inp_user:
    ui.ui_print()
    leng = methods.m_search("Введите, что хотите найти: ") # метод должен вернуть количество вернувшейся информации(одна строка или больше)
    if leng == 1:
        inp_user2 = ui.ui_menu("Что будете делать с найденой информацией? Можно удалить: для этого введите 1, или редактировать: 2")
    else:
        inp_user2 = ui.ui_menu("Введите индекс строки, с которой хотите работать: ")

if "2" == inp_user:
    methods.m_adding("Введите, что хотите найти: ")


# if "3" == inp_user:
#     methods.?("Введите, что хотите найти: ")

# if "4" == inp_user:
#     methods.?("Введите, что хотите найти: ")

# if "5" == inp_user:
#     methods.?("Введите, что хотите найти: ")