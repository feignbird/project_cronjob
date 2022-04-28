#Running Project Cronjob

<p>
This project is for showing you the use of cronjob/crontab. Cronjob is a program which can do a task or execute a function at a notified time, this can happend repeatedly.
</p>

## If you want to setup quickly have the project running up

1. `git clone git@github.com:feignbird/project_cronjob.git`
Clone the project

2. `cd project_cronjob`
Change dir

3. `chmod 744 run.sh`
Change permission of run.sh

4. `./run.sh`
execute run.sh
while running any pop-up comes then press 'OK'
Create super user

### Now your project is running, Now you can look for the endpoints below

### But if you want to stop the project for some time, press 
1. ` ctrl + c `

### If you again want to run the project from the terminal, run below commands
1. ` source cron-env/bin/activate `
2. ` cd api `
3. ` python manage.py runserver 0.0.0.0:8083 `

### If you want to stop the activate cronjobs, run below commands
if you are in project_cronjob folder (check using 'pwd' command)
1. ` cd api `
2. ` python manage.py crontab remove`

### if you want to again add specified cronjob to the crontab, run below commands
if you are in project_cronjob folder (check using 'pwd' command) & you're in api/ foler then jump to 2nd point.
1. ` cd api `
2. ` python manage.py crontab add`
or 
3. if you just want to see which active jobs are present `python manage.py crontab add ` 


Note:
if your port is already in use then run
`source cron-env/bin/activate`
`python manage.py runserver 0.0.0.0:8081` `<- [input_port_that_is_not_in_use] `

<hr>

## Follow below shown commands to run the program by writing each command yourself

1.` python3 -m venv cron-env`
 Above command will setup a python virtual environment named as 'cron-env', A virtual environment is needed beacause its good to source all our installed dependencies from a local environment & also, it helps running multiple projects on the same computer at the same time, with their own virtual environment.

2. ` source cron-env/bin/activate`
` Above command will tell terminal/computer that for this project source all the dependencies from 'cron-env' VE`

3.` python3 -m pip install --upgrade pip `
Above command will upgrade the pip package on our VE

4.` pip install -r requirements.txt `
 Above command will install the dependecies mentioned in requirements.txt file. For showing working of cronjobs, we just need four packages/dependencies: Django - for using django framework, DjangoRestFramework - for making RESTful APIs, Django-Crontab - for using cronjobs, Requests - for making http request to urls

5. ` cd api `
 Above command will change the directory you are working on to 'api' named dir `

6. ` python manage.py makemigrations && python manage.py migrate ` 
Above command will migrate the migrations

7. ` python manage.py crontab add `
 Above command will add specified cronjobs as a active cronjob in crontab 
 Note: Press OK if some permission window pops up 

8. ` python manage.py createsuperuser `
 By using Above command you can create a superuser for logging in the ADMIN panel

9. ` python manage.py runserver 0.0.0.0:9000 `
 Above will run your django project 

 Now you can hit 'http://0.0.0.0:9000/users/' endpoint to get the users created by crontab every 2 minutes 



## API Endpoints
### There are total of 2 endpoints <br>

11. ` GET http://localhost:9000/users/ ` <- Gives data of created users

2. ` GET http://localhost:9000/swagger.json `<- get swagger.json data

3. Goto URL: ` http://localhost:9000/admin/ `<- Log into admin panel to see created users

4. Goto URL: ` http://localhost:9000/swagger/ `<- Opens up swagger for the project

5. Goto URL: http://localhost:9000/redoc/ <- Opens up redoc generator for project <br>

` You can also see their 'data_joined' attribute, Difference b/w every user creation is 2 minutes `

### How to work with cronjob

1. `pip install django-crontab`
2. put in installed_apps -> django_crontab
3. add cron.py in any app you want & in that file you have to define functions that should be running on cronjobs.
4. add settings of cronjobs or Configuration of cronjobs in settings.py
```
 CRONJOBS = [ `
    `('* * * * *', 'location_to_the_function_you_want_to_run.cron.function_name', ``[list_of_positional_arguments_to_the_method], {'dictionary_of_keywork_argument':'_for_the_method'},"job_specifix_suffix") `
`]
```
5. ran the command `python manage.py crontab add`
6. if want to remove the cronjob just run `python manage.py crontab remove`, It'll remove every active cronjob from the crontab
7. if you want to see what cronjobs are activated, just run `python manage.py crontab show`

<br>
`for
 more information : https://pypi.org/project/django-crontab/`

