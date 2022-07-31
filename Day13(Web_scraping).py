# Web Scraping using Beautiful soup and request liv=brary

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.jumia.com.ng/?aff_click_id=441b8f3f-a557-471c-aacc-7d4f9ff60952&utm_source=kol&utm_medium=affiliation&utm_campaign=43b01fb3-23b0-4c5a-9d44-b1f0b80f5af7&utm_term=customlinks&utm_content=189f6752-f881-37f4-87a4-7cae442bf3ee")
print(response)