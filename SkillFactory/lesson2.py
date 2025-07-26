contacts = {}
for i in range(3):
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
print(contacts.keys())

print(contacts.values())

print()
for name, phone in contacts.items():
    print(f'Контакт: {name} Телефон: {phone}')

print('Добавляем новые записи в словарь:')
for i in range(2):
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
    print('Запись добавлена в словарь')

print('Редактируем запись в словарь:')
print(contacts)
name = input('Введите имя из словаря: ')
phone = input('Введите новый номер телефона: ')
contacts[name] = phone
print('Запись отредактирована')

print('Проверяем наличие записи в словарь:')
name = input('Введите имя: ')
if name in contacts.keys():
    del contacts[name]
    print('Запись удалена')
else:
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
    print('Запись добавлена в словарь')

print(contacts)