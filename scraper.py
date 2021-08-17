from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time
import random

session = HTMLSession()

url = 'https://riven.market/list/PC'
r = session.get(url)
userInput = 1
# inputString = "Please enter 1 to continue or 0 to stop \n"
desiredPositives = ['Damage','Multi','CritChance','CritDmg','Range', 'Speed']

def checkPositives(riven):
    if riven.attrs['data-stat1'] in desiredPositives and riven.attrs['data-stat2'] in desiredPositives and riven.attrs['data-stat3'] in desiredPositives:
        return True
    else:
        return False

while userInput != 0:
    try:
        r.html.render(sleep=5, keep_page=True, scrolldown=1)

        # prints all the information in html format
        allData = r.html.find('#riven-list')
        allDataHtml = allData[0].html
        # print(allDataHtml)
        source = allDataHtml
        soup = BeautifulSoup(source, 'html.parser')

        sellers = soup.find_all('div', class_="attribute seller")
        sellercount = 0

        # The following code below returns all the rivens in a giant list, unreadable
        rivens = r.html.find('.riven')
        passFilterCount = 0
        currentRivenCount = 0

        for riven in rivens:
            # returns dictionary of all the riven's atributes
            # print(riven.attrs)
            # Check for 3 positives, 1 negative
            currentRivenCount = currentRivenCount + 1
            if riven.attrs['data-stat1val'] != '0.0' and riven.attrs['data-stat2val'] != '0.0' and riven.attrs['data-stat3val'] != '0.0' and riven.attrs['data-stat4val'] != '0.0':
                if checkPositives(riven) is True:
                    print(riven.attrs['data-weapon'] + ' ' + riven.attrs['data-name'] + ':' + " -negative " + riven.attrs['data-stat4'] + ", Price: " + riven.attrs['data-price'] + " , seller: " + sellers[sellercount].text.strip())
                    passFilterCount = passFilterCount + 1
            sellercount = sellercount + 1
        print("Total Scraped: " + str(passFilterCount))
        number = random.randrange(180, 300)
        time.sleep(number)
    except KeyboardInterrupt:
        print('User has ended loop.')
