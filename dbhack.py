import random

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import Schoolkid, Lesson, Mark, Commendation, Chastisement, Teacher


def check_schoolkid_name(name):
    if name != '':
        try:
            Schoolkid.objects.get(full_name__contains=name)
        except MultipleObjectsReturned:
            print('Ошибка! Найдено больше одного ученика с указанным именем.')
        except ObjectDoesNotExist:
            print('Ошибка! Ученик с указанным именем не найден или допущена опечатка.')
    else:
        print('Введен пустой запрос. Укажите имя ученика!')


def create_commendation(full_name, lesson):
    check_schoolkid_name(full_name)
    child = Schoolkid.objects.filter(full_name=full_name)

    commendations = [
        'Молодец', 'Отлично!', 'Хорошо!', 'Гораздо лучше', 'чем я ожидал!', 'Ты меня приятно удивил!',
        'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!',
        'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
        'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
        'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!'
    ]

    target_lesson = Lesson.objects.filter(group_letter='А', year_of_study=6, subject__title=lesson)

    try:
        Commendation.objects.create(
            text=random.choice(commendations),
            created=target_lesson[0].date,
            schoolkid=child[0],
            subject=target_lesson[0].subject,
            teacher=target_lesson[0].teacher
        )
    except IndexError:
        print('Ошибка! Опечатка в названии предмета.')
    else:
        print('Похвала добавлена в дневник!')


def fix_marks(full_name):
    check_schoolkid_name(full_name)
    child = Schoolkid.objects.filter(full_name=full_name)
    return f'Исправлено плохих оценок: {Mark.objects.filter(schoolkid=child[0], points__lte=3).update(points=5)}'


def remove_chastisements(full_name):
    check_schoolkid_name(full_name)
    child = Schoolkid.objects.filter(full_name=full_name)
    Chastisement.objects.filter(schoolkid=child[0]).delete()
    return 'Замечания удалены из дневника!'
