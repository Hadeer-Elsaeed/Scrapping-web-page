from ast import arg
from .parser_controller import ParserController
import pandas as pd

class GetController(ParserController):
    def __init__(self):
        super().__init__()
    
    def parse_request(self):
        self.reqparse.add_argument('row', type=int, location='args', default='1')
        args = self.reqparse.parse_args()
        return args['row']

    def handle_request(self):
        row = self.parse_request()
        excel_output = self.read_excel()
        data_frames = excel_output[0]
        columns = excel_output[1]
        data = data_frames.to_dict()
        obj = {}
        try:
            for i in range(0, len(columns)):
                obj[columns[i]] = data[columns[i]][row]
            return data if not row else obj
        except KeyError:
            return data
        