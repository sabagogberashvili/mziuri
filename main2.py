# giorgi kiknadze
from bs4 import BeautifulSoup
import requests
import csv

# listi romelic sheicavs csv filies xazebis saxelebs
column_names = ['Entry Number', 'Name', 'Year', 'Game Price', 'Platform', 'Total Votes']

# xsnis main.csv fails to ar arsebobs qmnis
with open('main.csv', 'a', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(column_names)

# qmnis headers romelic mibadzavs web broswings
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

# gzavnis mititebul saitze motxovnas rom html content amoiros am yvelafristvis beautifulsoups iyenebs.
    site = requests.get('https://steam250.com/top250', headers=headers).text
    soup = BeautifulSoup(site, 'html.parser')
    games = soup.find_all('div', class_="appline")
    c = 1

# poulobs yvela html elements romelic aris class applineshi romelic saitze individualur tamashebs asaxavs.
# aseve yvela tamasidan amoirebs relevantur informacias rogoricaa name, date, price, content tags, platform information.
    for game in games:
        name = game.find('span', class_="title").text.split('. ')[1:]
        name = "{}".format(*name)
        game_date = game.find('span', class_="date").text if game.find('span', class_="date") else ""
        game_price = game.find('span', class_="price").text if game.find('span', class_="price") else "?????"
        game_content = game.find('a', class_="g2 tag").text if game.find('a', class_="g2 tag") else "N/A"
        game_platform = game.find('span', class_="platform")
        mac = game.find('a', class_="mac")
        win = game.find('a', class_="win")
        deck = game.find('a', class_="deck")

#saba gogberashvili

        platforms = []
        if mac and win and deck:
            platforms.append("Mac, Win, Deck")
        elif mac and win:
            platforms.append("Mac, Win")
        elif mac and deck:
            platforms.append("Mac, Deck")
        elif win and deck:
            platforms.append("Win, Deck")
        elif mac:
            platforms.append("Mac")
        elif win:
            platforms.append("Win")
        elif deck:
            platforms.append("Deck")
        else:
            platforms.append("N/A")#პლატფორმის განსაზღვრა

        total_votes_tag = game.find('div', class_="totalVotes")
        total_votes = total_votes_tag.find('span', class_="votes").text if total_votes_tag else "N/A" #მთლიანი ხმების ამოღება

        entry_number = c
        c += 1
        entry_data = [entry_number, name, game_date, game_price, game_content] #შესვლის მონაცემების სია

        game_platform = ', '.join(platforms) if platforms else 'N/A'
        entry_data.append(game_platform)

        entry_data.append(total_votes)#ამატებს მთლიან vote ბს

        # Write entry data to the CSV file
        with open('main.csv', 'a', encoding='utf-8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(entry_data)#წერს მონაცემებს CSV ფაილში
