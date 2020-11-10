import csv

def file():
    with open('test.tsv', mode='r', newline='') as in_file, \
            open('SB-10k.tsv', mode='w', newline='') as out_file:
        b = csv.reader(in_file, delimiter='\t')
        a = csv.writer(out_file, delimiter='\t')
        a.writerow(['tweet', 'sentiment'])
        for line in b:
            a.writerow(line)

file()