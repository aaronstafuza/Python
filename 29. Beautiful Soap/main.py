from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title) 
# La respuesta de esto es: <title>Angela's Personal Site</title>

# print(soup.title.string)
# La respuesta de esto es: Angela's Personal Site

# print(soup)
# # Con esto puedo ver todo mi HTML

# print(soup.prettify())
# Con esto puedo ver todo mi HTML pero con las sangrias (indentaciones)

# print(soup.a)
# print(soup.li)
# Me dara el primer a que haya en la web y se puede hacer con todo, por ejemplo con el primer "li", etc

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# va a encontrar todas las etiquetas de mi web. 

# for tag in all_anchor_tags:
    # print(tag.getText()) Me va a dar todos los textos que contiene cada etiqueta
    # print(tag.get("href")) me imprime todas los hrefs

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

name = soup.select_one(selector="#name")
print(name)