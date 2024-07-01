import csv
from parse_data import parse_data

def read_file(filename):
    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)
        data = parse_data(csvFile)
        return data