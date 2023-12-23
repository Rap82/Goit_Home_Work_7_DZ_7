# ===================  Home work 7 ========================

# =================== Створення та встановлення власних пакетів ==========================

# Модуль, що містить інструкції по установці, викликає функцію setup з пакету setuptools. 
# Функція setup робить установку пакету в системі і містить параметри, що конфігурують установку.

# Детальні інструкції по написанню setup.py ви можете отримати на сторінці документації.

# Приклад вмісту setup.py:

# from setuptools import setup

# setup(name='useful',
#       version='1',
#       description='Very useful code',
#       url='http://github.com/dummy_user/useful',
#       author='Flying Circus',
#       author_email='flyingcircus@example.com',
#       license='MIT',
#       packages=['useful'])
# В даному прикладі ми викликаємо setup з додатковими інформаційними параметрами, які будуть доступні користувачам. 
# А саме, ми вказали ім'я пакету, версію, короткий опис пакету, адресу, де можна подивитися початковий код, ім'я автора, 
# його email, ліцензію, набір пакетів, які включені у поставку.

# Що якщо наш пакет досить великий і прописувати вручну усі модулі packages незручно і існує ризик помилитися? 
# Тоді у setuptools є функція find_namespace_packages, яка допоможе знайти всі модулі і не пропустити нічого:

# from setuptools import setup, find_namespace_packages

# setup(
#     name='useful',
#     version='1',
#     description='Very useful code',
#     url='http://github.com/dummy_user/useful',
#     author='Flying Circus',
#     author_email='flyingcircus@example.com',
#     license='MIT',
#     packages=find_namespace_packages()
# )
# Такий пакет можна опублікувати на PyPi і тоді його можна буде встановити за допомогою pip, 
# або опублікувати початковий код і тоді можна буде встановити з початкових кодів.

# Щоб встановити цей пакет з початкового коду, виконайте в консолі pip install . або pip install -e . у папці, де лежить setup.py


# ================================ Звдання 1 / Task 1 ======================================

# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict), яка буде викликати функцію setup з параметрами 
# зі словника args_dict.

# Структура словника для параметра args_dicts має бути наступною

# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }

# ++++++++++++++++++++++++++++++++++  Код /Code  +++++++++++++++++++++++++++++++++++++++++++++++++


# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# } # Тестовий словник який має структуру яка відповідає умовам завдання.


# def do_setup ( args_dict ) : # Функція *do_setup ( args_dict )- для виклику функції *setup ( **args_dict )
#                              # Приймає один аргумент  словник  *args_dict - вказаного формату . З параметрами цього словника буде виклки функції setup ( **args_dict )   
    
#     setup ( **args_dict )   # Функція яка приймає як аргументи значення з словника і співставляє їх по порядку з значеннями описаними в самій функції  def setup (...)- дивись опис функції в коді нижче.
#                             # Важливо : щоб в описі функції *def setup(...) , Було стільки аргумантів скільки в словнику ключів *args_dict ,
#                             # *setup ( **args_dict ) - такий запис рівноціний в ручну створеному запису   *setup (name = args_dict['name'] , version=args_dict['version'] , description=args_dict['description'], url=args_dict['url'], author=args_dict['author'], author_email=args_dict['author_email'],license=args_dict['license'] ,packages=args_dict['packages'] )
#                             # де перший аргумент *name переданий у функцію *setup() отримає значення взяте з нашого словника *args_dict за ключем *'name'
#                             # другий аргумент *version переданий у функцію *setup() отримає значення взяте з нашого словника *args_dict за ключем *'version'
#                             # і так далі. Щоб обійти явне задавання аргументів можна зробити запис **імя_зміної- де дві зірочки "**" - це означає всі значення . імя_зміної - це імя змінної що буде містити множину  значень (тип list, dict, set , tuple -та інші )
    
    


# # def setup ( **_ ) :  # Якщо кількість аргументів і їх імена ,які будуть передані ,наперед невідомо можна їх записати у вигляді  (**_ )
# #                      # Де '**'- множина значень .'_' - одинокий символ підкреслення - це в пайтон позначення будь якої зміної імя якої наперед невідомо.

