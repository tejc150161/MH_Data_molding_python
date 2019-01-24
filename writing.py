import csv

def match_db(record, media):
    if 'asahi' == media:
        csv_name = 'asahi_match_record.csv'
    elif 'yomiuri' == media:
        csv_name = 'yomiuri_match_record.csv'
    elif 'mainichi' == media:
        csv_name = 'mainichi_match_record.csv'
    db = open(csv_name, 'a')
    db_cav = csv.writer(db, lineterminator='\n')
    db_cav.writerow(record)
    db.close()
    return 'complete'

def _id_db(id_data):
    db = open('_id_data.csv', 'a')
    db_cav = csv.writer(db, lineterminator='\n')
    db_cav.writerow(id_data)
    db.close()
    return 'complete'