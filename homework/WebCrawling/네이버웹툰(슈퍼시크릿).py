import requests
import time

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

#마지막화 140화(후에 에필로그 더 있음)
url = 'https://comic.naver.com/webtoon/detail?titleId=650304&no=1'
site = requests.get(url, headers=header_info)
html_data = site.text

name_pos1 = html_data.find('titleName: "')+len('titleName: "')
tmp_html_data = html_data[name_pos1:]
name_pos2 = tmp_html_data.find('"')
name = tmp_html_data[:name_pos2]
print(name)

for i in range(140):
    url = url[:-len(str(i+1))]+str(i+1)
    site = requests.get(url, headers=header_info)
    html_data = site.text

    img_pos = html_data.find('div class="view_area"')+len('div class="view_area"')
    html_data = html_data[img_pos:]
    img_end_pos = html_data.find('</div>')
    html_data = html_data[:img_end_pos]
    imgurl = []

    count = html_data.count('img src=')

    for j in range(count):
        pos1 = html_data.find('img src="')+len('img src="')
        html_data = html_data[pos1:]
        pos2 = html_data.find('"')
        extract_data = html_data[:pos2]
        html_data = html_data[pos2+1:]
        imgurl.append(extract_data)
    
        try:
             file_name = f'{name}{i+1}_{j+1}.{extract_data[-3:]}'
             ss = requests.get(extract_data, headers=header_info)
             print(extract_data)
             file = open(file_name, 'wb')
             file.write(ss.content)
             file.close()
        except Exception as e:
            print('에러 발생', e)


        time.sleep(2)

