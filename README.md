# Practice fast api with mysql and sqlalchemy and alembic

- Source from [devpress.csdn.net](https://devpress.csdn.net/python/62f5096cc6770329307fb178.html) <-- Thanks a lot this guy. :D


## Mysql

- Run docker command:

```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -p 3306:3306 -p 33060:33060 -d mysql:8.0.32
```

- Create user:

```
CREATE USER 'xyz'@'localhost' IDENTIFIED BY 'password';
```

- Grant permission:

```
GRANT ALL PRIVILEGES ON *.* TO 'xyz'@'localhost' WITH GRANT OPTION;
```

- Make sure the new privileges are put into effect:

```
FLUSH PRIVILEGES;
```


- Create database:

```
CREATE DATABASE fastapi_blog;
```

- Create migrations environment by running `alembic` init command. (**Note**) init alembic easy to see but hard to know what it is so `migrations` is best I think so.

```
alembic init migrations
```


- Adding User and Articles Table by `alembic` command:

```
alembic revision --autogenerate -m "Adding User and Article Table"
```

- Command above create migration file. Command below create tables:

```
alembic upgrade head
```
