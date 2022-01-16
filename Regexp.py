import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
for contact in range(1, len(contacts_list)):
    i = contacts_list[contact]
    name_pattern = r"'(\w*[А-Яа-я]+)'?,?\s?'?([А-Я][а-я]+)'?,?\s?'?(\w+)?'"
    name = re.findall(name_pattern, str(i))
    phone_pattern = r"(\+7|8)\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d+)(\s\(?(доб.)\s?(\d+)\)?)?"

    i[0] = name[0][0]
    i[1] = name[0][1]
    i[2] = name[0][2]
    i[5] = re.sub(phone_pattern, r"+7(\2)\3\4\5 \7\8", i[5])

    if len(i) > 7:
        del i[7:]

correct_contacts = [contacts_list[0]]
for i in contacts_list:
    l_name = i[0]
    f_name = i[1]
    for j in range(1, len(contacts_list)):
        c2 = contacts_list[j]
        if l_name == c2[0] and f_name == c2[1]:
            if i[2] == '':
                i[2] = c2[2]
            if i[3] == '':
                i[3] = c2[3]
            if i[4] == '':
                i[4] = c2[4]
            if i[5] == '':
                i[5] = c2[5]
            if i[6] == '':
                i[6] = c2[6]
    if i not in correct_contacts:
        correct_contacts.append(i)

# print(correct_contacts)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(correct_contacts)
    print('Данные обработаны')