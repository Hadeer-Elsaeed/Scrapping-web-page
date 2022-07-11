from get_page_content import Get_Page_Content

def main():
    get_content = Get_Page_Content()
    get_content.write_to_excel()
    get_content.write_to_google_sheet()

if __name__ == "__main__":
    main()