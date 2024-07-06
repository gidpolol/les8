def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('Handbook.txt')
    while (choice!=7):
        if choice==1:
            print_handbook(phone_book)
        elif choice==2:
            lastname=input('Фамилия: ')
            print(*find_by_lastname(phone_book,lastname))
        elif choice==3:
            number=input('Телефон: ')
            print(*find_by_number(phone_book,number))	
        elif choice==4:
            lastname=input('Фамилия: ')
            name=input('Имя: ')
            number=input('Телефон: ')
            user_data=input('Описание: ')
            add_new_user(lastname,name,number,user_data)
        elif choice==5:
            lastname=input('Укажите фамилию человека, у которого нужно изменить описание: ')
            user_data=input('Описание: ')
            сhange_data(phone_book,lastname,user_data)
        elif choice==6:
            filename = input("Укажите название текстового файла, в который нужно перенести данные из основного словаря: ")
            transfer_of_data(filename,phone_book)
        choice=show_menu()
        
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
		  "5. Изменить данные\n"
          "6. Перенести данные из одного справочника в другой\n"
          "7. Закончить работу\n")
    choice = int(input())
    return choice

# 1. Отобразить весь справочник
def print_handbook(phone_book):
    for i in range(len(phone_book)):
        print(phone_book[i]['Фамилия'],phone_book[i]['Имя'],phone_book[i]['Телефон'],phone_book[i]['Описание'])
        i+=1

# 2. Найти абонента по фамилии       
def find_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == lastname:
            return (phone_book[i]['Фамилия'],phone_book[i]['Имя'],phone_book[i]['Телефон'],phone_book[i]['Описание'])
        
# 3. Найти абонента по номеру
def find_by_number(phone_book,number):
    for i in range(len(phone_book)):
        if phone_book[i]['Телефон'] == number:
            return (phone_book[i]['Фамилия'],phone_book[i]['Имя'],phone_book[i]['Телефон'],phone_book[i]['Описание'])
        
# 4. Добавить абонента в справочник

def add_new_user(lastname,name,number,user_data):
    with open("Handbook.txt", "a", encoding="utf-8") as handbook:
        data = ['\n',lastname,',',name,',',number,',',user_data]
        handbook.writelines(data)
        
# 5. Изменить данные

def сhange_data(phone_book,lastname,user_data):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == lastname:
            phone_book[i]['Описание'] = user_data + "\n"
            write_txt("Handbook.txt",phone_book)

# 6. Перенести данные из одного справочника в другой

def transfer_of_data(filename,phone_book):
    write_txt(filename, phone_book)

# Чтение файла 
def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            #dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            phone_book.append(record)	
    return phone_book

# Запись в файл
def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')
            
work_with_phonebook()