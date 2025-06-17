import os

application_absolute_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    # Busca um arquivo na estrutura de arquivos contendo a chave secreta
    # Utilizamos 'you-will-never-guess' para ambiente de desenvolvimento
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess.'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    # Endereço para o banco de dados
    MONGODB_DATABASE_URI = 'mongodb+srv://joaosumi:BsnQ3CwAUPGXEI25@database-n3.aozyrxl.mongodb.net/'
    DATABASE_NAME = "n3"