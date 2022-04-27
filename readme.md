# Running Project Cronjob
` This project is for showing you the use of cronjob/crontab. `
` Cronjob is a program which can do a task or execute a function at a notified time, this can happend repeatedly. `

## If you want to setup quickly have the project running up

1. git clone git@github.com:feignbird/project_cronjob.git <br>
` Clone the project `

2. cd project_cronjob <br>
` Change dir `

3. chmod 744 run.sh <br>
` Change permission of run.sh `

4. ./run.sh <br>
` execute run.sh ` <br>
` while running any pop-up comes then press 'OK' `<br>
` Create super user`

`Note:`<br>
` if your port is already in use then run` <br>
source cron-env/bin/activate<br>
python manage.py runserver 0.0.0.0:8081 `<- [input_port_that_is_not_in_use] `<br>


<hr>

## Follow below shown commands to run the program by writing each command yourself

1. python3 -m venv cron-env <br>
` Above command will setup a python virtual environment named as 'cron-env', A virtual environment is needed beacause its good to source all our installed dependencies from a local environment & also, it helps running multiple projects on the same computer at the same time, with their own virtual environment.`

2. source cron-env/bin/activate <br>
` Above command will tell terminal/computer that for this project source all the dependencies from 'cron-env' VE`

3. python3 -m pip install --upgrade pip <br>
` Above command will upgrade the pip package on our VE `

4. pip install -r requirements.txt <br>
` Above command will install the dependecies mentioned in requirements.txt file. For showing working of cronjobs, we just need four packages/dependencies: Django - for using django framework, DjangoRestFramework - for making RESTful APIs, Django-Crontab - for using cronjobs, Requests - for making http request to urls `

5. cd api <br>
` Above command will change the directory you are working on to 'api' named dir `

6. python manage.py makemigrations && python manage.py migrate <br>
` Above command will migrate the migrations `

7. python manage.py crontab add <br>
` Above command will add specified cronjobs as a active cronjob in crontab `
` Note: Press OK if some permission window pops up `

8. python manage.py createsuperuser <br>
` By using Above command you can create a superuser for logging in the ADMIN panel `

9. python manage.py runserver 0.0.0.0:9000 <br>
` Above will run your django project `

` Now you can hit 'http://0.0.0.0:9000/' endpoint to get the user created by crontab every 2 minutes `

