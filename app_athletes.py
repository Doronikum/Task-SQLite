# Импортируем библиотеку sqlite3 для работы с базами данных SQLite.
import sqlite3
# Устанавливаем соединение с базой данных "athletes.db". БД и программа должны находится в одной папке
con = sqlite3.connect("athletes.db")
# Создаем курсор для выполнения запросов к базе данных.
cur = con.cursor()
#------------------------------------------
#Очистка и заполнение БД
#Первоначальное заполнение БД
def athletes_install(data_menu):
    name = ('Рылов','Исинбаева','Лысенко','Стяжкин','Валуев','Ильченко','Поветкин','Тайсон')
    gender = ('муж','жен','муж','муж','муж','жен','муж','муж')
    adge = ('28','42','27','22','51','36','45','51')
    country = ('РФ','РФ','РФ','РФ','РФ','РФ','РФ','США',)
    sport = ('плавание','прыжки с шестом','прыжки в высоту','подводное плавание','бокс','плавание','бокс','бокс')
    action = (1,0,1,1,0,1,1,0)

    # Формирование кортежа с данными о фильме
    cur.execute('DELETE FROM athletes')
    for i in range(len(name)):
        athletes_add=[] 
        athletes_add.append(i+1)
        athletes_add.append(name[i])
        athletes_add.append(gender[i])
        athletes_add.append(adge[i])
        athletes_add.append(country[i])
        athletes_add.append(sport[i])
        athletes_add.append(action[i])
        print(athletes_add)
        # Выполнение SQL запроса для добавления фильма в базу данных
        cur.execute('INSERT INTO athletes (Id, name, gender, adge, country,sport,action) VALUES (?, ?, ?, ?, ?,?,?)', tuple(athletes_add))
    # Сохранение изменений в базе данных
    con.commit()
    print("Начальная БД загружена")
    text=input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход')
    data_menu = int(text)
    return (data_menu)
#-----------------------------------
#Вывод БД
def athletes_all(data_menu):
    res=cur.execute('SELECT * FROM athletes')
    result = res.fetchall()
    print('Общий список спортсменов')
    i=1
    for data in result:
        print(f'{i}. Фамилия {data[1]}, пол {data[2]}, возраст {data[3]} лет, страна {data[4]}, вид спорта {data[5]}, активность {data[6]}')
        i+=1

    print('Конец списка спортсменов в БД')
    text=input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход')
    data_menu = int(text)
    return (data_menu)

#----------------------------------------------------------------------------------------------------------------------------------------
#Поиск в БД
def athletes_name(data_menu):
    name=input("Введите фамилие спортсмена")
      
    res=cur.execute('SELECT * from athletes WHERE NAME == ?', (name,))
    result = res.fetchall()
    print('Данные выбранного спортсмена')
    for data in result:
        print(f'Фамилия {data[1]}, пол - {data[2]}, возраст - {data[3]} лет, страна - {data[4]}, вид спорта - {data[5]}, активность {data[6]}')
    print('Конец данных в БД')
    text=input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход')
    data_menu = int(text)
    return (data_menu)
#-----------------------------------------------------------------------------------------------------------------------------------------
#Добавление в БД
def athletes_add(data_menu):
    print('Внесение в БД банных нового спортсмена')
    athletes_add=[] 
    #athletes_add.append(i)
    athletes_add.append(input('Введите имя'))
    athletes_add.append(input('Введите пол (муж/жен)'))
    athletes_add.append(input('Введите возраст'))
    athletes_add.append(input('Введите страну'))
    athletes_add.append(input('Введите вид спорта'))
    athletes_add.append(input('Введите активность'))
    print(athletes_add)
    # Выполнение SQL запроса для добавления фильма в базу данных
    cur.execute('INSERT INTO athletes (name, gender, adge, country,sport,action) VALUES (?, ?, ?, ?, ?, ?)', tuple(athletes_add))
    # Сохранение изменений в базе данных
    con.commit()
    print('Спортсмен сохранен в БД')
    text=input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход')
    data_menu = int(text)
    return (data_menu)
#-----------------------------------
#1.Подсчет общего числа пользователей
#2.Запрос на изменение их активности
#  Запрос на фильтрацию по активности
#  Запрос на удаление неактивных

def athletes_activ(data_menu):
    menu_5=int(input('Введите действия: 6 - изменить активности спортсменов, 7 - фильтр по активности, 8 - удалить не активных, 0 - выход'))
    #data_menu = int(input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход'))

    while menu_5!=0:
        #Изменение активности спортсменов
        if menu_5 == 6:
            # 1. Подсчет общего числа пользователей
            res=cur.execute('SELECT name FROM athletes')
            result = res.fetchall()
            name_athl=result 
            col_athl=len(result)
            num_id=result 
            #print(f'result{result}, name_athl {name_athl}, col_athl {col_athl}')
            # 2. изменение БД, фильтрации и удаление неактивных
            print(f'Введите активности {col_athl} спортсменов - 1 или 0')
            aktiv_new=[]
            for i in range(col_athl):
                aktiv_new.append(input(f'Спортсмен {i+1}. {name_athl[i][0]}- 1 или 0: '))
                c=aktiv_new[i]
                cur.execute('UPDATE athletes SET action = ? WHERE name = ?', (c, name_athl[i][0]))
                con.commit()
            print(f'Изменения внесены: {aktiv_new}')

        #фильтр активных спортсменов
        elif menu_5 == 7:
            res=cur.execute('SELECT * FROM athletes WHERE ACTION != 0')
            result = res.fetchall()
            print('Вывод активных спортсменов')
            i=1
            for data in result:
                print(f'{i}. Фамилия {data[1]}, пол {data[2]}, возраст {data[3]} лет, страна {data[4]}, вид спорта {data[5]}, активность {data[6]}')
                i+=1
                print('Конец списка активных спортсменов в БД')
        #удаление не активных спортсменов
        elif menu_5 == 8:
            res=cur.execute('DELETE FROM athletes WHERE ACTION ==0')
            result = res.fetchall()
            con.commit()            
            print('Из БД удалены не активные спортсмены')    
        else:
            pass
        menu_5=int(input('Введите действия: 6 - изменить активности спортсменов, 7 - фильтр по активности, 8 - удалить не активных, 0 - выход'))
    text=input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход')
    data_menu = int(text)
    return (data_menu)
    


data_menu = int(input('Введите действие: 1 - Начальная загрузка БД, 2 - Вывод всей БД, 3 - Вывод данных спортсмена, 4 - Добавить спорсмена, 5 - Изменение активност спорсмена, 0 - Выход'))
while data_menu!=0:
    if data_menu == 1:
        data_menu=athletes_install(data_menu)
    elif data_menu == 2:
        data_menu=athletes_all(data_menu)
    elif  data_menu == 3:
        data_menu=athletes_name(data_menu)
    elif  data_menu == 4:
        data_menu=athletes_add(data_menu)
    elif  data_menu == 5:
        data_menu=athletes_activ(data_menu)        
    else:
        print('Завершение программы')
        data_menu=0



