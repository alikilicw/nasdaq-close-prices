from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# get a driver instance
def get_driver() -> Firefox:

    profile = FirefoxProfile()

    profile.set_preference("browser.tabs.animate", False)
    profile.set_preference("browser.panorama.animate_zoom", False)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.shell.checkDefaultBrowser", False)
    profile.set_preference("app.update.auto", False)
    profile.set_preference("app.update.enabled", False)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)

    options = Options()
    options.add_argument('--headless')
    options.set_preference("layers.acceleration.disabled", True)

    return Firefox(options)