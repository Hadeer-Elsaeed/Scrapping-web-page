from .parser_controller import ParserController
import settings
import pandas as pd

class PutController(ParserController):
    def __init__(self):
        super().__init__()
        self.excel_file = settings.EXCEL_FILE

    def parse_request(self):
        self.reqparse.add_argument('row', type=int)
        columns = self.read_excel()[1]
        for i in range(0, len(columns)):
                self.reqparse.add_argument(
                columns[i],
                location=['json']
            )
        args = self.reqparse.parse_args()
        return args

    def handle_request(self):
        args = self.parse_request()
        row = args['row']
        data_frames = self.read_excel()[0]
        data_frames.iloc[(data_frames.index == row).argmax()] = args
        data_frames.to_excel(self.excel_file, index=False)
        return {'msg': 'row is updated successfully'}
    