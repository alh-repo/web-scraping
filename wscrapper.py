#! /usr/bin/env python

# Adam Hennefer
# Webscraping introduction
# 11.24.2020

# to run: $ ./wscrapper.py
#   or
# to run: $ python wscrapper.py
#
# May need to install the following modules, displayed here with commands:
# 	pip3 install requests
# 	pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL = 'https://www.espn.com/nfl/game?gameId=401220335'
page = requests.get(URL)

#print(page.content)
#with open("crawlput.html", "w") as f:
#  f.write(str(page.content))

soup = BeautifulSoup(page.content, 'html.parser')

score1 = soup.find(class_='score icon-font-after')
score2 = soup.find(class_='score icon-font-before')
visitor = soup.find(class_='short-name')
home = soup.find(class_='team home')

#scores = soup.find_all(class_='short-name')
#for team in scores:
#	print(team.text)

for elm in home.select(".short-name"):
	hometeam = elm.text
	#print(elm.text)
	
if int(score1.text) > int(score2.text): 
	winner = visitor.text
	winScore = score1
	loser = hometeam
	loseScore = score2
else: 
	winner = hometeam
	winScore = score2
	loser = visitor.text
	loseScore = score2

print(winner+" "+str(winScore.text)+" -W")
print(loser+" "+str(loseScore.text)+" -L")



