This repository was created when I was learning backend development during the Meta Back-end Development online course. 
Feel free to take a look at the code :)

# Enviroment: VENV

- To activate run:
    "source env/bin/activate"

- To deactivate
    "deactivate"

- To instal requirements:
    "pip install -r requirements.txt"
-------------------------------------------

# Project Level
- static HTML
http://127.0.0.1:8000/

- admin pannel
http://127.0.0.1:8000/admin/

- the API
http://127.0.0.1:8000/api/

- djoser endpoints
http://127.0.0.1:8000/auth/
    
    - create user 
    http://127.0.0.1:8000/auth/users/

    - crearte token
    http://127.0.0.1:8000/auth/token/login/

- to obtain token by DRF
http://127.0.0.1:8000/api-token-auth/

-------------------------------------------

# App Level

- menu item endpoints
http://127.0.0.1:8000/api/menu-items/
http://127.0.0.1:8000/api/menu-items/<pk>

- booking endpoints (mapped with Router)
http://127.0.0.1:8000/api/booking/tables/
http://127.0.0.1:8000/api/booking/tables/<pk>

-------------------------------------------

# MySQSL

- Configure the database setting accordingly with your database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'admindjango',
        'PASSWORD': 'employee@123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
