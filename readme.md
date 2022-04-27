# Running Project Cronjob
` This project is for showing you the use of cronjob/crontab. `
` Cronjob is a program which can do a task or execute a function at a notified time, this can happend repeatedly. `

## Follow below shown commands to run the program

1. python3 -m venv cron-env 
` Above command will setup a python virtual environment named as 'cron-env', A virtual environment is needed beacause its good to source all our installed dependencies from a local environment & also, it helps running multiple projects on the same computer at the same time, with their own virtual environment.`

2. source cron-env/bin/activate
` Above command will tell terminal/computer that for this project source all the dependencies from 'cron-env' VE`

3. python3 -m pip install --upgrade pip
` Above command will upgrade the pip package on our VE `

4. pip install -r requirements.txt
` Above command will install the dependecies mentioned in requirements.txt file. For showing working of cronjobs, we just need four packages/dependencies: Django - for using django framework, DjangoRestFramework - for making RESTful APIs, Django-Crontab - for using cronjobs, Requests - for making http request to urls `

5. cd api
` Above command will change the directory you are working on to 'api' named dir `

6. python manage.py makemigrations && python manage.py migrate
` Above command will migrate the migrations `

7. python manage.py crontab add
` Above command will add specified cronjobs as a active cronjob in crontab `
` Note: Press OK if some permission window pops up `

8. python manage.py createsuperuser
` By using Above command you can create a superuser for logging in the ADMIN panel `

9. python manage.py runserver 0.0.0.0:9000
` Above will run your django project `

` Now you can hit 'http://0.0.0.0:9000/' endpoint to get the user created by crontab every 2 minutes `
