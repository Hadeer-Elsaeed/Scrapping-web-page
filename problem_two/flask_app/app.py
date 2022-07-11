from flask import Flask
from flask_restful import Api
from resources.process_excel_file import RestExcel

app = Flask(__name__)
api = Api(app)

api.add_resource(RestExcel, '/process_excel')

if __name__ == '__main_ _':
    app.run(host="0.0.0.0", debug=True)
