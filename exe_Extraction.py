# -*- coding: utf-8 -*-
import bs4, requests
from janome.tokenizer import Tokenizer

#URL先データ抽出関数
def exe(url):
    #Web情報を取得
    get_url = requests.get(url)
    soup = bs4.BeautifulSoup(get_url.text,"html.parser")
    text = ""

    #タイトル　見出しタグ　3社とも <h1>
    title = soup.find("h1").string
    title = ''.join(title.split()).encode('utf-8')

    #本文内容取得
    if 'asahi' in url: #朝日新聞
        for div in soup.find_all('div', class_="ArticleText"):
            for text_component in div.find_all('p', limit=3):
                text_component = text_component.string
                text = text + str(text_component.encode('utf-8'))
    
    elif 'mainichi' in url: #毎日新聞
        for text_component in soup.find_all("p", class_="txt", limit=4):
            text_component = text_component.string
            text = text + str(text_component.encode('utf-8'))
        text = ''.join(text.split())

    elif 'yomiuri' in url: #読売新聞
        for div in soup.find_all('article'):
            for text_component in div.find_all('p', limit=4):
                text_component = text_component.string
                text = text + str(text_component.encode('utf-8'))
    data = title + text

    #analysis_janome
    analysis_data = []
    t=Tokenizer()
#    j_txt = t.tokenize(data)
    j_txt = t.tokenize(unicode(data, 'utf-8'))
    for i in j_txt:
        partOfSpeech = i.part_of_speech.split(',')[0]
        if partOfSpeech == u'名詞':
            analysis_data.append(i.surface)
    keywords = list(set(analysis_data))

    return keywords