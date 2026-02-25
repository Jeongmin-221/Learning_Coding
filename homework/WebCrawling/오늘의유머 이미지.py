import requests

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url, headers=header_info)
html_data = site.text

count = html_data.count('td class="subject"')



for i in range(count):
    pos1 = html_data.find('td class="subject"')
    html_data = html_data[pos1:]

    pos2 = html_data.find('a href ="')+len('a href ="')
    html_data = html_data[pos2:]

    pos3 = html_data.find('" target')

    title_link = "https://www.todayhumor.co.kr" + html_data[pos2+len('t"><a href="'):pos3] 
    extract_data = html_data[:pos3]
    
    pos4 = html_data.find('target="_top">')+len('target="_top">')
    html_data = html_data[pos4:]

    pos5 = html_data.find('</a>')
    extract_data = html_data[:pos5]

    html_data = html_data[pos2+1:]

    print(i+1, extract_data)

    #순위 내 각 사이트 링크를 타고들어가기
    sub_site = requests.get(title_link, headers=header_info)
    sub_site_data = sub_site.text
    sub_pos1 = sub_site_data.find('<div class="viewContent">')+len('<div class="viewContent">')
    sub_site_data = sub_site_data[sub_pos1:]

    sub_pos1_1 = sub_site_data.find('<!--viewContent-->')
    sub_site_data = sub_site_data[:sub_pos1_1]

    sub_pos2 = 0
    sub_pos3 = 0
    
    #텍스트로만 이루어진 글 골라내기
    if '.jpg' in sub_site_data :
        sub_pos2 = sub_site_data.find('<img src="')+len('<img src="')
        sub_pos3 = sub_site_data.find('.jpg')
        img_site_url = sub_site_data[sub_pos2:sub_pos3+4]
        print(img_site_url)

    else:
        humor_text_data = []
        p_count = sub_site_data.count("<p>")
        print(p_count)
        for a in range(p_count):
             sub_pos_p = sub_site_data.find('<p>')+len('<p>')
             sub_pos_p_end = sub_site_data.find('</p>')
             detail = sub_site_data[sub_pos_p:sub_pos_p_end]
             if '<b>' in detail:
                sub_pos_b = detail.find('<b>')+len('<b>')
                sub_pos_b_end = detail.find('</b>')
                detail = detail[sub_pos_b:sub_pos_b_end]
             humor_text_data.append(detail)
             sub_site_data = sub_site_data[sub_pos_p_end+1:]
             print(detail)
            
    print()
