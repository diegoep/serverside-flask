# Administration Frontend (Server-side)

## Installation

## Init the database

First configure the database with name, user and password "rdo".

After that, start the database through the command:
```
python3 manage.py db init
```

Then create the migration:
```
python3 manage.py db migrate
```

To apply the migration changes to the database run the command:
```
python3 manage.py db upgrade 
```


To create default user:
```
python3 manage.py seed 