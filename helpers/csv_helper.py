import csv

class CsvHelper:

    def read_csv(self, file_path):
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)

        