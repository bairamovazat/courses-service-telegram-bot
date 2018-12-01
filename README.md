#Базовая демонстрация телеграм бота без сервиса.

* ##В планах:
    * Реализовать REST-сервис хранения и обработки данных
    * Реализовать Telegram bot для доступа к сервису
    * Реализовать Web-часть для доступа к сервису(На Vue.js)
    * Максимально разделить весь проект на независимые модули (сервис, веб интерфейс, бот телеграм, бот вк)

* ######Реализовано
    * Базовый функционал Telegram bot для демонстрации
    * Базовый "каркас" REST-сервиса (Spring, Hibernate, PostgresSQL)

Модель базы данных
![alt text](resources/database.png)

Макеты для браузерной версии (приблизительные):

Страница входа:
![Login page](design/Login&#32page.png)

Выбор курса (для студента и преподавтеля):
![studSelect](design/SelectCourse&#32Student.png)          ![teachSelect](design/SelectCourse&#32Teacher.png)

Страница курса (для студента):
![CourseMenuStud](design/Course&#32main&#32menu&#32for&#32student.png)

Страница задания с курса (для студента):
![TaskStud](design/Course&#32Task.png)

Страница центра контроля успеваемости (для студента):
![EdContrStud](design/Education&#32control&#32center.png)