#DJANGO-EC2-AWS
[Spanish version](README_ES.md)

Simple web application made with Django. It has been deployed with
[Amazon EC2](https://aws.amazon.com/es/ec2/?trk=58ace84c-cd27-448f-9f64-ec1187db737b&sc_channel=ps&s_kwcid=AL!4422!3!590500029721!p!!g!!aws%20ec2&ef_id=Cj0KCQjwgO2XBhCaARIsANrW2X07HTO6sZZmFMW5FhTWw29Vto-K4AedH1y96tyUw3d6r0qtAbLrLmkaAtciEALw_wcB:G:s&s_kwcid=AL!4422!3!590500029721!p!!g!!aws%20ec2) service.

**Index**
1. [Modifications in the project](#1)
2. [EC2 Virtual Machine](#2)
3. [Installing the application in the virtual machine](#3)
4. [Deployment Server Configuration](#4)
5. [Supervisor Settings](#5)
6. [Launch the application](#6)

---

### Modifications in the project {#1}

For the proper functioning of the application, the following modifications have been made:
- The `settings.py` file has been modified so that it allows all HOST.

```python
ALLOWED_HOSTS = ['*']
```

- The file `requeriments.txt` has been generated with the command `pip freeze > requeriments.txt` so that the server can be installed with `pip install -r requeriments.txt`.

- Added .gitignore file so that unwanted files, such as the SECRET_KEY from the Django project, are not uploaded.

> The server is instantiated with the command `python manage.py runserver`

---

### EC2 virtual machine {#2}

It runs with the **Ubuntu Server 22.04 LTS** OS image. Instance type: t2.micro.
In network configuration the firewall rules are:
- Port 22 is open for application access.
- Port 8000 is open for access to the deployment server.
- HTTP, HTTPS and All traffic is enabled for all sources.
- The rest of the configuration was left by default.

---

### Installation of the application in the virtual machine {#3}

Once the EC2 instance is launched. On the command line, enter the following commands:

```bash
sudo apt-get update
sudo apt-get install python3-pip
udo pip3 install gunicorn
sudo apt-get install monitor
sudo apt-get install nginx -y
sudo pip3 install django
sudo apt install git-all
```

Then you must push the project to the virtual machine:

`git clone https://github.com/TadeopCreator/django-ec2-aws.git`

Install requirements: Where the requirements.txt file is located.

```bash
pip install -r requirements.txt
```

Set the environment variables for the application:
Adding the `.env` file with environment variables:

`SECRET_KEY=django-insecure-s4#YOUR_SECRET_KEY`

Editing the `settings.py` file to make use of environment variables:

```python
import environment
matter you

# Initialize environment variables
env = environment.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
```

---

### Deployment server configuration {#4}

```bash
sudo cp django-ec2-aws/deploy/nginx.conf /etc/nginx/sites-available/django-ec2-aws
sudo ln -s /etc/nginx/sites-available/django-ec2-aws /etc/nginx/sites-enabled/django-ec2-aws
sudo service nginx restart
```

---

### Supervisor configuration {#5}

```bash
sudo cp django-ec2-aws/deploy/django-ec2-aws.conf /etc/supervisor/conf.d/django-ec2-aws.conf
sudo supervisor ctl reread
sudo supervisor ctl update
sudo supervisorctl restart django-ec2-aws
```

---

## Launch the application {#6}

```bash
python3 manage.py runserver 0:8000
```

Now the app is running on the deployment server :smile:. The application can be accessed from the browser.

That has been all we need to launch the application.
To exit the virtual machine, execute the `exit` command.

Thanks to the video [C2 deploy DJango application | NGINX | Overseer | Gunicorn](https://www.youtube.com/watch?v=wIx9c_RjUaA&list=WL&index=6&t=721s)
from Technology Hub for providing a guide to deploying an application with AWS EC2.
