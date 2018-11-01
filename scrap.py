'''
Scrap the project names and urls of github machine learning repos
'''

from selenium import webdriver #browser launching
from selenium.webdriver.common.by import By #search with parameters
from selenium.webdriver.support.ui import WebDriverWait #allow wait page #till loading
from selenium.webdriver.support import expected_conditions as EC #determine page loaded or not
from selenium.common.exceptions import TimeoutException #handling timeout
 
driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = '/home/pravesh/Downloads/chromedriver'
def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)
 
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")
 
#headline's got a h1 tag with class h3 ln-condensed
projects = browser.find_elements_by_xpath("//h1[@class='h3 lh-condensed']")
 
project_list = {}
for project in projects:
    project_name = project.text
    project_url = project.find_elements_by_xpath("a")[0].get_attribute('href')
    print(project_name+' -> '+project_url)
    project_list[project_name] = project_url

browser.quit()
