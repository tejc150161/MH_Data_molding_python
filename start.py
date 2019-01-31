# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from decimal import Decimal
import csv, json, os, exe_Comparison, exe_Extraction, MH_google_drive_connection, writing

#-----一致率計算は「simpson係数」を使用-----
app = Flask(__name__)
@app.route('/upload')
def up():
    drive = MH_google_drive_connection.Authentication()
    status = MH_google_drive_connection.upload(drive)
    return status
#@app.route('/delete')
#def de():
#    drive = MH_google_drive_connection.Authentication()
#    status = MH_google_drive_connection.delete(drive)
#    return status
#    return "コメントアウト"
#@app.route('/import')
#def do():
#    drive = MH_google_drive_connection.Authentication()
#    status = MH_google_drive_connection.download(drive)
#    return status
@app.route('/', methods=['POST'])
def post_connect():
    data = request.json
    #response_json = {}
    if 'url' in data : #受け取ったURLを形態素解析・返却
        url = data['url']
        check_data = exe_Extraction.exe(url)
        return jsonify({'results':check_data})

    elif '_id' in data:
        _id = data['_id']
        id_data = [] #ID管理
        if 'results' in data:
            results = data['results']
            record = [_id, results] #ID,　形態素解析＋NLUデータリスト　格納
            if 'media' in data:
                status = writing.match_db(record, data['media']) #recordに格納されているデータ登録
                if 'distribution_date' in data:
                    distribution_date = data['distribution_date']
                    media = data['media']
                    id_data = [_id, media, distribution_date] #ID, メディア, 日付　格納
                    status = writing._id_db(id_data) #id_dataに格納されているデータ登録
                    #対象のIDと他社の記事から一致率を求め各社値の高いものを登録
                    _id1,rate1,_id2,rate2 = exe_Comparison.exe(_id)
                    record2 = [_id, _id1, rate1, _id2, rate2]
                    status = writing.match_id(record2)
                else:
                    status = 'distribution_date'
            else:
                status = 'media_error'
            return status
        else: #一致率リクエスト処理
            information_result = exe_Comparison.exe_information(_id)
            if '-----' == information_result[1]:
                return jsonify({'_id1':information_result[1],'rate1':information_result[2],'_id2':"",'rate2':'0'})
                #return jsonify({'_id1':information_result[2],'rate1':float(information_result[3]),'_id2':"",'rate2':float(0)})
            if '-----' == information_result[3]:
                return jsonify({'_id1':information_result[0],'rate1':information_result[1],'_id2':"",'rate2':'0'})
                #return jsonify({'_id1':information_result[0],'rate1':float(information_result[1]),'_id2':"",'rate2':float(0)})
            if '-----' != information_result[1] and '-----' != information_result[3]:
                return jsonify({'_id1':information_result[0],'rate1':float(information_result[1]),'_id2':information_result[2],'rate2':float(information_result[3])})
                #return jsonify({'_id1':information_result[0],'rate1':float(information_result[1]),'_id2':information_result[2],'rate2':float(information_result[3])})
        return 'request_data_error'

port = int(os.getenv('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)

    
