# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json, os, delete, download, exe_Comparison, exe_Extraction, writing

#-----一致率計算は「simpson係数」を使用-----

app = Flask(__name__)

@app.route('/test')
def index():
    return 'test'

@app.route('/download')
def dl():
    status = download.download()
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
            return status
        else:
            _id1,rate1,_id2,rate2 = exe_Comparison.exe(data['_id'])
            return jsonify({'_id1':_id1,'rate1':rate1,'_id2':_id2,'rate2':rate2})
    else:
        return 'request_data_error'

port = int(os.getenv('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)