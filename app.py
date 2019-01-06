from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item',
                        type=str,
                        required=True,
                        help="cannot be left blank")

    def get(self):
        return {'items': items}

    def post(self):
        data = Item.parser.parse_args()
        items.append(data['item'])
        print("Posting:", data['item'])
        
        return {'items': items}

    def delete(self):
        items = []
        print("Purging")
        print(items)
        return {'items': items}


api.add_resource(Item, '/store')  # http://127.0.0.1:5000/store

if __name__ == '__main__':
    app.run(port=5000, debug=True)
