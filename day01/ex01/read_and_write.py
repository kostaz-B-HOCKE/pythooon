#!/Users/eabradol/42/python/pythooon/day01/ex01

def read_and_write(filename):
    # dir_way = 'pythooon/day01/ex01/'
    dir_way = ""
    file_csv = open(dir_way+filename+'.csv', 'r')
    file_tsv = open(dir_way+filename+'.tsv', 'w')
    file_tsv.write(file_csv.read().replace(',\"', '\t\"').replace('\",', '\"\t'))
    file_csv.close()
    file_tsv.close()

if __name__ == '__main__':
    read_and_write('ds')
