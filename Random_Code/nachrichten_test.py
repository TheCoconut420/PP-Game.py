import requests
from bs4 import BeautifulSoup

url_page = "https://www.espn.com/golf/leaderboard/_/tournamentId/401056502"
page = requests.get(url_page)
soup = BeautifulSoup(page.text, 'html.parser')

table_with_namelist = soup.select_one('table:has(a.leaderboard_player_name)')

for a in table_with_namelist.select('.leaderboard_player_name'):
    print(a.text)