import Comparison, csv

def exe(_id):
    match_id = open('_id_data.csv', 'r')
    reader = csv.reader(match_id)
    for i in reader:
        if _id == i[0]:
            madia = i[2]
            break
    match_id.close()

    if 'asahi' == madia:
        Extraction='asahi_match_record.csv'
        Object_csv1='mainichi_match_record.csv'
        Object_csv2='yomiuri_match_record.csv'
    elif 'mainichi' == madia:
        Extraction='mainichi_match_record.csv'
        Object_csv1='asahi_match_record.csv'
        Object_csv2='yomiuri_match_record.csv'
    elif 'yomiuri' == madia:
        Extraction='yomiuri_match_record.csv'
        Object_csv1='asahi_match_record.csv'
        Object_csv2='mainichi_match_record.csv'

    _id1, rate1 = Comparison.comparison(_id, Extraction, Object_csv1)
    _id2, rate2 = Comparison.comparison(_id, Extraction, Object_csv2)

    return _id1, rate1, _id2, rate2

def exe_information(id):
    result_value = []
    db = open('_id_match.csv', 'r')
    reader = csv.reader(db)
    for i in reader:
        if id == i[0]:
            result_value.append(i[1])
            result_value.append(i[2])
            result_value.append(i[3])
            result_value.append(i[4])
    db.close()
    return result_value