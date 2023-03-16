''''
Курсовая работа студентки Февралевой  А.А.
Дисциплина- Программирование
Задание-получение списка фильмов выпущенных в определенном году
Сортировка списка по году выпуска фильма
Исходные данные в файл- films.txt
имя фала (программы)- 21-ZIE Fevraleva_course_work.py
'''
''''
Функция запроса даты выхода фильма
'''
global realease_date,s_realease_date,year_films
def get_date():
    global realease_date, s_realease_date
    realease_date=int(input("Введите год выпуска фильмов:"))
    s_realease_date=str(realease_date)

    
'''
Функция формирования списка фильмов нужного года
'''

def  search(realease_date):
    global year_films
    year_films=[]
    films=open('films.txt','r',encoding='utf-8')
    #print(films)
    for s in films:
        cl=s.split(';')
       # print(cl)
        if s_realease_date==cl[0]:
            year_films.append(s)
    films.close()
    return year_films

'''
Функция  сортировки в алфавитном порядке
'''

def  mysort(year_films):
    year_films.sort()
    return year_films


'''
Функция вывода результатоов
'''

def print_results(realease_date,year_films):
    print("Количество фильмов ,выпущенных в ",realease_date,"году: ",len(year_films))
    print("Список фильмов,выпущенных в ",realease_date,'году:')
    print("__________________________________________________________________________________________")
    print("{:5}\t{:10}\t{:25}\t{:15}\t{:10}".format("№", "год", " название", "жанр","длительность"))
    print("__________________________________________________________________________________________")
    num = 1


    for i in year_films:
        f = i.split(";")
        # = f[3].replace("\n", '')
        print("{:5}\t{:10}\t{:25}\t{:15}\t{:10}".format(str(num), f[0], f[1],f [2],f[3]))
        num+= 1

    print("___________________________________________________________________________________________")


'''
основная программа

'''
'''
Проверка ввода строки перехватом исключений при помощи конструкции 
                    try...except    
'''

try:
    
    date=get_date( )
    year_films=search(realease_date)
    '''
    Проверяем наличие даных в файле
    '''
    if len(year_films) == 0:
        print("Нет информации о фильмах,выпущенных в ", realease_date, "году")
    else:
        if len(year_films) > 1:
            year_films = mysort(year_films)
            ''''Вызов функции вывода результатов'''
            print_results(realease_date, year_films)
#Перехват ошибки ValueError, т.е. ввода строки вместо числа

except ValueError:
    print("Вы ввели не год")


