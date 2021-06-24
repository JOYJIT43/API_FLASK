# from os import name
from flask import Flask, request, jsonify
from product_service import ProductService

app=Flask(__name__)


if __name__ == "__main__":
   app.run(debug=True)

service = ProductService()


@app.after_request
def add_headers(response):
    
    response.headers['Access-Control-Allow-Origin']= '*'
    response.headers['Access-Control-Allow-Headers']='Content-Type , Access-Control-Allow-Headers,Authorization'
    response.headers['Access-Control-Allow-Methods']  ='GET,POST,PUT,DELETE,OPTIONS'
    return response


@app.route('/',methods=['GET'])
def welcome():
    return "WELCOME"

@app.route('/products',methods=['GET'])
def get_all_products():
    return jsonify(service.read_all())


@app.route('/products/<p_id>',methods=['GET'])
def get_one_product(p_id):
    return jsonify(service.read_one(p_id))


@app.route('/products',methods=['POST'])
def save_product():
    return jsonify(service.create(request.form))


@app.route('/products/<p_id>',methods=['PUT','PATCH'])
def modify_product(p_id):
    return jsonify(service.update(p_id, request.form))


@app.route('/products/<p_id>',methods=['DELETE'])
def delete_product(p_id):
    return jsonify(service.delete(p_id))














   
    
