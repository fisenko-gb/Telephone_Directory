вот такой поиск мне кажется лучше

# def return_dict(id, surname, name, fathername, telefon, comment):
#     mydict = {
#         'id': id,
#         'surname': surname,
#         'name': name,
#         'fathername': fathername,
#         'telefon': telefon,
#         'comment': comment
#     }
#     return mydict


# def test(str_searh:str):
#     bd_list = []
#     bd_list.append(return_dict(1, 'Иванов', 'Иван',
#                                'Иванович', 89270010101, 'телефон Иванов'))
#     bd_list.append(return_dict(2, 'Петров', 'Петр',
#                                'Петрович', 89270020202, 'телефон Петрова'))
#     bd_list.append(return_dict(3, 'Степанов', 'Степан',
#                                'Степанович', 89270030303, 'телефон Степанова'))
#     bd_list.append(return_dict(4, 'Сидоров', 'Иван',
#                                'Петрович', 89270040404, 'телефон Сидорова'))
#     for i in bd_list:
#         for k in i.values():
#             if str_searh.upper() in (str(k)).upper():
#                 print(*i.values())
#                 break

# test('иВа')

# ну т.е. сама функция поиска вот ищет что угодно во всех полях):
# for i in bd_list:
#         for k in i.values():
#             if str_searh.upper() in (str(k)).upper():
#                 print(*i.values())
#                 break
