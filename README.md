### qa_guru_hw_19_mobile_automation

Задание:
1) Зарегистрировать аккаунт в https://browserstack.com
2) Запустить автотест из занятия локально
3) Разработать еще один автотест на открытие любой статьи(статья не будет отображена на browserstack, 
отображена будет ошибка, вам нужно реализовать только клик на то, что вы ищите). 
Если хотите чтобы статью было видно, нужно залить свою апк википедии и работать с ней.
4) Разработать еще один автотест на iOS
5) Адаптировать conftest.py для работы с двумя типами платформ - Android, iOS
6) Вынести данные (логин, пароль, урл BrowserStack и т.д.) в .env с pydantic
7) Сделать сборку в Jenkins