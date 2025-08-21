# Base
from sqlalchemy.ext.declarative import declarative_base

"""
En esta parte se esta aprendiendo que es declaratie_base esto nos retorna una
clase especial que sirve com plantilla que nos permitira construir todas las tablas 
de nuestra base de datos 
--> es como decir create table ____ en este caso en usado atravez de la herencias 
heredando la clase base en automatico lo convierte en una tabla por eso 
es que se sigue la convecion Base para compartir esa variable del script
"""

from sqlalchemy.orm import DeclarativeBase
#PEro en este caso

#Se usa una clase abstracta base con herencia: es similar usar declarativaBase
#solo que esto es base herencia
class Base(DeclarativeBase):
    pass
