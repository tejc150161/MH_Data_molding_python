# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json, os, exe_Comparison, exe_Extraction, MH_google_drive_connection, writing

#-----一致率計算は「simpson係数」を使用-----

app = Flask(__name__)

@app.route('/test')
def index():
    return 'test'

@app.route('/display')
def display():
    drive = MH_google_drive_connection.Authentication()
    status = MH_google_drive_connection.display(drive)
    return status

@app.route('/upload')
def up():
    drive = MH_google_drive_connection.Authentication()
    status = MH_google_drive_connection.delete(drive)
    status = MH_google_drive_connection.upload(drive)
    return status

@app.route('/delete')
def de():
    #drive = MH_google_drive_connection.Authentication()
    #status = MH_google_drive_connection.delete(drive)
    #return status
    return "コメントアウト"

@app.route('/import')
def do():
    drive = MH_google_drive_connection.Authentication()
    status = MH_google_drive_connection.download(drive)
    return status

@app.route('/', methods=['POST'])
def post_connect():
    data = request.json
    response_json = {}
    if 'url' in data :
        url = data['url']
        check_data = exe_Extraction.exe(url)
        return jsonify({'results':check_data})
    elif '_id' in data:
        record = []
        id_data = []
        record2 = []
        record.append(data['_id'])
        id_data.append(data['_id'])
        if 'distribution_date' in data:
            id_data.append(data['distribution_date'])
            if 'media' in data:
                id_data.append(data['media'])
                if 'results'in data:
                    record.append(data['results'])
                    status = writing.match_db(record, data['media'])
                    if status != "media_error":
                        writing._id_db(id_data)
                else:
                    status = 'results'
            else:
                status = 'media_error'
            _id1,rate1,_id2,rate2 = exe_Comparison.exe(data['_id'])
            record2.append(data['_id'])
            record2.append(_id1)
            record2.append(rate1)
            record2.append(_id2)
            record2.append(rate2)
            writing.match_id(record2)
            return status
        else:
            information_result = exe_Comparison.exe_information(data['_id'])
            return jsonify({'_id1':information_result[0],'rate1':information_result[1],'_id2':information_result[2],'rate2':information_result[3]})
    else:
        return 'request_data_error'

port = int(os.getenv('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)