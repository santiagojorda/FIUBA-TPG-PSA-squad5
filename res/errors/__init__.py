import importlib
import os
import glob

# Obtener la lista de todos los archivos .py en el directorio actual
module_files = glob.glob(os.path.dirname(__file__) + "/*.py")
module_names = [
    os.path.basename(f)[:-3]  # Quita la extensión .py
    for f in module_files
    if os.path.isfile(f) and not f.endswith('__init__.py')
]

# Importar dinámicamente las clases que empiezan con mayúscula
for module_name in module_names:
    if module_name != '__init__':
        module = importlib.import_module('.' + module_name, __package__)
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and name[0].isupper():
                globals()[name] = obj

# Define __all__ para controlar qué nombres se exportan
__all__ = [name for name in module_names if name[0].isupper()]