from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# get a driver instance
def get_driver() -> Chrome:
    
    options = Options()
    
    # Chromium'un bulunduğu yolu belirt
    options.binary_location = '/usr/bin/chromium'  # Bu, Chromium'un kurulu olduğu sistemdeki yolu
    
    # Set Chrome preferences (Chromium için de geçerli)
    prefs = {
        'profile.default_content_setting_values': {
            'cookies': 2,
            'images': 2,
            'javascript': 2,
            'popups': 2,
            'geolocation': 2,
            'notifications': 2,
        },
        'browser.tabs.animate': False,
        'browser.download.manager.showWhenStarting': False,
        'browser.shell.checkDefaultBrowser': False,
        'app.update.auto': False,
        'app.update.enabled': False,
        'browser.cache.disk.enable': False,
        'browser.cache.memory.enable': False
    }
    
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    return Chrome(options=options)
