class Contact:

    def __init__(self, name, surname, number, favorite_contact=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.favorite_contact = favorite_contact
        self.args = args
        self.kwargs = kwargs
        for passion in self.args:
            print('-', passion)

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n' \
               f'Номер телефона: {self.number}\n' \
               f'В Избранных: {self.favorite_contact}\n' \
               f'Дополнительная информация: \n\t{self.kwargs}'


jhon = Contact('Jhon', 'Smith', '+71234567809',
               telegram='@jhony', email='jhony@smith.com')
Heisenberg = Contact('Walter', 'White', '+15467770102',
                telegram='@heisenberg', email='walter@white.com')               
print(jhon)

class Phonebook:

    def __init__(self, book_name):
        self.contact_list = []
        self.book_name = book_name

    def add_contact(self, contact_inatance):
        self.contact_list.append(contact_inatance)

    def print_contacts(self):
        for contact in self.contact_list:
            print(contact)

    def find_contact(self):
        name_2 = input('Введите имя: ')
        family_2 = input('Введите фамилию: ')
        for contact in self.contact_list:
            if contact.name == name_2:
                if contact.surname == family_2:
                    print(contact)
                else:
                    print('Контакт не найден')
                    break
    
    def remove_contacts(self):
        rem_contact_number = input('Введите номер контакта для удаления: ')
        for contact in self.contact_list:
            if contact.number == rem_contact_number:
                self.contact_list.remove(contact)
                print(f'Контакст {contact.name} удален')

    def find_priority_numbers(self):
        for contact in self.contact_list:
            if contact.favorite_contact != False:
                print(f'{contact.name}\nИзбранные номера: {contact.favorite_contact}')

MyBook = Phonebook('MyBook')
MyBook.add_contact(jhon)
MyBook.add_contact(Heisenberg)


def main():
    while True:
        print(f'Спмсок доступных функций:\n'
              f'1 - Вывод всех контактов \n'
              f'2 - Поиск контакта по имени и фамилии\n'
              f'3 - Вывод всех избрвнных номеров\n'
              f'4 - Удаление контакта\n'
              f'5 - Выход')
        user_input = input('Введите команду: ')
        if user_input == '1':
            MyBook.print_contacts()
            print(input())
        elif user_input == '2':
            MyBook.find_contact()
            print(input())
        elif user_input == '3':
            MyBook.find_priority_numbers()
            print(input())
        elif user_input == '4':
            MyBook.remove_contacts()
            print(input())
        elif user_input == '5':
            break


if __name__ == '__main__':
    main()

    


