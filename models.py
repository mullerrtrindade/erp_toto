from sqlalchemy import create_engine, column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
## Engine do banco de dados SQLite
db= create_engine("sqlite:///./erp_toto.db")

## Base para as classes de modelo
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

## Classes de tabela para o banco de dados

class Usuario(Base): 
    __tablename__ = "usuarios"
    id = column("id",Integer, primary_key=True, index=True, autho_increment=True)
    nome = column("nome",String, index=True)
    email = column("email",String, unique=True, index=True, nullable=False)
    senha = column("senha",String, nullable=False)
    admin = column("admin",Boolean, default=False)
    ativo = column("ativo",Boolean, default=True)

def __init__(self, nome:str, email:str, senha:str, admin:bool=False, ativo:bool=True):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.admin = admin
    self.ativo = ativo


# administrador
# clientes_string
# estoque



# Executa a função de metadados para criar as tabelas no banco de dados

