import requests
from bs4 import BeautifulSoup

urlOne = 'https://www.nytimes.com/2023/05/01/us/politics/debt-limit-date-janet-yellen.html'
urlTwo = 'https://www.nytimes.com/2023/05/01/business/first-republics-regional-banks-crisis.html'
urlThree = 'https://www.nytimes.com/2023/05/01/business/first-republic-bank-jpmorgan.html'
urlFour = 'https://www.nytimes.com/2023/05/01/us/politics/prison-guards-teachers-staff.html'
urlFive = 'https://www.nytimes.com/2023/05/01/opinion/biden-trump-harris-2024.html'

responseOne = requests.get(urlOne)
responseTwo = requests.get(urlTwo)
responseThree = requests.get(urlThree)
responseFour = requests.get(urlFour)
responseFive = requests.get(urlFive)

soupOne = BeautifulSoup(responseOne.content, 'html.parser')
soupTwo = BeautifulSoup(responseTwo.content, 'html.parser')
soupThree = BeautifulSoup(responseThree.content, 'html.parser')
soupFour = BeautifulSoup(responseFour.content, 'html.parser')
soupFive = BeautifulSoup(responseFive.content, 'html.parser')

print(soupOne.find('body').get_text())

#Challenge 39
'''
Write a Python program that scrapes the title and description
of the first five articles on the homepage of the New York Times (https://www.nytimes.com/)
and prints them out.
Use the requests and BeautifulSoup libraries to perform the scraping.
You can use any regular expression techniques you have learned to clean up the text if needed.
'''

#This challenge required the installation of "beautifulsoup4"
#pip install beautifulsoup4

#NY TIMES doesn't work. Fun module tho.