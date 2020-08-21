import requests
import time
from bs4 import BeautifulSoup

def to_fixed(numObj, digits=2):
    return f'{numObj:.{digits}f}'

def remaining_time(anime_num, delay_time):
    remaining_time_minutes = int(((anime_num / 50) * delay_time) / 60)
    remaining_time_seconds = int(((anime_num / 50) * delay_time) % 60)
    return f'Time remaining: {remaining_time_minutes} Minutes, {remaining_time_seconds} seconds'

def parse():

    file = open('anime_list.txt', 'w', encoding='utf-8')

    site_anime_num = 10500
    parsing_percent = 0
    request_time = 7

    remaining_time(site_anime_num, request_time)

    for page in range(0, site_anime_num, 50):

        parsing_percent = ((page + 50) / site_anime_num) * 100
        print(f'Progress: {to_fixed(parsing_percent)}%')
        
        time.sleep(request_time) # Delay

        link = f'https://myanimelist.net/topanime.php?limit={page}'

        response = requests.get(link)

        bs = BeautifulSoup(response.text, 'lxml')

        temp_title = bs.find_all('a', class_='hoverinfo_trigger fl-l fs14 fw-b')
        temp_score = bs.find_all('div', class_='js-top-ranking-score-col di-ib al')
        temp_link = bs.find_all('a', class_='hoverinfo_trigger fl-l ml12 mr8', href=True)

        for i in range(len(temp_title)):
            file.write(f'{i + 1 + page} | {temp_title[i].text} | {temp_score[i].text} | {temp_link[i]["href"]}\n')
        
    file.close()
    