# #     for elemet,value in _.items() :  # Ми можемо також працювати з наперед невизначеним аргументом якщо його тип буде відповідати тому що ми хочемо з ним зробити.
# #                                      # в нашому випадку *setup ( **args_dict ) . **args_dict- це множина типу словник . Тому ми можемо скористатись всіма методами і способами  які достіпні для роботи з словниками
# #                                      # В нашому випадку ми будемо в циклі for проходитись по всіх ключах і значеннях з невідомого наперед словника і принтити ключ і відповідне значення попорядку. 
# #         print (elemet)
# #         print (value)
    
    

# # # def setup (name , version , description , url, author, author_email, license, packages ) : # Функція  з наперед відомими аргументами. і явно оголошеними . Сформована тільки під цей конкретний випадок .
# #                                                                                              # def setup ( **_ ) : - такий запит є універсальний якщо наперед невідомом ні кількість значень ні назву зміної.

# #     #  print (name , version , description , url, author, author_email, license, packages )

    
# # do_setup (args_dict)  # виклик функції *do_setup (args_dict)


# ================================ Звдання 2 / Task 2 ======================================

# Якщо в нашому пакеті є залежності, щоб він запрацював, потрібно встановити додаткові пакети, треба їх всі прописати в параметрі install_requires:

# from setuptools import setup, find_namespace_packages

# setup(
#     name='useful',
#     version='1',
#     description='Very useful code',
#     url='http://github.com/dummy_user/useful',
#     author='Flying Circus',
#     author_email='flyingcircus@example.com',
#     license='MIT',
#     packages=find_namespace_packages(),
#     install_requires=['markdown']
# )
# В цьому прикладі наш пакет буде вимагати встановити спочатку пакет markdown перед встановленням. 
# Порядок встановлення залежностей визначає сам менеджер пакетів (pip наприклад).


# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Модифікуємо приклад попередньої задачі. Для функції do_setup необхідно передбачити другий параметр, який буде списком залежностей.

# Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами зі словника args_dict та параметром install_requires,
# який набуває значення requires.

# Структура словника для параметра args_dicts має бути наступною

# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }

# ++++++++++++++++++++++++++++++++++  Код /Code  +++++++++++++++++++++++++++++++++++++++++++++++++

# from setuptools import setup # для VScode цей імпорт оки непотрібний. Видає зараз помилку мабудь неістальвана ця біліотека наразі в мене.

# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
#             }  # Тестовий словник який має структуру яка відповідає умовам завдання.

# def do_setup ( args_dict, requires ) :  # Функція *do_setup ( args_dict )- для виклику функції *setup ( **args_dict )
#                                     # Приймає Два аргумента, Перший словник *args_dict а інший  - значення *requires які тереба добавити в нашу функцію *septup(**args_dict ) для нового параметру *install_requires
#                                     # Дане питання закриваэмо ти що просто добавляэмо в наш словник *args_dict який передасться в функцію  do_setup(args_dict, requires) новий ключ *install_requires  і його значення *requires
#                                     # Добавляємо новий ключ і значення внаш словник методом *імя_словника.update({'ключ': *значення})

#     args_dict.update ( { 'install_requires': requires } ) # Метод .update({'key': value})- записує в наш словник нову пару ключ : значення в кінець словника.
#                                                           #  args_dict.update({'install_requires': requires}) - в нашому випадку до словника *args_dict в кінці добавить  ключ 'install_requires' з значенням *requires

#     setup ( **args_dict )  # Виклик функції *setup ( **args_dict ) 
   


# def setup ( **_ ) :  # Якщо кількість аргументів і їх імена ,які будуть передані ,наперед невідомо можна їх записати у вигляді  (**_ )
#                      # Де '**'- множина значень .'_' - одинокий символ підкреслення - це в пайтон позначення будь якої зміної імя якої наперед невідомо.

