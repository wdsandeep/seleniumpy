import requests
from bs4 import BeautifulSoup
url = "https://www.studiohba.com/projects/hotel-resorts/"

# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

# Step 3 : HTML Tree Traversal
# print(type(soup))
# print(type(title))
# print(type(title.string))
# Get the title of HTML Page
title = soup.title

paras = soup.findAll('p')
paras = soup.findAll('a')
# print(soup.find('li'))
# print(soup.find('li')['class'])
# print(soup.find('li')['id'])
# print(soup.find('li')['style'])

# print(soup.find("div", class_="studio_projectinner").get_text())
# print(soup.get_text())

# img = soup.findAll('img')

# for image in img:
#     print(image.get('src'))

soup = BeautifulSoup(htmlContent, 'html.parser')
anchors = soup.findAll('a')
# print(anchors)

# all_links = set()

# for link in anchors:
#     if(link.get('href') != '#'):
#         linkText = link.get('href')
#         all_links.add(linkText)
#         print(linkText)


# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup, features="html5lib")
# print(soup2.p.string)

projectinnerr = soup.find(class_='clientList')
# for elem in projectinnerr.contents:
#     print(elem)
#     print("-----------------------")

# for item in projectinnerr.stripped_strings:
#     print(item)
#     print('------------')

# for item in projectinnerr.parents:
#     print(item.name)

projectinnerr1 = soup.find(id='projectinnerr')
# print(projectinnerr1.next_sibling.next_sibling)
# print('------------------')
# print(projectinnerr1.previous_sibling.previous_sibling)

elem = soup.select('#footer')
print(elem)
