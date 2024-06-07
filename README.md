# Trabajo practico grupal - PSA - Squad 5 - 1c_2024


## Instalacion de dependencias:

#### Entorno virtual: ([Mas info sobre entornos de python](https://docs.python.org/es/3/library/venv.html)) 

1. Instalar [python 3.12.4](https://www.python.org/)
2. (En caso de no estar creado) En consola creamos entorno virtual `python3 -m venv backend-env`
3. Activamos el entorno virtual (Windows) `backend-env\Scripts\activate.bat`
4. Una vez ingresado al enviroment instalamos FastAPI, Behave y Uvicorn `pip install fastapi behave uvicorn`
<!-- 6. Instalamos Selenium `pip install selenium`  -->

## Documentacion y ejecucion manual
1. Usamos uvicorn para crear servidor local. Ejecutamos `uvicorn main:app --reload`

> FastAPI permite probar la funcionalidad ingresando a [127.0.0.0.1:8000/docs](127.0.0.0.1:8000/docs)



## Tests:
Para mas informacion acerca de [Behave](https://behave.readthedocs.io/en/latest/tutorial/#environmental-controls)
1. Correr en terminal `behave` para ejecutar los tests
