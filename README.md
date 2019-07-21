# db-hack

В файле scripts.py есть 3 функции:
1) fix_marks позволяет исправить оценки ученика в базе данных на пятерки;
2) remove_chastisements удаляет замечания ученика;
3) adding_commendation добавляет благодарность ученику от преподователя.

### Как установить

Необходимо скачать файл scripts.py на компьютер.

### Пример использования

Из базы данных, с помощью Django shell, получите учетную запись ученика, которому нужно внести изменения. Например:
```
from datacenter.models import Schoolkid
>>> child = Schoolkid.objects.filter(full_name__contains="Фролов Иван")[0]
>>> child
<Schoolkid: Фролов Иван Григорьевич 6А>
```
Для работы всех функций, необходимо, также импортировать следующие модели данных:
```
>>> from datacenter.models import Mark, Сhastisement, Lesson, Commendation
```

Импортируйте нужную функцию из файла scripts.py. Также, для функции adding_commendation, необходимо импортировать random:
```
>>> from scripts import adding_commendation
>>> import random
```
Далее, используйте саму функцию, введя данные, например:
```
>>> commendation = adding_commendation(child, 'Музыка')
>>> commendation
<Commendation: Фролов Иван Григорьевич>
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).