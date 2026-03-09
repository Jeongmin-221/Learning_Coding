import requests

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://news.naver.com/'
site = requests.get(url, headers=header_info)
html_data = site.text

pos1 = html_data.find('<div class="main_brick_item _channel_main_news_card_wrapper">')
html_data = html_data[pos1:]
pos2 = html_data.find('<div class="main_brick_item _horizontal_card_wrapper _horizontal_scroll_type">')
html_data = html_data[:pos2]

count = html_data.count('a href="')

for i in range(count):
    artic_pos = html_data.find('a href="')+len('a href="')
    html_data = html_data[artic_pos:]
    artic_pos2 = html_data.find('"')
    link = html_data[:artic_pos2]
    
    url = link
    site = requests.get(url, headers=header_info)
    content_html_data = site.text

    title_pos1 = content_html_data.find("<title>")+len("<title>")
    title_pos2 = content_html_data.find("</title>")
    title = content_html_data[title_pos1:title_pos2]
    
    article_pos = content_html_data.find('<article id="dic_area" class="go_trans _article_content">')+len('<article id="dic_area" class="go_trans _article_content">')
    article = content_html_data[article_pos:]
    article_pos2 = article.find('</article>')
    article = article[:article_pos2]

    img_artic = article
    count = img_artic.count('data-src="')
    img_link = []
    for i in range(count):
        img_pos = img_artic.find('data-src="')+len('data-src="')
        img_artic = article[img_pos:]
        img_endpos = img_artic.find('?')
        img_link.append(img_artic[:img_endpos])
        img_artic = img_artic[img_endpos:]


    content = ""
    while True:
        pos1 = article.find(">")+1
        if not pos1:
            break

        article = article[pos1:]
        pos2 = article.find("<")
        content = content + article[:pos2].strip() + "\n"
        article = article[pos2+1:]

    try:
            file_name = f'{title}.txt'
            ss = content.encode('utf-8')
            file = open(file_name, 'wb')
            file.write(ss)
            file.close()
            
            for j in range(count):
                file_name = f'{title}{j+1}.{img_link[j][-3]}'
                ss = requests.get(img_link[j], headers=header_info)
                file = open(file_name, 'wb')
                file.write(ss)
                file.close()
    except Exception as e:
            print('에러 발생', e)

    
    html_data = html_data[artic_pos2+1:]
