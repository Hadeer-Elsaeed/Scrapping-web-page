import requests
from bs4 import BeautifulSoup
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import settings

class Get_Page_Content:
    def __init__(self):
        self.url = settings.WEBISTE+"{}"
    
    def fetch_data(self):
        """ Fetch data and get coulumns, data and links
        """
        response = requests.get(settings.WEB_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        columns = [i.get_text(strip=True) for i in table.find_all("th")]
        data = []
        links = []
        for tr in table.find("tbody").find_all("tr"):
            data.append([td.get_text(strip=True) for td in tr.find_all("td")])
            for td in tr.find_all("td")[1:2]:
                link = td.find('a')
                if link['href'].startswith("/wiki/"):
                    links.append(link['href'])
                links.append('None')
        return columns, data, links
    
    def make_hyperlink(self, link, text):
        """ function that prepare hyperlink 
        """
        return '=HYPERLINK("%s", "%s")' % (self.url.format(link), text) if link else text

    
    def write_to_excel(self):
        """ write content to excel sheet
        """
        inserted_data = self.fetch_data()
        columns = inserted_data[0]
        data = inserted_data[1]
        links = inserted_data[2]
        data.pop(0)
        for i in range(0, len(data)):
            new_name = self.make_hyperlink(links[i], data[i][1])
            data[i][1]= new_name
        data.insert(0, [])
        df = pd.DataFrame(data,columns=columns)
        df.to_excel(settings.EXCEL_PATH, index=False)

    def write_to_google_sheet(self):
        """ write content to google sheet
        """
        inserted_data = self.fetch_data()
        columns = inserted_data[0]
        data = inserted_data[1]
        data.pop(0)
        scope = [settings.SCOPE_SPREADSHEET, settings.SCOPE_AUTH_DRIVE]
        credentials = Credentials.from_service_account_file("client_secret.json", scopes=scope)
        client = gspread.authorize(credentials)
        spreadsheet = client.open("spreadsheet")
        try:
            worksheet = spreadsheet.add_worksheet(title="spreadsheet", rows="500", cols=10)
        except:
            worksheet = spreadsheet.worksheet("spreadsheet")
        finally:
            worksheet.append_row(columns)
            worksheet.append_rows(data)
