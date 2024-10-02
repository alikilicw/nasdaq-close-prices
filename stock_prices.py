from driver import get_driver
from selenium.webdriver.common.by import By

# url = 'https://markets.businessinsider.com/index/components/nasdaq_100'


def get_stock_prices():

    driver = get_driver()
    output = {}

    for page in range(1, 4):
        url = f'https://markets.businessinsider.com/index/components/nasdaq_100?p={page}'
        driver.get(url)
        
        table = driver.find_element(By.XPATH, '//div[@class="table-responsive"]//table[@class="table table__layout--fixed"]//tbody[@class="table__tbody"]')

        rows = table.find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            
            cols = row.find_elements(By.TAG_NAME, 'td')

            name = cols[0].text
            last_price = cols[1].get_attribute('innerHTML').split('<br>')[0].strip()

            output[name] = last_price

    driver.quit()
    return output