# Модуль осуществляет управление логикой программы

import ui
import methods
#import json 
import time


name_file = "our_bd.json"

# def convert(stroka: str) -> dict:
#     res_dict=json.loads(stroka) 
#     return res_dict

def labor(do_it: int, list_rezult):
    if do_it == 1:
                # редактирование
        list_dick = ui.input_data_for_change(list_rezult) # метод отредактирует найденное m_search
        our_bd = methods.m_edit(name_file, list_dick)
        ui.print_ui(our_bd)
        time.sleep(3)
        return

    if do_it == 2:
                # импорт
        format_file = ui.format_operation()
        if format_file == 1:
            res = methods.export_txt()
            ui.result_operation(res)
        elif format_file == 2:
            res = methods.export_csv()
            ui.result_operation(res)
        elif format_file == 3:
            res = methods.export_json()
            ui.result_operation(res)
            time.sleep(3)
            return

    if do_it == 3:
                # удаление
        our_bd = methods.m_delete(name_file, list_rezult)
        ui.print_ui(our_bd)
        time.sleep(3)
        return

                # выход в основное меню
    if do_it == 4:
        return

def action(name_file, inp_user, user_inf = ""):
    if 1 == inp_user:    # это поиск
        # m_search вернет список словарей - в list#
        # leng-Количество найденных id
        list_rez = methods.m_search(name_file, user_inf) 
        leng = len(list_rez)
        if leng == 1:
            ui.print_ui(list_rez)   # распечатает в консоль найденное
            do_it = ui.ui_podmenu() # метод должен спросить за 1, 2, 3, 4 пункты и вернуть ответ в int
            labor(do_it, list_rez)
            return
    else:
            # метод должен спросить какой id из выведенных в консоль пользователь выбирает и возвращает его, - в list
        list_id = ui.make_lst_id()   
        do_it = ui.ui_podmenu()
        labor(do_it, list_id)
        return
  
    if 2 == inp_user:  #  добавление
        # метод должен выдать последовательно имена полей, а пользователь набирает что ему нужно. Пример: Surname: Бобкин
        # Name: Алексей и т.д.. Все долно сохраняться в список словарей. Метод возвращает список словарей
        our_bd = methods.m_adding(name_file, user_inf)
        ui.print_ui(our_bd)
        time.sleep(3)
        return

    if 3 == inp_user:  #  экспорт
        format_file = ui.format_operation()
        if format_file == 1:
            res = methods.export_txt()
            ui.result_operation(res)
            time.sleep(3)
            return
        elif format_file == 2:
            res = methods.export_csv()
            ui.result_operation(res)
            time.sleep(3)
            return
        elif format_file == 3:
            res = methods.export_json()
            ui.result_operation(res)
            time.sleep(3)
            return

    if 4 == inp_user:   #  импорт
        format_file = ui.format_operation()
        if format_file == 1:
            res = methods.import_txt()
            ui.result_operation(res)
            time.sleep(3)
            return
        elif format_file == 2:
            res = methods.import_csv()
            ui.result_operation(res)
            time.sleep(3)
            return
        elif format_file == 3:
            res = methods.import_json()
            ui.result_operation(res)
            time.sleep(3)
            return



ui.hello_user()

while True:
    inp_user = ui.ui_menu()
    if inp_user == 3 or inp_user == 4:
        action(name_file, inp_user)
    elif inp_user == 1:
        user_infor = ui.ui_input_new_data
        action(name_file, inp_user, user_infor)
        continue
    elif inp_user == 2:
        new_user_data = ui.make_lst_of_dict_for_add()
        action(name_file, inp_user, new_user_data)
        continue
    elif inp_user == 5:
        ui.print_ui("До свидания!")
        break