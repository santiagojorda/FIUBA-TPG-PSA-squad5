# 💾 Desarrollo backend - Area Soporte
    Trabajo practico grupal - PSA 
    Squad 5 - Tribu B - 1C2024

    Equipo: 👨🏻‍🦱 Santiago Jorda - 102924
            👨🏻‍🦱 Johantan Buraschi - 107633 


## 🔗 Links 
* [Proyecto PSA](https://psa-management-system.onrender.com/)
* [Microservicio Soporte](https://psa-support-microservice.onrender.com/docs)
* [Microservicio Proyectos](https://psa-project-microservice.onrender.com/docs)
> ✳️ **Nota para el usuario:** Al estar hosteados en la plataforma **render** puede ser que tarde en desplegarse tanto los microservicios como el proyecto, esto puede demorarse 1/2 minutos aprox. 

## 📄 Documentacion del proyecto
* [Drive Squad 5](https://drive.google.com/drive/folders/16KUXoImTK2DJhupSf9I3fHXa1O-lUWv8?usp=drive_link)
* [Drive Tribu B](https://drive.google.com/drive/folders/1kk9sMHNTHK2ZDU2OysbkcFmO0dborEGy?usp=drive_link)

## 🔨 Instalacion de dependencias:

#### Entorno virtual: ([+ info](https://docs.python.org/es/3/library/venv.html)) 

1. Instalar [python 3.12.4](https://www.python.org/)
2. En consola creamos entorno virtual `python3 -m venv backend-env`
3. Activamos el entorno virtual (Windows -> terminal command prompt) `backend-env\Scripts\activate.bat`
4. Instalar las dependencias para el lado desarrollador `pip install -r dev-requirements.txt` , en caso de produccion instalarlas `pip install -r requirements.txt`
<!-- 6. Instalamos Selenium `pip install selenium`  -->

## 📖 Documentacion y ejecucion en entorno local
1. Usamos uvicorn para crear servidor local. Ejecutamos `py main.py` o con reload: `uvicorn main:app --reload`

    **FastAPI permite probar la funcionalidad ingresando a [127.0.0.1:8000/docs](127.0.0.1:8000/docs)**



## 💻 Tests:
Para mas informacion acerca de [Behave](https://behave.readthedocs.io/en/latest/tutorial/#environmental-controls)
* Correr en terminal `py test_main.py` para ejecutar los tests
