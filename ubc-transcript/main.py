import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import bs4

def retrieveGrades():
    driver = webdriver.Chrome("./driver/chromedriver.exe")
    driver.get("https://ssc.adm.ubc.ca/sscportal/servlets/SSCMain.jsp?function=SessGradeRpt")
    # User must manually login
    wait = input("Press any key to continue after logging in")
    if (driver.current_url != "https://ssc.adm.ubc.ca/sscportal/servlets/SSCMain.jsp?function=SessGradeRpt"):
        print("Log in unsuccesful")
        sys.exit()
    driver.switch_to_frame(driver.find_element_by_id('iframe-main'))
    return driver.page_source

def parse(page):
    data = []
    cleanedPage = bs4.BeautifulSoup(page, features = "lxml")
    try:
        gradesTable = cleanedPage.find(id='allSessionsGrades')
    except:
        print('Unable to find grades table')
        sys.exit()
    gradesTableBody = gradesTable.find('tbody')
    rows = gradesTableBody.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        temp = []
        for col in cols:
            temp.append(str(col.string))
        data.append(temp)
    return data


def clean(data):
    print(data)
    
    
def main():
    print('Log in to SSC in the following window')
    page = retrieveGrades()
    data = parse(page)
    clean(data)
    print('Wait till the course name lookup completes')


if __name__ == "__main__":
    main()
