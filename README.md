# asap-simple-crud
## PaaS access
https://nameless-thicket-68176.herokuapp.com/


## Running it local
1. Clone it
    ```sh
    git clone git@github.com:leocabralweb/asap-simple-crud.git
    cd asap-simple-crud
    ```
2. Install requirements:
    ```sh
    pip install -r requirements.txt
    ```
3. Export database configuration URL to DATABASE_URL env var:
    ```
    export DATABASE_URL='postgres://...'
    ```
4. Run django scripts
    ```
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver 0:8000
    ```
5. Access throught http://localhost:8000
