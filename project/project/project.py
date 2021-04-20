from datetime import timedelta, date
import fileinput
from prettytable import PrettyTable
import os
import pyttsx3
import re
import sys





class AdressBook:
    
    def __init__(self):

        self.name = ''
        self.number_phone = ''
        self.email = ''
        self.birthday = ''
        self.notes = ''
        self.engine = pyttsx3.init()
        self.engine.say('Приветствую, я твой персональный ассистент Лара, введите  хелп что бы усзнать мои возможности')
        self.engine.runAndWait()
        print('Greetings, I am your personal assistant Lara. Enter \'help\' and you will see my possibilities')
    
    
    def empty_file(func):
        def inner(path):
            try:
                if os.path.isfile('Book_folder//AdressBookNew.txt') and os.path.getsize('Book_folder//AdressBookNew.txt') > 0:
                    return func('Book_folder//AdressBookNew.txt')

            except:
                print('Адресная книга пуста, для начала добавьте контакты')
            else:
                print('Адресная книга пуста, для начала добавьте контакты')

        return inner


    def input_name(self):

        self.engine = pyttsx3.init()
        self.engine.say('Введите имя')
        self.engine.runAndWait()
        self.name = input('Please enter name: ')
        return self.name

    def input_number_phone(self):

        self.engine = pyttsx3.init()
        self.engine.say('Введите номер')
        self.engine.runAndWait()
        while True:
            try:
                self.number_phone = input('Please enter number: ')
                if self.number_phone == (re.search(r'\+?\d?\d?\d?\d{2}\d{7}', self.number_phone)).group():
                    break
            except AttributeError:
                print('Повторите ввод номера!')
        return self.number_phone

                
    def input_email(self):

        self.engine = pyttsx3.init()
        self.engine.say('Введите адресс электронной почты')
        self.engine.runAndWait()
        while True:
            try:
                self.email = input('Please enter email: ')
                if self.email == (re.search(r'[a-zA-Z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}', self.email)).group():
                    break
            except AttributeError:
                print('Повторите ввод мыла!')
        return self.email

    def input_birthday(self):

        self.engine = pyttsx3.init()
        self.engine.say('Введите день рождения')
        self.engine.runAndWait()
        self.birthday = input('Please enter birthday: ')
        return self.birthday

    def create_notes(self):

        self.engine = pyttsx3.init()
        self.engine.say('Введите заметку')
        self.engine.runAndWait()
        self.notes = input('Please enter notes: ')
        return self.notes

    def c_ontakt(self):
        c_ontakt = user.input_name() + ',    ' + user.input_number_phone() + ', ' +  user.input_email() + ', '\
                +  user.input_birthday() + ', ' + user.create_notes() + ', '+'\n'
        return c_ontakt
    
    def create(self):

        with open('Book_folder//AdressBookNew.txt', 'a') as file:
            file.write(str(user.c_ontakt()))
            

    def command(self):

        self.engine = pyttsx3.init()
        self.engine.say('Пожалуйста введите команду: ')
        self.engine.runAndWait()

        select = input('Plaese enter command: ')

        if select == 'add':
            user.create()
        elif select == 'search':
            user.search() 
        elif select == 'delete':
            user.delete()
        elif select == 'edit':
            user.edit()
        elif select == 'show all':
            user.show_all()
        elif select == 'birthday':
            user.congratulate()
        elif select == 'note':
            user.upgrade_notes()
        elif select == 'help':
            user.help()
        elif select == 'exit':
            user.exit()    

    
                    
        
    def help(self):

        self.engine = pyttsx3.init()
        self.engine.say('Вы выбрали хелп, ознакомтесь с возможностями')
        self.engine.runAndWait()
        print('______________________________________')
        print('Created contact:        add')
        print('Search for a contact:   search ')
        print('Deleting a сontact:     delete ')
        print('Editing a contact:      edit')
        print('Show address book:      show all ')
        print('Birthday:               birthday') 
        print('upgrade_notes:          note')
        print('Exit Assistant:         exit') 
        print('______________________________________')                       

    def search(self):
        
        self.engine = pyttsx3.init()
        self.engine.say('Вы выбрали поиск:')
        self.engine.say('Введите искомый контакт:')
        self.engine.runAndWait()
        position_name = input('Please enter search name: ')  
        td = []
        with open('Book_folder//AdressBookNew.txt', 'r') as file:
            n = 0
            for string in file:
                if string.find(position_name.lower()) != -1 or string.find(position_name.title()) != -1:
                    n += 1
                    k = string.rstrip('\n').split()
                    for el in k:
                        p = el.rstrip(',')
                        td.append(p)
            print(user.func_input(td))
            self.engine = pyttsx3.init()
            self.engine.say('Количество найденных контактов:' + str(n))
            self.engine.runAndWait()
            if n == 0:
                
                self.engine = pyttsx3.init()
                self.engine.say('Контакта не существует в адресной книге')
                self.engine.runAndWait()    
                       
    
    def delete(self):
        
        self.engine = pyttsx3.init()
        self.engine.say('Вы выбрали удаление, напишите имя контакта который нужно удалить')
        self.engine.runAndWait()
        delete_contaсt = input('Please enter delete name: ')
        for string in fileinput.input('Book_folder//AdressBookNew.txt', inplace=True):
            if delete_contaсt in string:
                continue
            print(string.rstrip('\n'))
        self.engine = pyttsx3.init()
        self.engine.say('Контакт был удален')
        self.engine.runAndWait() 


    def q_1(self, z):
        f = z.split(', ')
        f.pop(1)
        f.insert(1, (user.input_number_phone()))
        a = ', '.join(f)
        return a

    def q_2(self, z):
        f = z.split(', ')
        f.pop(2)
        f.insert(2, (user.input_email()))
        a = ', '.join(f) 
        return a

    def q_3(self, z):
        f = z.split(', ')
        f.pop(3)
        f.insert(3, (user.input_birthday()))
        a = ', '.join(f)
        return a

    def q_4(self, z):
        f = z.split(', ')
        f.pop(4)
        f.insert(4, (user.create_notes()))
        a = ', '.join(f) 
        return a

    def edit_1(self, z):

        self.engine = pyttsx3.init()
        self.engine.say('Вы выбрали редактирование:')
        self.engine.say('Введите Выберите элемент для редактирования:')
        self.engine.runAndWait()
        print('''1. Number phone
2. Email
3. Birthday
4. Заметки''')

        d = input('What do you want to change: ')
        number = {
            '1': user.q_1,
            '2': user.q_2,
            '3': user.q_3,
            '4': user.q_4
            }
        return number[d](z)

    @empty_file
    def edit(self):
        edit_contaсt = user.input_name()
        with open('Book_folder//AdressBookNew.txt', "r") as file:
            lines = file.readlines()
        with open('Book_folder//AdressBookNew.txt', "w") as file:
            n = 0
            for line in lines:
                if edit_contaсt in line:
                    n +=1
                    lines[lines.index(line)] = (user.edit_1(lines[lines.index(line)]))
            if n == 0:
                self.engine = pyttsx3.init()
                self.engine.say('Данного контакта нет в адресной книге')
                self.engine.runAndWait()
 
            file.writelines(lines)     

    def show_all(self):

        self.engine = pyttsx3.init()
        self.engine.say('Перед Вами книга контактов')
        self.engine.runAndWait()
        td = []
        with open('Book_folder//AdressBookNew.txt', "r") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                k = line.rstrip('\n').split()
                for el in k:
                    z = el.rstrip(',')
                    td.append(z)
        print(user.func_input(td))
    
    def congratulate(self):

        self.engine = pyttsx3.init()
        self.engine.say('Введите количество дней, а я Вам подскажу у кого из Ваших контактов день рождение')
        self.engine.runAndWait()
        td = []
        a = int(input('Please enter count day: '))
        today = date.today()
        z = today + timedelta(days=a)
        with open('Book_folder//AdressBookNew.txt', 'r') as file:
            n = 0
            for line in file:
                if line.find(r"{}.0{}".format(z.day, z.month)) != -1 or line.find(r"{}.{}".format(z.day, z.month)) != -1:
                    n += 1
                    k = line.rstrip('\n').split()
                    for el in k:
                        p = el.rstrip(',')
                        td.append(p)
            print(user.func_input(td))
            self.engine = pyttsx3.init()
            self.engine.say(str(n) + 'Ровно столько именинников в этот день')
            self.engine.runAndWait()
            if n == 0:
                self.engine = pyttsx3.init()
                self.engine.say('В этот день нету дней рождения')
                self.engine.runAndWait()

    @empty_file
    def upgrade_notes(self):
        edit_contaсt = user.input_name()
        with open('Book_folder//AdressBookNew.txt', "r") as file:
            lines = file.readlines()
        with open('Book_folder//AdressBookNew.txt', "w") as file:
            for line in lines:
                if edit_contaсt in line:
                    lines[lines.index(line)] = (user.q_4(lines[lines.index(line)]))
            file.writelines(lines)


    def func_input(self,td):
        th = ['Name', 'Number phone', 'Email', 'Date of Birth', 'Note']

        columns = len(th)
        table = PrettyTable(th)


        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        return table        

           

    def exit(self):

        self.engine = pyttsx3.init()
        self.engine.say('Досвидание, была рада помочь')
        self.engine.runAndWait()
        print("Good bye!")
        sys.exit(0)                
        


                          
                
user = AdressBook()


def main():
    

    while True:
        try:
            os.mkdir('Book_folder')
        except FileExistsError:
            pass
        user.command()

    

    

    

if __name__ == '__main__':
    main()