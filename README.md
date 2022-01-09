Запустить docker-compose
Установить зависимости requirements_for_ scrypt.txt (pip install -r requirements_for_scrypt.txt) для alarm.py в виртуальной среде

GET
http://localhost:8080/
получение всех записей

POST
http://localhost:8080/
Создание новой записи  бд

PUT
http://localhost:8080/<string:id_key>
Изменение записи по id
