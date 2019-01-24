import urllib.request

def download():
    url = "https://goo.gl/1kw79Y"
    file_list = ['_id_data.csv', 'asahi_match_record.csv','yomiuri_match_record.csv','mainichi_match_record.csv']

    for file in file_list:
        urllib.request.urlretrieve(url, file)
    return "保存しました"