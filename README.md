#Базовая демонстрация телеграм бота.

##Серверная часть:
	* https://bitbucket.org/azatbairamov/courses-service/src/master/

##тыкай сюда, если бот не отвечает https://courses-service-telegram-bot.herokuapp.com
######(Т.к сервис засыпает, когда нет запросов. Веб хуки не настроены так что от бота не просыпается)

* ##В планах:
    * Реализовать REST-сервис хранения и обработки данных
    * Реализовать Telegram bot для доступа к сервису
    * Реализовать Web-часть для доступа к сервису(На Vue.js)
    * Максимально разделить весь проект на независимые модули (сервис, веб интерфейс, бот телеграм, бот вк)

* ######Реализовано
    * Базовый функционал Telegram bot для демонстрации
    * Базовый "каркас" REST-сервиса (Spring, Hibernate, PostgresSQL)

* ######Участники:
	* Байрамов Азат
	* Лигай Вячеслав
	* Тахаутдинов Камиль
	* Рыжов Егор
	* Низамутдинов Ильгиз

Модель базы данных
![alt text](resources/database.png)

Макеты для браузерной версии (приблизительные):

Страница входа:
![Login page](design/LoginPage.png)

Выбор курса (для студента и преподавтеля):
![studSelect](design/SelectCourseStudent.png)          ![teachSelect](design/SelectCourseTeacher.png)

Страница курса (для студента):
![CourseMenuStud](design/CourseMainMenuForStudent.png)

Страница задания с курса (для студента):
![TaskStud](design/CourseTask.png)

Страница центра контроля успеваемости (для студента):
![EdContrStud](design/EducationControlCenter.png)