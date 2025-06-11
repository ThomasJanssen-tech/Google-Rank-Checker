import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd
import datetime

load_dotenv()

df = pd.read_csv('keywords.csv')

# fetch the keywords from the CSV file
keywords = df.columns

i = 1

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
keyword_positions = [date]

# looping through all keywords in the CSV file
while(i < len(keywords)):

    keyword = keywords[i]

    headers = {
        'Authorization': 'Bearer '+os.getenv('BRIGHTDATA_API_KEY'),
        'Content-Type': 'application/json',
    }

    page = 1
    continue_loop = True
    count = 1

    # looping through the first 5 pages of Google search results
    while page <= 5 and continue_loop:

        data = {
            "zone": "serp_api",
            "url": "https://www.google.com/search?q="+urllib.parse.quote_plus(keyword)+"&start="+str((page-1)*10),
            "format": "raw",
            "country": os.getenv("GOOGLE_COUNTRY"),
        }


        response = requests.post('https://api.brightdata.com/request', headers=headers, json=data)

        soup = BeautifulSoup(response.content, "html.parser")

        #print(response.status_code)

        results = soup.find_all("h3")

        position = 0

        # checking whether website is mentioned in the search results
        for result in results:

            if(result.parent.has_attr('href')):
                title = str(result.parent['href'])

                print(title)

                if(os.environ.get('WEBSITE_URL') in title):
                    position = count
                    continue_loop = False
                    break

                count += 1

        page += 1

        # adding the position of the keyword to the list
        print(f"Keyword: {keyword}, Position: {position}")

    keyword_positions.append(position)

    i += 1





df2 = pd.DataFrame([keyword_positions],columns=keywords)


df_result = pd.concat([df, df2])
df_result.to_csv('keywords.csv', index=False)