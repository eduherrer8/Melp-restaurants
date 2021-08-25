
# Melp-restaurants
  

## Installation

You must have [Docker](https://www.docker-com/)

1.  Create an `.env`file. You can copy or rename the `example.env`file

2.  Start the containers
```
docker-compose up
```
3. The site will be up at
```
http://localhost:8000/
```
## Uploading data 
For this particular case, it's useful to do it in the django admin site

To get access you must first create a superuser, with the containers up
```
docker-compose exec api bash
```
Once in the container
```
python manage.py createsuperuser
```
Now go to the admin site and login
```
http://localhost:8000/admin
```
1. In the restaurants section choose import (top right corner)
2. Choose the file and format
3. Confirm import

As long as it has the same format as the one provided it should be alright

## Running the tests

```
docker-compose run --rm api python manage.py test
```

## Stop the project
```
docker-compose down
```

## Docs
The API docs are available as postman collection under `MELP.postman_collection.json`
