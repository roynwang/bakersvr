mysql -uroot -p435393055 -e'drop database baker;CREATE DATABASE baker DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
