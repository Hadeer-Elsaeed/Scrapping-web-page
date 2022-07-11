import requests
from bs4 import BeautifulSoup
import qrcode
from fpdf import FPDF
import zipfile
import os

class GenerateQr:
    def __init__(self):
        self.excel_file = '../output_files/data_excel.xlsx'
        self.scrap_url = 'https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9'
    
    def make_hyperlink(self, link):
        if link:
           return f"https://ar.wikipedia.org{link}" 
           

    def scrap_web_url(self):
        response = requests.get(self.scrap_url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        data = []
        links = []
        for tr in table.find("tbody").find_all("tr"):
            data.append([td.get_text(strip=True) for td in tr.find_all("td")])
            for td in tr.find_all("td")[1:2]:
                link = td.find('a')
                if link['href'].startswith("/wiki/"):
                    links.append(link['href'])
                links.append('None')
        return data, links
    

    def generate_pdf(self, i, novel, writer):  
         # Add a page
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font("IBMPlexSansArabic-Bold", style="", fname="fonts/IBMPlexSansArabic-Bold.ttf", uni=True)
            # set style and size of font 
            # that you want in the pdf
            pdf.set_font("IBMPlexSansArabic-Bold", size = 20)
            pdf.image(f'images/img{i}.png', x=50, y=50, w=90, h=90)
            pdf.cell(175, 260, ln=1, txt = novel, align='C')
            pdf.cell(175, -230, ln=1, txt = writer, align='C')
            # save the pdf with name .pdf
            pdf.output(f"pdf_files/book_cover_{i}.pdf")

    
    def generate_code(self):
        data = self.scrap_web_url()[0]
        links = self.scrap_web_url()[1]
        data.pop(0)
        for i in range(0, len(data)):
            hyper_link = self.make_hyperlink(links[i])
            img = qrcode.make(hyper_link)
            img.save(f'images/img{i}.png')
            novel = data[i][1][::-1]
            writer = data[i][2][::-1]
            self.generate_pdf(i, novel, writer)
           
    def zip_output_pdfs(self):
        try:
            zipObj = zipfile.ZipFile('output.zip', 'w', zipfile.ZIP_DEFLATED)
            for filename in os.listdir('pdf_files/'):
                zipObj.write(os.path.join('pdf_files/', filename))
        except FileNotFoundError as e:
            print("An error occurred")
        finally:
            zipObj.close()


       