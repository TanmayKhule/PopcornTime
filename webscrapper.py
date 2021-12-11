import requests
from bs4 import BeautifulSoup as Soup

##################################################### IMDB #####################################################
def IMDB(movie_name_raw):
    movie_name = movie_name_raw.replace(' ', '+')

    imdb_base_url = 'https://www.imdb.com/'
    tag = ''
    try:
        source = requests.get('https://www.imdb.com/find?s=tt&q={}'.format(movie_name))
        source.raise_for_status()
        
        soup = Soup(source.text, 'html.parser')

        movies = soup.find('tr', class_='findResult odd').a
        flag=0
        title= ""
        movie = str(movies)
        tag = movie.split('/')[2]
    
    except Exception as e:
        print('There was a problem: {}'.format(e))

    rev_url = imdb_base_url + "title/" + str(tag) + "/criticreviews/"


    link = requests.get(rev_url)
    movie_soups = Soup(link.text, "html.parser")
    tag = movie_soups.find_all("div", attrs={"class": "summary"})
    i = 0

    summary = "\nIMDB reviews:\n"
    for review in tag:
        i += 1
        summary += "review" + str(i) + ": "
        summary += review.get_text().strip() + "\n" + "\n"

    return summary


##################################################### rottentomatoes #####################################################
def rottenTomatoe(movie_name_raw):
    summary = ""
    movie_name = movie_name_raw.replace(" ", "_")
    movie_name = movie_name.lower()
    rt_url = "https://www.rottentomatoes.com/m/"

    rt_base_url = rt_url + str(movie_name)
    
    review_type = "/reviews?type="

    url = rt_base_url + review_type + "top_critics"

    req = requests.get(url)

    soup = Soup(req.text, "html.parser")
    reviews = soup.find_all(class_="the_review")

    i = 0
    summary += "\nRotten Tomatoes reviews:\n"
    for review in reviews:
        i += 1
        summary += "review" + str(i) + ": "
        summary += review.get_text().strip() + "\n" + "\n"
    return summary
