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

` Now you can hit 'http://0.0.0.0:9000/users/' endpoint to get the users created by crontab every 2 minutes `



## API Endpoints
### There are total of 2 endpoints <br>

1. GET http://localhost:9000/users/ <- Gives data of created users

2. GET http://localhost:9000/swagger.json <- get swagger.json data

3. Goto URL: http://localhost:9000/admin/ <- Log into admin panel to see created users <br>

4. Goto URL: http://localhost:9000/swagger/ <- Opens up swagger for the project

5. Goto URL: http://localhost:9000/redoc/ <- Opens up redoc generator for project <br>

` You can also see their 'data_joined' attribute, Difference b/w every user creation is 2 minutes `

### How to work with cronjob

1. pip install django-crontab
2. put in installed_apps -> django_crontab
3. add cron.py in any app you want & in that file you have to define functions that should be running on cronjobs.
4. add settings of cronjobs or Configuration of cronjobs in settings.py
` CRONJOBS = [ `
    `('* * * * *', 'location_to_the_function_you_want_to_run.cron.function_name', ``[list_of_positional_arguments_to_the_method], {'dictionary_of_keywork_argument':'_for_the_method'},"job_specifix_suffix") `
`]`
5. ran the command 'python manage.py crontab add'
6. if want to remove the cronjob just run 'python manage.py crontab remove', It'll remove every active cronjob from the crontab
7. if you want to see what cronjobs are activated, just run 'python manage.py crontab show'
for more information : https://pypi.org/project/django-crontab/

