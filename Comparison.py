import csv

def comparison(_id, Extraction, file):
    max_id = 'python_test'
    max_match_rate = 0

    f = open(Extraction,'r')
    reader = csv.reader(f)
    for b in reader:
        if b[0] == _id:
            text_data = b[1]
    f.close()

    fo = open(file,'r')
    reader = csv.reader(fo)
    for o in reader:
        len1 = len(text_data)
        len2 = len(o[1])
        bond_len = len(set(text_data) & set(o[1]))
        if len1 <= len2:
            match_rate = bond_len/len1
        else:
            match_rate = bond_len/len2
        if match_rate >= max:
            max_id = o[0]
            max_match_rate = match_rate
    fo.close()

    return max_id, max_match_rate


