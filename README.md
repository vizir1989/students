based on https://github.com/markqiu/fastapi-mongodb-realworld-example-app

TODO:
0. jwt (https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) +
1. logging (mount mongodb logging)
2. coverage +
3. code style
4. sonar or something like this
5. redis
6. prometheus and graphana
7. logging parser

# run pytest
1. run docker-compose
```shell
docker-compose up -d --force-recreate
```
2. run pytest
```shell
docker-compose exec web coverage run -m tox .
```
3. check coverage
```shell
docker-compose exec web coverage report
```

4. run checking codestyle
```shell
pycodestyle --config pycodestyle.ini .
```