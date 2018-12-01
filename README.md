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
![alt text](design/designWeb.psd)

Страница входа:
![alt text](design/Login page.png)

Выбор курса (для студента и преподавтеля):
![alt text](design/SelectCourse Student.png)          ![alt text](design/SelectCourse Teacher.png)

Страница курса (для студента):
![alt text](design/Course main menu for student.png)

Страница задания с курса (для студента):
![alt text](design/Course Task.png)

Страница центра контроля успеваемости (для студента):
![alt text](design/Education control center.png)