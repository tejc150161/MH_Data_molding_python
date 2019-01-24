import bs4, requests
from janome.tokenizer import Tokenizer

def exe(url):
    get_url = requests.get(url)
    soup = bs4.BeautifulSoup(get_url.text,"html.parser")
    text = ""

    title = soup.find("h1").string
    title = ''.join(title.split()).encode('utf-8')

    if 'asahi' in url:
        for div in soup.find_all('div', class_="ArticleText"):
            for text_component in div.find_all('p', limit=3):
                text_component = text_component.string
                text = text + str(text_component.encode('utf-8'))
    
    elif 'mainichi' in url:
        for text_component in soup.find_all("p", class_="txt", limit=4):
            text_component = text_component.string
            text = text + str(text_component.encode('utf-8'))
        text = ''.join(text.split())

    elif 'yomiuri' in url:
        for div in soup.find_all('article'):
            for text_component in div.find_all('p', limit=4):
                text_component = text_component.string
                text = text + str(text_component.encode('utf-8'))
    data = title + text

    analysis_data = []
    t=Tokenizer()
    j_txt = t.tokenize(unicode(data, 'utf-8'))
    for i in j_txt:
        partOfSpeech = i.part_of_speech.split(',')[0]
        if partOfSpeech == u'名詞':
            analysis_data.append(i.surface)
    keywords = list(set(analysis_data))

    return keywords