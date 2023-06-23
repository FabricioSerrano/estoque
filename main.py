from flask import Flask, jsonify, request
from database.database import Database


app = Flask(__name__)
database = Database()


# routes
@app.route('/products/registered', methods=['GET'])
def get_registered_products() -> list[tuple]:
    return jsonify(database.return_registered_products())


@app.route('/products/insert', methods=['POST'])
def register_product() -> None:

    args = request.args

    database.register_product(
        args.get('product'), 
        args.get('brand'),
        args.get('user')
    )

    return jsonify({"status" : "ok"})




if __name__ == '__main__':
    app.run(debug=True)