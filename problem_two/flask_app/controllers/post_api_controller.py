from .parser_controller import ParserController
import settings

class PostController(ParserController):
    def __init__(self):
        super().__init__()
        self.excel_file = settings.EXCEL_FILE

    def input_list_parser(self, input_data):
        columns = self.read_excel()[1]
        for obj in input_data:
            if obj not in columns :
                raise ValueError(f'{obj} name is incorrect')
        return input_data

    def parse_request(self):
        self.reqparse.add_argument('input_data', type=self.input_list_parser, required=True, action='append')
        args = self.reqparse.parse_args()
        return args['input_data']

    def handle_request(self):
        input_data = self.parse_request()
        excel_output = self.read_excel()
        data_frames = excel_output[0]
        for i in range(0, len(input_data)):
            data_frames = data_frames.append(input_data[i], ignore_index=True)
        data_frames.drop_duplicates(subset=None, keep="last", inplace=True)
        data_frames.to_excel(self.excel_file, index=False)
        return {'msg': 'row is added successfully'}
    