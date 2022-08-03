# Web Scraping using Beautiful soup and request liv=brary

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.jumia.com.ng/?aff_click_id=441b8f3f-a557-471c-aacc-7d4f9ff60952&utm_source=kol&utm_medium=affiliation&utm_campaign=43b01fb3-23b0-4c5a-9d44-b1f0b80f5af7&utm_term=customlinks&utm_content=189f6752-f881-37f4-87a4-7cae442bf3ee")


#  To get the staus respones
print(response.status_code)
# To get the content
# print(response.content)

# To get it as html

soup = BeautifulSoup(response.content,'html.parser')
print(soup.prettify())

# Find will find the first encounter of the elememt specify
# find('a') -> Finds the first anchor tag
# find_all('img;) -> Finds all image tags
# find_parent('img') -> Finds parent tag


# find('<tag_name>', attr = {"class": "<class_name>"})