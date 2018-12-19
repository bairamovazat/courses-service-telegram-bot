from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    rec_book_number = models.CharField(max_length=128)
    is_teacher = models.BooleanField()
    telegram_id = models.IntegerField()
    confirm = models.BooleanField(default=False)
    password = models.CharField(max_length=128)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_teacher_id')
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    visit_users = models.ManyToManyField(User)


class Exercise(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    lesson = models.ForeignKey(Lesson)
    max_scope = models.IntegerField()


class Grade(models.Model):
    exercise = models.ForeignKey(Exercise)
    student = models.ForeignKey(User)
    score = models.IntegerField()


class Post(models.Model):
    exercise = models.ForeignKey(Exercise)
    course = models.ForeignKey(Course)
    text = models.CharField(max_length=256)
    name = models.CharField(max_length=64)
