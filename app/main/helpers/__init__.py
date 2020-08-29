from .csv_helper import CsvHelper
from os.path import abspath

class CsvHelperRunner():
    @staticmethod
    def run():
        print("CSV READ")

        csvHelper = CsvHelper()

        path = abspath('helpers/data.csv')
        data = csvHelper.read_csv(path)

        print(data)
