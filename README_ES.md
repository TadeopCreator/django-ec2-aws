# DJANGO-EC2-AWS

Simple aplicacion web realizada con Django. Ha sido desplegada con el
servicio de [Amazon EC2](https://aws.amazon.com/es/ec2/?trk=58ace84c-cd27-448f-9f64-ec1187db737b&sc_channel=ps&s_kwcid=AL!4422!3!590500029721!p!!g!!aws%20ec2&ef_id=Cj0KCQjwgO2XBhCaARIsANrW2X07HTO6sZZmFMW5FhTWw29Vto-K4AedH1y96tyUw3d6r0qtAbLrLmkaAtciEALw_wcB:G:s&s_kwcid=AL!4422!3!590500029721!p!!g!!aws%20ec2).

**Índice**   
1. [Modificaciones en el proyecto](#1)
2. [Maquina virtual EC2](#2)
3. [Instalacion de la aplicacion en la maquina virtual](#3)
4. [Configuracion del servidor de despliegue](#4)
5. [Configuracion del supervisor](#5)
6. [Lanzar la aplicacion](#6)

---

### Modificaciones en el proyecto <a name="1"></a>

Para el buen funciona de la aplicacion se han realizado las siguientes modificaciones:
- Se ha modificado el archivo `settings.py` para que permite todo HOST.
	
	```python
	ALLOWED_HOSTS = ['*']
	```

- Se ha generado el archivo `requeriments.txt` con el comando `pip freeze > requeriments.txt` para que se pueda instalar el servidor con `pip install -r requeriments.txt`.

- Se ha añadido el archivo .gitignore para que no se suban archivos no deseados, como la SECRET_KEY del proyecto de Django.

>Se instancia el servidor con el comando `python manage.py runserver`

---

### Maquina virtual EC2 <a name="2"></a>

Corre con la imagen del SO **Ubuntu Server 22.04 LTS**. Tipo de instacia: t2.micro.
En configuracion de red las reglas de firewall son:
- El puerto 22 esta abierto para el acceso a la aplicacion.
- El puerto 8000 esta abierto para el acceso al servidor de despliegue.
- HTTP, HTTPS y All traffic esta habilitado para toda fuente.
- El resto de la configuracion se dejo por defecto.

### Instalacion de la aplicacion en la maquina virtual <a name="3"></a>

Una vez lanzada la instancia del EC2. En la linea de comandos se deben introducir los siguientes comandos:

```bash
sudo apt-get update
sudo apt-get install python3-pip
udo pip3 install gunicorn
sudo apt-get install supervisor
sudo apt-get install nginx -y
sudo pip3 install django
sudo apt install git-all
```

Luego se debe realizar el push del proyecto a la maquina virtual:

`git clone https://github.com/TadeopCreator/django-ec2-aws.git`

Instalar los requerimentos: Donde se encuentra el archivo `requeriments.txt`

```bash
pip install -r requeriments.txt
```

Configurar las variables de entorno para la aplicacion:
Añadiendo el archivo `.env` con las variables de entorno:

`SECRET_KEY=django-insecure-s4#YOUR_SECRET_KEY`

Editando el archivo `settings.py` para hacer uso de las variables de entorno:

```python
import environ
import os

# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
```

---

### Configuracion del servidor de despliegue <a name="4"></a>

```bash
sudo cp django-ec2-aws/deploy/nginx.conf /etc/nginx/sites-available/django-ec2-aws
sudo ln -s /etc/nginx/sites-available/django-ec2-aws /etc/nginx/sites-enabled/django-ec2-aws
sudo service nginx restart
```

---

### Configuracion del supervisor <a name="5"></a>

```bash
sudo cp django-ec2-aws/deploy/django-ec2-aws.conf /etc/supervisor/conf.d/django-ec2-aws.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart django-ec2-aws
```

---

## Lanzar la aplicacion <a name="6"></a>

```bash
python3 manage.py runserver 0:8000
```

Ahora la app esta corriendo en el servidor de despliegue :smile:. Se puede acceder a la aplicacion desde el navegador.

Eso ha sido todo lo que necesitamos para lanzar la aplicacion.
Para salir de la maquina virtual se debe ejecutar el comando `exit`

Gracias al video [C2 deploy DJango application | NGINX | Supervisor | Gunicorn](https://www.youtube.com/watch?v=wIx9c_RjUaA&list=WL&index=6&t=721s)
de Technology Hub por ofrecer una guia para desplegar una aplicacion con AWS EC2.
