import sqlite3
from flask.globals import request

from werkzeug.wrappers import Request

class ProductModel():
    def __init__(self):
        self.conn = sqlite3.connect('Product_Management.db',check_same_thread=False)
        self.create_product_table()
        self.conn.row_factory=sqlite3.Row



    
    def __del__(self):

        self.conn.commit()
        self.conn.close()


    def update_product(self,_id,params):
    
        # if request.method == "PUT":

            query = """ UPDATE products SET Name = '{0}', Description = '{1}' , Image ='{2}' WHERE
            Id ={3}""".format(
            params.get('Name'),
            params.get('Description'),
            params.get("Image"),
            _id
            )

            self.conn.execute(query)

            # print("Successfully updated!")

            return self.get_product_by_id(_id)
        
        # elif request.method == "PATCH":
            
        #     query = """ UPDATE products SET Description = '{0}'  WHERE Id ={1}""".format(
        #     params.get('Description'),
        #     _id
        #     )

        #     self.conn.execute(query)

        #     return self.get_product_by_id(_id)




    def get_all_products(self):

        query = "SELECT * FROM products"
        result_set=self.conn.execute(query).fetchall()
        result = [
            {column : row[i] for i,column in enumerate (result_set[0].keys())}
            
            for row in result_set
        ]
        
        return result




    def create_product(self,params):

        query = "INSERT INTO products (Name , Description ,Image) VALUES ('{0}' , '{1}','{2}')".format(

        params.get('Name'),
        params.get('Description'),
        params.get('Image')

        )
        result = self.conn.execute(query)
        return self.get_product_by_id(result.lastrowid)




    def get_product_by_id(self,_id):

        query = "SELECT * FROM products WHERE Id = {0}".format(_id)

        result_set=self.conn.execute(query).fetchall
        result = [
            {column : row[i] for i,column in enumerate (result_set[0].keys())}
            
            for row in result_set
        ]
        return result


    
    def delete_product(self,_id):

        query = "DELETE FROM products WHERE Id = {0}".format(_id)

        res= self.conn.execute(query)

        status = 200 if res.rowcount == 1 else 404

        return {"status": status , "affected_rows":res.rowcount, "message":"Not Found! Nothing to delete"}

        



    def create_product_table(self):
    
        query = """
        CREATE TABLE IF NOT EXISTS "products" (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Description TEXT NOT NULL,
            Image TEXT
        );
        """
        self.conn.execute(query)
    