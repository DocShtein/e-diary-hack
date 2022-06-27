### Инструкция по установке и запуску скриптов для правки электронного дневника

Для запуска скриптов из файла `dbhack.py` необходимо скопировать данный файл в папку, где располагается файл `manage.py`

Последовательность действий:
1. В терминале перейти в директорию с файлом `dbhack.py` и запустить интерактивную консоль (shell) выполнив команду 
```
python manage.py shell
```

![image](https://user-images.githubusercontent.com/39937490/175934453-a4c7d404-aa76-4209-a1b5-aed59bb39448.png)

2. В интерактивной консоли выполнить команду 
```
import dbhack
```

![console](https://user-images.githubusercontent.com/39937490/175934530-7aa81c54-0d36-4091-b3cd-1b95cb69e2a3.jpg)

3. Описание команд для правки электронного дневника c примерами запуска:

    * `dbhack.fix_marks()` - в скобках указывается ФИО в кавычках. Команда заменяет плохие оценки (2 и 3 балла) на пятёрки:
    
    ![fix_marks](https://user-images.githubusercontent.com/39937490/175934665-49b2b510-5770-43da-9e78-aa92bb175f90.jpg)

    * `dbhack.fix_marks()` - в скобках указывается ФИО в кавычках. Команда удаляет замечания из электронного дневника:
    
    ![del_chasts](https://user-images.githubusercontent.com/39937490/175934723-5328439b-e0d5-4ad1-a1f9-96a24c3f0750.jpg)

    * `dbhack.create_commendation()` - в скобках указываются ФИО и предмет в кавычках. Команда добавляет в электронный дневник похвалу по указанному предмету:
    
    ![commend](https://user-images.githubusercontent.com/39937490/175934772-4a0793cd-6f9c-439d-a2ee-a85d4ecf5b00.jpg)

Для копирования:
```
dbhack.fix_marks()
```
```
dbhack.fix_marks()
```
```
dbhack.create_commendation()
```

### Цели проекта
Данный проект связан с [электронным дневником школы](https://github.com/DocShtein/e-diary)

Этот сайт - интерфейс для учеников школы. Здесь можно посмотреть оценки, расписание и прочую открытую информацию. Учителя заполняют базу данных через другой сайт. Ставят там оценки и т.д.

Для работы на проектом необходимо развернуть сайт и получить файл базы данных.

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
