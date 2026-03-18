import requests
import pymysql
import time

except_char = '\\//:*?"<>|<>'


def upload_to_azure(title, content, news_url, img_link):

    conn = pymysql.connect(
        host='',
        user='',
        password='',
        db='',
        charset='utf8mb4',
        use_unicode = True
    )

    try:
        with conn.cursor() as cursor:
            sql_art = "INSERT INTO news_articles (title, content, url) VALUES (%s, %s, %s)"
            cursor.execute(sql_art, (title, content, news_url))

            article_id = conn.insert_id()

            if img_link:
                sql_img = "INSERT INTO article_images (article_id, image_url) VALUES (%s, %s)"
                for url in img_link:
                    cursor.execute(sql_img, (article_id, url))

            conn.commit()
            print(f"성공: [{title}] 업로드 완료 (ID: {article_id})")

    except Exception as e:
        print(f"DB 에러 발생: {e}")
        conn.rollback()
    finally:
        conn.close()

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

    if 'press' in link:
        continue
    
    url = link
    site = requests.get(url, headers=header_info)
    content_html_data = site.text

    title_pos1 = content_html_data.find("<title>")+len("<title>")
    content_html_data = content_html_data[title_pos1:]
    title_pos2 = content_html_data.find("</title>")
    tmp_title = content_html_data[:title_pos2]
    title = ""
    for i in tmp_title:
        if i not in except_char:
            title += i
    
    article_pos = content_html_data.find('<article id="dic_area" class="go_trans _article_content">')+len('<article id="dic_area" class="go_trans _article_content">')
    article = content_html_data[article_pos:]
    article_pos2 = article.find('</article>')
    article = article[:article_pos2]
    
    img_artic = article
    count = img_artic.count('" data-src="')
    img_link = []
    for i in range(count):
        img_pos = img_artic.find('<img id="')+len('<img id="')
        if img_pos == -1:
            continue
        img_artic = img_artic[img_pos:]
        img_pos = img_artic.find(' data-src="')+len(' data-src="')
        img_artic = img_artic[img_pos:]
        img_endpos = img_artic.find('?')
        result = img_artic[:img_endpos]
        if "http" not in result:
            img_artic = img_artic[img_endpos+1:]
            continue
        img_link.append(result)
        img_artic = img_artic[img_endpos+1:]


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

        news_data = {
            'title': title,
            'content': content,
            'url': link
        }

        image_list = img_link


        upload_to_azure(title, content, link, img_link)

    except Exception as e:
        print('에러 발생:', e)
        input()

    
    html_data = html_data[artic_pos2+1:]
    time.sleep(1)
