    Trabajo practico grupal - PSA 
    Squad 5 - Tribu B - 1C2024

# Desarrollo backend - Area Soporte

## Instalacion de dependencias:

#### Entorno virtual: ([+ info](https://docs.python.org/es/3/library/venv.html)) 

1. Instalar [python 3.12.4](https://www.python.org/)
2. En consola creamos entorno virtual `python3 -m venv backend-env`
3. Activamos el entorno virtual (Windows -> terminal command prompt) `backend-env\Scripts\activate.bat`
4. Instalar las dependencias para el lado desarrollador `pip install -r dev-requirements.txt` , en caso de produccion instalarlas `pip install -r requirements.txt`
<!-- 6. Instalamos Selenium `pip install selenium`  -->

## Documentacion y ejecucion manual
1. Usamos uvicorn para crear servidor local. Ejecutamos `py main.py` o con reload: `uvicorn main:app --reload`

    **FastAPI permite probar la funcionalidad ingresando a [127.0.0.1:8000/docs](127.0.0.1:8000/docs)**



## Tests:
Para mas informacion acerca de [Behave](https://behave.readthedocs.io/en/latest/tutorial/#environmental-controls)
* Correr en terminal `behave tests/features` para ejecutar los tests
* Otra forma es `py test_main.py`
