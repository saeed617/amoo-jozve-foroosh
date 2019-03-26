+ clone repo

```
git clone https://github.com/saeed617/amoo-jozve-foroosh.git
```

+ cd into project dir
```
cd amoo-jozve-foroosh
```

+ install `virtualenv` and create a new virtual environment

```
pip install virtualenv
virtualenv venv
```

+ activate `virtualenv`
```
source venv/bin/activate
```

+ install requirements
```
pip install requirements/development.txt
```

+ run `migrate` command
```
python manage.py migrate
```

+ run server
```
python manage.py runserver
```

+ open `localhost:8000` on your favorite browser and enjoy