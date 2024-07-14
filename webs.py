import requests
from bs4 import BeautifulSoup


url="https://www.simplilearn.com/"

r= requests.get(url)
htmlContent= r.content

# print(htmlContent)
#BeautifulSoup used to extract html and xml file i.e extract data.

soup= BeautifulSoup(r.content,'html.parser')
# for i in soup.find_all("code"):
#     print(i.text)

# title = soup.title
# print(title.string)

# a=soup.find_all('p')
# for i in a:
#     print(i)

# print(soup.find('p')[6]['class'])
# second_p = soup.find_all('p')[7]  # Find all <p> tags and get the seventh one
# print(second_p['class']) #find class of second p

# print(soup.find('p').get_text())

anchor=soup.find_all('a')
# print(anchor)

# for i in anchor:
#     print(i.get('href'))

al = set()
# for i in anchor:
#     href = i.get('href')
#     if href is not None:
#         text = "https://www.simplilearn.com/" + href
#         al.add(text)
#         print(text)

root=soup.find(id='root')
print(root)
 