def comparison(_id, Extraction, file):
    max = 0

    f = open(Extraction,'r')
    reader = csv.reader(f)

    for b in reader:
        if b[0] == _id:
            text_data = b[1]
    f.close()

    f = open(file,'r')
    reader = csv.reader(f)
    for o in reader:
        len1 = len(text_data)
        len2 = len(o[1])
        bond_len = len(set(text_data) & set(data2))
        if len1 <= len2:
            match_rate = bond_len/len1
        else:
            match_rate = bond_len/len2

        if match_rate >= max:
            max_id = o[0]
            max = match_rate
    f.close()

    return _id, match_rate


