python3 -m venv cron-env
source cron-env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
cd api
python manage.py makemigrations && python manage.py migrate
python manage.py crontab add
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8083