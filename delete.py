# -*- coding: utf-8 -*-
import csv
from datetime import datetime, date, timedelta


def d_record():
    two_days_ago = datetime.today() - timedelta(days=2)#二日前
    data = '_id_data.csv'
    csv_list = ['asahi_match_record.csv','yomiuri_match_record.csv','mainichi_match_record.csv']

    f = open(data, 'r')
    reder = csv.reder(f)
    for i in reder:
        if i[1] <= two_days_ago:
            #各社のcsvファイル内にある対象IDを探す
            for j in csv_list:
                o = open(j, 'r+')
                reder2 = csv.reder(o)
                for r in reder2:
                    if r == i[0]:
                        j.pop(i)
    f.close()



#https://code.i-harness.com/ja-jp/q/47deb3