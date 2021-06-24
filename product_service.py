from product_model import ProductModel


class ProductService:
    def __init__(self):
        self.model = ProductModel()
        
    def read_all(self):
        return self.model.get_all_products()

    def read_one(self,_id):
        return self.model.get_product_by_id(_id)

    def create(self,params):
        return self.model.create_product(params)
    
    def update(self,_id, params):
        return self.model.update_product(_id,params)

    def delete(self,_id):
        return self.model.delete_product(_id)
