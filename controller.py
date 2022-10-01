# Модуль осуществляет управление логикой программы

import ui
import methods
import json 


name_file = "our_bd.json"

def convert(stroka: str) -> dict:
    res_dict=json.loads(stroka) 
    return res_dict



def action(name_file, inp_user, user_inf):
    if "1" == inp_user:
        # метод должен вывести в консоль список словарей, вернуть список id - в list#
        # leng-Количество найденных id
        list_rez = methods.m_search(name_file, user_inf) 
        leng = len(list_rez)
        if leng == 1:
            do_it = ui.ui_podmenu() # метод должен спросить за 6, 7 и 5 пункты и вернуть ответ в int
            if do_it == 6:
                # .m_edit должен быть больше похож на .m_write(), а то вопрос-как происходит редактирование?

                list_dick = ui.ui_input_data_for_chanje()
                methods.m_edit(name_file, list_dick)
            if do_it == 7:
                methods.m_delete(name_file, list_id)
        else:
            # метод должен спросить какой id из выведенных в консоль пользователь выбирает и возвращает его, - в list
            list_id = ui.ui_menu_quest_id()   
            do_it = ui.ui_podmenu()
            if do_it == 6:
                methods.m_edit(name_file, list_id)
            if do_it == 7:
                methods.m_delete(name_file, list_id)

    if "2" == inp_user:
        # метод должен выдать последовательно имена полей, а пользователь набирает что ему нужно. Пример: Surname: Бобкин
        # Name: Алексей и т.д.. Все долно сохраняться в список словарей. Метод возвращает список словарей
        list_dtct = ui.ui_input_new_data()
        methods.m_adding(name_file, list_dtct)
    # if "3" == inp_user:
    #     methods.?()

    # if "4" == inp_user:
    #     methods.?()

    # if "5" == inp_user:
    #     methods.?()


# get, set, action   -get получить выбор пользователя, и данные
# set - отправляет данные 
# action - вся работа
# convert - конвертирует строку в словарь(питон, dict)

ui.ui_menu()