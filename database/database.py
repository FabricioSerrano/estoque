import pyodbc
import pandas as pd
from database import return_cursor

class Database:
    def __init__(self) -> None:
        
        self.schema = 'estoque'

        self.cursor = return_cursor()

        if type(self.cursor) in (Exception, pyodbc.Error):
            raise ConnectionError('Erro de conexão com o banco de dados')
        

    def return_registered_products(self) -> dict:
        
        return {"data" : [tuple(row) for row in self.cursor.execute('call s_Retorna_Produtos_Cadastrados();').fetchall()]}


    def register_product(self, name : str, brand : str, user : str) -> None:

        self.cursor.execute(f'''call s_Cadastra_Produto('{name}', '{brand}', '{user}');''')
