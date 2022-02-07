# Drone With Cameras - Inventory App


## Instructions


### Open Console and go to folder DroneInventory/inventory_api 

install requirements.txt with Python 3.8, eg:
- ```pipenv --python 3.8```
- ```pipenv shell```
- ```pipenv install -r requirements.txt```



### Makemigrations & migrate

```python manage.py makemigrations```
then

```python manage.py migrate```


### Create user
```python manage.py createsuperuser```

### enter name and password


```python manage.py runserver <your IP adress>:8000```


open in browser 
```http://<yourIp>:8000/api/v1/```


Login with username + password

### Now you can enter camera details on this page.



## Frontend with React -> nodejs needs to be installed. I used v17.4.0

open new console and go to folder ```/DroneInventory/frontend```

```npm install``` installs packages

In file ```/DroneInventory/frontend/src/Home.js``` enter your IP (needs to be same as <youIp> from above): \
-For this you can set variable ```b``` with your IP (needs to be string format) \
-or uncomment line 13 and replace  <youIp> with your Ip adress. In this case line 14 needs to be commented out.\


```npm run start```  starts App

browser should open now, if not enter in browser ```<yourIp>:3000``` 

page should be available on other devices in network now by entering in browser: ```<yourIp>:3000```
