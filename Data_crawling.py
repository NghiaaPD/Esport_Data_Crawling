import requests
from bs4 import BeautifulSoup
import time

url = 'https://ensiplay.com/teams/lol'
response = requests.get(url)

while True:
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table_data = soup.find('table', class_ = "cq-table teams-table")
        #Extract the rows of the table data
        rows = table_data.find_all('tr')


        for row in rows:
            column = row.find_all('td')
            # print(column)
            if column:
                rank_and_subrank = column[0].text.strip().split('\n')
                new_rank = [x for x in rank_and_subrank if x != '']
                rank = new_rank[0]
                if len(new_rank) > 1:
                    subrank = new_rank[1]
                else:
                    subrank = "None"

                team_name = column[1].text.strip()

                Total_value = column[2].text.strip()

                ENSI_score = column[3].text.strip()

                Country = column[4].text.strip()
                print(Country)

                Winrate_and_Streak = column[5].text.strip().split('\n')
                Winrate = Winrate_and_Streak[0]
                # print(len(Winrate_and_Streak))
                Streak_procesing = [x for x in Winrate_and_Streak[1].split(' ') if x != '' and x != '%' and x != '/']
                if len(Streak_procesing) < 1:
                    Streak = "None"
                else:
                    Streak = Streak_procesing[0]

                Next_match = column[6].text.strip()

                print("TOP 20 ESPORTS TEAM IN THE WORLD\n")
                print(f"Rank:{rank}\
                    \nSub rank: {subrank}\
                    \nTeam name: {team_name}\
                    \nTeam value: {Total_value}\
                    \nENSI score: {ENSI_score}\
                    \nCountry: {Country}\
                    \nWinrate & Streak: {Winrate}% & {Streak}\
                    \nNext match: {Next_match}")

    time.sleep(120)