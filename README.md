#### myRetail REST

---

Simple REST API with providing get, post put and tokenized get.

Running upon swagger UI (Documentation Tool)

```
products
    - get products
    - get products/{id}
    - put products/{id}

v1/redsky
    - post auth 
        (payload: {"username": *, "password": password})
    - get /case_study_v1?key={}&tcin={}
```

---

#### REQUIREMENTS

* Python3.9
* Docker

---

#### INSTALLATION

```
git clone git@github.com:solly0702/myRetail_REST.git
cd myRetail_REST
docker-compose build
docker-compose up -d
```

`app will be running on 0.0.0.0:3003`

---

#### CONFIGURATION

```
# FLASK CONFIGURATION
./app/.flask_env
-----------------------
ENV={production, test, development}
SECRET_KEY={key to encode and decode jwt}
DB_HOST={mongodb host from mongodb image (docker-compose.yml)}
DB_PORT={mongodb port (default=27017)}
DB_USER={mongodb username from image }
DB_PWD={mongodb password from image}
DB_SOURCE={mongodb user role}
DB_NAME={mongodb database name}

# DB CONFIGURATION
./docker/.db_env
MONGO_INITDB_DATABASE={initial dbname}
MONGO_INITDB_ROOT_USERNAME={db username}
MONGO_INITDB_ROOT_PASSWORD={db userpassword}
```

---

#### TEST

Unit test with pytest module. Test covers database model field and validation function.

`cd myRetail_REST && pytest`