#     for elemet,value in _.items() :  # Ми можемо також працювати з наперед невизначеним аргументом якщо його тип буде відповідати тому що ми хочемо з ним зробити.
#                                      # в нашому випадку *setup ( **args_dict ) . **args_dict- це множина типу словник . Тому ми можемо скористатись всіма методами і способами  які достіпні для роботи з словниками
#                                      # В нашому випадку ми будемо в циклі for проходитись по всіх ключах і значеннях з невідомого наперед словника і принтити ключ і відповідне значення попорядку. 
#         print ( elemet )  # Принтанути поточний ключ з переданого в функцію словника
#         print ( value )   # # Принтанути відповідне  поточне значення з переданого в функцію словника . 
#                             # Принтане всіключі і всі їх значення попорядку . Ключ і відповідне значення бо прінтемо в циклі for де попорядку  перебераємо пари ключ і занчення 

# requires = "fine"  # занчення для перевірки.

# do_setup ( args_dict, requires ) # Виклик функції *do_setup ( args_dict, requires ) 

#  ++++++++++++++++++++++++++++++++++  Код /Code для атопереврки +++++++++++++++++++++++++++++++++++++++++++++++++

# def do_setup ( args_dict, requires ) : 

#     args_dict.update ( { 'install_requires': requires } ) 

#     setup ( **args_dict )



# ================================ Звдання 3 / Task 3 ======================================

# Якщо наш пакет містить додаток, який можна викликати з консолі, зручно буде додати можливість виклику цього застосування 
# у будь-якому місці нашої системи з консолі. Для цього у виклику setup додамо ще один параметр — entry_points. 
# Цей параметр приймає словник, де ми можемо вказати список "точок входу" для ключа console_scripts.

# Наприклад, в нашому пакеті у модулі some_code.py є функція hello_world, яка виводить у консоль повідомлення Hello World!. 
# Після встановлення пакету ми зможемо у будь-якому місці нашої системи виконати в консолі команду: helloworld і отримаємо у відповідь Hello World!.

# Щоб це працювало в системі Python повинен викликатися при виклику файлів з розширенням .py та setup.py має бути змінений:

# from setuptools import setup, find_namespace_packages

# setup(
#     name='useful',
#     version='1',
#     description='Very useful code',
#     url='http://github.com/dummy_user/useful',
#     author='Flying Circus',
#     author_email='flyingcircus@example.com',
#     license='MIT',
#     packages=find_namespace_packages(),
#     install_requires=['markdown'],
#     entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
# )
# У списку точок входу console_scripts можуть бути виконувані файли (.exe), скрипти Bash, cmd, PowerShell і будь-який інший файл,
# який операційна система зможе виконати.


# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Продовжуємо модифікувати приклад. Для функції do_setup необхідно передбачити третій параметр, який буде словником, 
# де ми можемо вказати список "точок входу" для ключа console_scripts.

# Функція do_setup(args_dict, requires, entry_points) повинна викликати функцію setup з параметрами словника args_dict 
# та параметром install_requires, який набуває значення requires. Третій параметр entry_points приймає словник, 
# де ми можемо вказати список "точок входу" для ключа console_scripts.

# Структура словника для параметра args_dicts має бути наступною

# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }


#  Алгоритм : вирішення просто обновляємо наш словник ще одним новою паролю ключ і значення відповідно до умови завдання.
# Завдання вчить як маючи почакткове сформоване значення для функції поповнювати новими аргументами за певним шаблоном.

#  ++++++++++++++++++++++++++++++++++  Код /Code для атопереврки +++++++++++++++++++++++++++++++++++++++++++++++++

# def do_setup ( args_dict, requires, entry_points ) :
#     args_dict.update ( { 'install_requires': requires } ) # записуємо в наш словник в кінці нову пар ключ і значення.
#     args_dict.update ( { 'entry_points': entry_points } ) # записуємо в наш словник в кінці нову пар ключ і значення.
#     setup ( **args_dict )  # Викликаєм функцію вже з оновленими аргументами і їх значеннями.


# ================================ Звдання 4 / Task 4 ======================================