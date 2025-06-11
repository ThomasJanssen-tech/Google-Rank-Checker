import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import urllib.parse
import datetime
import gspread
import json
from google.oauth2.service_account import Credentials

load_dotenv()

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_info(
    json.loads(os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS')),
    scopes=scopes
)

gc = gspread.authorize(credentials)

sh = gc.open_by_key(os.getenv("GOOGLE_SHEET_ID"))
worksheet = sh.sheet1

keywords = worksheet.row_values(1)

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
            "zone": "serp_api1",
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

                #print(title)

                if(os.environ.get('WEBSITE_URL') in title):
                    position = count
                    continue_loop = False
                    break

                count += 1

        page += 1



    # adding the position of the keyword to the list
    keyword_positions.append(position)
    print(f"Keyword: {keyword}, Position: {position}")

    i += 1

worksheet.append_row(keyword_positions)


