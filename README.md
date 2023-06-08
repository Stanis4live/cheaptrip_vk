# Тестированние VK API&UI http://vk.com/
# дополнено stanis.forlive@gmail.com

#### 1. Для запуска тестов необходимо установить виртуальное окружение:
> python -m venv venv
-  Активировать виртуальное окружение:
> source venv/Scripts/activate
- Установить зависимости:
> pip install -r requirements.txt


#####2. Перед запуском тестов необходимо внести следующие данные в файл /_test_data/access_data.py:
- TOKEN
> access_token для работы с api vk, описание получения токена https://dev.vk.com/api/access-token/implicit-flow-user
> ссылка, по которой можно просто получить токен https://vkhost.github.io/
- OWNER_ID
> id группы или пользователя на стене которого нужно разместить пост.
> id сообщества начинается со знака "-"
- DOMAIN
> имя профиля пользователя, отображающееся в адресной строке при нахождении на "Моя страница" (http://vk.com/domain)





