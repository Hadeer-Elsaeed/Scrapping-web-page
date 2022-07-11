# scrapping_web_page
# To Run Parsing Program
- clone scrape_webpage
- create and start a a virtual environment
    - "pip install --upgrade virtualenv"
    - "python3 virtualenv env venv" 
    - "source venv/bin/activate"
- pip install -r requirements.txt 

# Problem_One
scrapping web page table and save content in excel file and google sheet
## Packages are used
- "requests" --> to get response from web api url.
- "Beautiful Soup" --> get data from html content
- "Pandas" --> useed to save data in excel file
- "google.oauth2" and "gspread" to get credentials from client_secret file and call  
    google_sheet_api to save data in google_sheet
## To Run Problem_one
Run these commands in terminal
- cd problem_one
- python3 main.py 

# Problem_Two
Make api to access data in excel file [Get - Post - Put - Delete] using flask framework
## Packages are used
- "flask_restful" to make api .
- "Pandas" to read and write to excel file.
## To Run Problem_two
- cd problem_two/flask_app
- flask run 

# Problem_Three
Get data from api, make Qr code for some data in a pdf file and zip all pdf files
## Packages are used
- "requests" --> to get response from web api url.
- "Beautiful Soup" --> get data from html content.
- "qrcode" to make qr code.
- "fpdf" to make pdf files.
- "zipfile" to zip directory.
## To Run Problem_three
Run these commands in terminal
- cd problem_three
- python3 main.py 
