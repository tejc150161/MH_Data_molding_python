import Comparison, csv

def exe(_id):
    match_id = open('_id_data.csv', 'r')
    reder = csv.reder(match_id)
    for i in reder:
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