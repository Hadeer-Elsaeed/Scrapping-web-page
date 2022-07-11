from .parser_controller import ParserController
import pandas as pd
import settings

class DeleteController(ParserController):
    def __init__(self):
        super().__init__()
        self.excel_file = settings.EXCEL_FILE
    
    def parse_request(self):
        self.reqparse.add_argument('row', type=int, default='1')
        args = self.reqparse.parse_args()
        return args['row']

    def handle_request(self):
        row = self.parse_request()
        data_frames = self.read_excel()[0]
        try:
            data_frames = data_frames.drop(row)
            data_frames.to_excel(self.excel_file, index=False)
            return {'msg': 'row is deleted successfully'}
        except KeyError as e :
            return {'error': "This row doesn't exist"}
        