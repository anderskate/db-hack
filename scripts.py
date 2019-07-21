import random


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    return bad_marks


def remove_chastisements(schoolkid):
    chastisements = Сhastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
    return chastisements


def add_commendation(schoolkid, subject_title):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Ты меня приятно удивил!',
        'Талантливо!',
        'Так держать!',
        'Здорово!',
        'Я вижу, как ты стараешься!',
        'Я поражен!',
        'Это как раз то, что нужно!',
        'Великолепно!',
        'Я тобой горжусь!'
    ]
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title
    )
    random_commendation = random.choice(commendations)
    random_lesson = random.choice(lessons)
    commendation = Commendation.objects.create(
        text=random_commendation,
        created=random_lesson.date,
        schoolkid=schoolkid,
        subject=random_lesson.subject,
        teacher=random_lesson.teacher
    )
    return commendation