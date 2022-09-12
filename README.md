# Комментарии к заданию.

По заданию нужно было сделать всего два эндпоинта, и я добавил еще два аналогичных для модели Orders из дополнительной задачи. Создание моделей в таком случае возможно в админ панеле, логин и пароль я вам прислал в ответе на HeadHunter. Модели Tax и Discount связанны с соответстующими моделями в моем аккаунте на Stripe,создать их через админ панель не получится, но я добавил несколько, полагаю этого хватит чтобы протестировать.

# API
<ul>
  <li>GET /api/buy/{id}/ - Получить Stripe session ID для оплаты Item </li>
  <li>GET /api/items/{id}/ - Получить HTML-странцу с информацией об Item и кнопка Buy для переходя на старницу оплаты </li>
  <li>GET /api/orders/buy/{id}/- Получить Stripe session ID для оплаты Order</li>
  <li>GET /api/orders/{id}/ - Получить HTML-странцу с информацией о заказе и кнопка Buy для переходя на старницу оплаты </li>
</ul>

# Где расположен 

Протестировать API можно по адресу http://51.250.22.169/

# Как запустить локально
Для запуска приложения у вас должен быть установлен docker-compose, и зарегестрированный аккаунт на https://stripe.com/

Склонировать репозиторий и перейти в каталог infra/

```
https://github.com/ilinNE/stripe_assessment_test.git
cd stripe_assessment_test/infra/
```
Заполнить в файле .env секретный и публичный ключи stripe. Остальные переменные заполнены тестовыми данными, достаточными для запуска.  
Запустить контенеры в фоновом режиме

```
sudo docker-compose up -d
```
Выполнить миграции,собрать статческие файлы и создать супервользователя.
```
sudo docker-compose exec django python manage.py migrate
sudo docker-compose exec django python manage.py collectstatic
sudo docker-compose exec django python manage.py createsuperuser
```
Теперь приложение доступно по адресу http://localhost/

Можно войти в панель администратора http://localhost/admin/ используя логин и пароль суперпользователя, и наполнить базу обьектми.
