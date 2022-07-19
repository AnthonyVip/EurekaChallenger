# EurekaChallenger
English:

For the solution of the challenge I have decided to use the FastAPI framework for the api development 
together with PostgreSQL as database engine and the sqlmodel ORM.

all libraries used in the project are added in requirements.txt

steps to run the project on local:
1. Install the libraries in the terminal: pip install -r requirements.txt
2. modify the file in the path: /app/v1/settings/settings.cfg and change the values of the database
3. execute the file in the path /app/v1/model/create_db.py to create the tables in the database
4. to run the project you could run directly in the terminal: python main.py or you could also use the following command: uvicorn main:app --host 0.0.0.0.0 --port 8000
5. to test the functionality of the project we would make use of the Swagger UI in the path {host}:{port}/docs this UI will allow us to see the api documentation and test all the endpoints

heroku testing steps:
1. enter the Swagger UI through the following url: https://eureka-challenger.herokuapp.com/docs
2. Swagger UI allows us to test all the endpoints of the api, as well as to see their documentation.
3. to test the endpoints that require authorization (in this case /api/v1/symbol/) you must log into Swagger UI with a valid email and password, to do this you must click on the Authorize button located in the upper right corner of the screen and enter the email and password.
4. once step 3 is done, the /api/v1/symbol/ endpoint can be tested.


Español:

Para la solucion del reto he decidido usar el framework FastAPI para el desarrollo de la api
junto con PostgreSQL como motor de base de datos y el ORM sqlmodel.

todas las librerias usadas en el proyecto estan añadidas en el requirements.txt

pasos para correr el proyecto en local:
1. Instalar las librerias en el terminal: pip install -r requirements.txt
2. modificar el acrhivo en la ruta: /app/v1/settings/settings.cfg y cambiar los valores de la base de datos
3. ejecutar el archivo en la ruta /app/v1/model/create_db.py para crear las tablas en la base de datos
4. para correr el proyecto se podria ejecutar directamente en el terminal: python main.py o tambien se podria usar el siguiente comando: uvicorn main:app --host 0.0.0.0 --port 8000
5. para probar la funcionalidad del proyecto se haria uso de la Swagger UI en la ruta {host}:{port}/docs esta UI nos permitira ver la documentacion de la api y probar todos los endpoints

pasos para las pruebas en heroku:
1. ingresar a la Swagger UI mediante la siguiente url: https://eureka-challenger.herokuapp.com/docs
2. Swagger UI nos permite probar todos los endpoints de la api, asi como ver la documentacion de los mismos.
3. para probar los endpoints que requieren autorizacion(en este caso /api/v1/symbol/) se debe loguear en Swagger UI con un email y contraseña valido, para ello se debe le debe dar click en el boton Authorize localizado en la esquina superior derecha de la pantalla e ingresar el email y contraseña.
4. una vez hecho el paso 3 ya se podra probar el endpoint /api/v1/symbol/

