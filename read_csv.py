from csv import DictReader

def read_csv():
    dictionary = {}
    with open('input.csv') as csvfile:
        csvreader = DictReader(csvfile)
        for row in csvreader:
            dictionary.update(row)
        
    return (dictionary.keys())


print(read_csv())