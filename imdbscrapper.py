from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/find?s=tt&q=Titanic')
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('tr', class_='findResult odd').a
    flag=0
    title= ""
    movie = str(movies)
    tag = movie.split('/')[2]
    
except Exception as e:
    print('There was a problem: {}'.format(e))