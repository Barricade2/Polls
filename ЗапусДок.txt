КОМАНДЫ
...\> pip install virtualenv
...\> py -m venv venv
...\> venv\Scripts\activate
...\> pip install -r requirements.txt
...\> py manage.py runserver
Starting development server at http://127.0.0.1:8000


Документация должна открываться по ссылке http://127.0.0.1:8000/api/v1/swagger/
Можно ориентироваться по url.

Главная страница - http://127.0.0.1:8000/
Страница для опроса - http://127.0.0.1:8000/polls/
При нажатии на опрос открывается вопросы - http://127.0.0.1:8000/polls/1/question/
Вопросы содержат перечни.

Только у админа есть права добавить, удалить, редактировать опрос, вопрос, пречни. Пароль - admin, логин - admin.
А у обычных пользователей нет авторизации как такого, им этого не нужно. Их имена будут храниться на некоторе время в сессиях, чтобы 
отследить их действия. 

Страница с Api url'ами - http://127.0.0.1:8000/api/v1/polls/
Главный список со всеми атрибутами - http://127.0.0.1:8000/api/v1/polls/pollsapi/
Атрибуты опросов get,post - http://127.0.0.1:8000/api/v1/polls/pollssingl
Атрибуты вопросов get,post http://127.0.0.1:8000/api/v1/polls/questionsingl/
Атрибуты опроса для запроса put, delete http://127.0.0.1:8000/api/v1/polls/pollssinglId/<int:pk>/
Атрибуты вопроса для запроса put, delete http://127.0.0.1:8000/api/v1/polls/questionsinglId/<int:pk>/
Абстрактные пользователи - http://127.0.0.1:8000/api/v1/polls/userchoicesingl/<int:pk>/

Проект состоит из трех главных папок.
-api
--v1/polls
-apps
--polls
--polls_login
-config

Надо будет через фронтент запросы кидать в api или взять данные из этого api, переделать скрипты запросов внутри templates  через ajax формы.