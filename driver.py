from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# get a driver instance
def get_driver() -> Firefox:
    options = Options()
    options.add_argument('--headless')

    return Firefox(options)