from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import Relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instacia de la base para crear la tabla
Base = declarative_base()

#Listado de modelos de la App

#Ususrio
class Usuario(Base):
    __tablename__ = 'usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseñas=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))
    
#Gasto
class Gasto(Base):
    __tablename__ = 'Gastos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(99))
    fotoicono=Column(String(12))

#Categoria
class Categoria (Base):
    __tablename__ =  'Categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria = Column(String(50))
    descripcion=Column(String(99))
    fotoicon = Column(String)

#Metodos de pago
class MetodoPago(Base):
    __tablename__ = 'MetodoPago'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(55))
    descripcion=Column(String(99))

#Facturas
class Factura(Base):
    __tablename__ = 'Factura'
    

