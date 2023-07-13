import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in all_movies]

# for n in range (len(movie_titles) -1, -1, -1): #arranca del final y va recorriendo hacia el principio de la lista
#     print(movie_titles[n])

movies = movie_titles[::-1] #Aca lo que se hace es leer de atras para adelante. Hacer un "reverse"

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

