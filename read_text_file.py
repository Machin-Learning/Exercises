def read_text_file(word):
    f = open('input.txt','r')
    l = f.readlines()
    ls = []
    for line in l:
        ls.append(line.count(word))
    count = sum(ls)
    return (count)

print(read_text_file('And'))

# from csv import DictReader



# with open('input.csv') as csvfile:
#     csvreader = DictReader(csvfile)
#     for row in csvreader:
#         # process a row from the CSV file