import requests
from bs4 import BeautifulSoup as Soup

##################################################### IMDB #####################################################
def IMDB(movie_name_raw):
    imdb_url = "https://www.imdb.com/search/title/?title="
    imdb_base_url = "https://www.imdb.com/"
    # movie_name = str(input())
    movie_name = movie_name_raw
    imdb_url = imdb_url + movie_name

    r = requests.get(imdb_url)

    imdb_movies_soup = Soup(r.text, "html.parser")

    movie_tags = imdb_movies_soup.find_all("a", attrs={"class": None})

    movie_tags = [
        tag.attrs["href"]
        for tag in movie_tags
        if tag.attrs["href"].startswith("/title") & tag.attrs["href"].endswith("/")
    ]

    movie_tags = list(dict.fromkeys(movie_tags))

    rev_url = imdb_base_url + str(movie_tags[0]) + "criticreviews/"
    title_url = imdb_base_url + str(movie_tags[0])

    title_link = requests.get(title_url)
    title_soups = Soup(title_link.text, "html.parser")
    title = title_soups.find("h1")

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
    rt_url = "https://www.rottentomatoes.com/"
    rt_searchUrl = rt_url + str("search?search=") + str(movie_name)

    rt = requests.get(rt_searchUrl)
    rt_movies_soup = Soup(rt.text, "html.parser")
    rt_mov = str(rt_movies_soup.find_all("script", attrs={"id": "movies-json"}))

    rt_base_url = rt_mov[
        rt_mov.find("https://rottentomatoes.com/m/") : (
            rt_mov.find('"', rt_mov.find("https://rottentomatoes.com/m/"), len(rt_mov))
        )
    ]

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
