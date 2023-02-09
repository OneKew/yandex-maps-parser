def into_json(org_id, name, address, website, phone, social):
    """ Шаблон файла OUTPUT.json"""



    # Проверка opening_hours на отсутствие одного их рабочих дней
    # Создается отдельный список (opening_hours_new) с полученными значениями
    # Далее он проверяется на отсутствие того или иного рабочего дня
    # На индекс отсутствующего элемента вставляется значение  "   выходной"


    data_grabbed = {
        "ID": org_id,
        "name": name,
        "address": address,
        "website": website,
        "phone": phone,
        "social": social,

    }
    return data_grabbed