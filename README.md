# EurekaChallenger
English:

For the solution of the challenge I have decided to use the FastAPI framework for the api development 
together with PostgreSQL as database engine and the sqlmodel ORM.

all libraries used in the project are added in requirements.txt

steps to run the project on local:
1. Install the libraries in the terminal: pip install -r requirements.txt
2. modify the file in the path: /app/v1/settings/settings.cfg and change the values of the database
3. execute the file in the path /app/v1/model/create_db.py to create the tables in the database
4. to run the project you could run directly in the terminal: python app.py or you could also use the following command: uvicorn main:app --host 0.0.0.0.0 --port 8000
5. to test the functionality of the project we would make use of the Swagger UI in the path {host}:{port}/docs this UI will allow us to see the api documentation and test all the endpoints


Español:

Para la solucion del reto he decidido usar el framework FastAPI para el desarrollo de la api
junto con PostgreSQL como motor de base de datos y el ORM sqlmodel.

todas las librerias usadas en el proyecto estan añadidas en el requirements.txt

pasos para correr el proyecto en local:
1. Instalar las librerias en el terminal: pip install -r requirements.txt
2. modificar el acrhivo en la ruta: /app/v1/settings/settings.cfg y cambiar los valores de la base de datos
3. ejecutar el archivo en la ruta /app/v1/model/create_db.py para crear las tablas en la base de datos
4. para correr el proyecto se podria ejecutar directamente en el terminal: python app.py o tambien se podria usar el siguiente comando: uvicorn main:app --host 0.0.0.0 --port 8000
5. para probar la funcionalidad del proyecto se haria uso de la Swagger UI en la ruta {host}:{port}/docs esta UI nos permitira ver la documentacion de la api y probar todos los endpoints

