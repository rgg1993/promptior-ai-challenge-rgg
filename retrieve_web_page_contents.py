from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service


# Save page contents
def save_page_content(driver, filename):
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    pretty_content = soup.prettify()
    with open(filename, "w") as f:
        f.write(pretty_content)

# Retrieve web page contents
def retrieve_web_page_contents(landing_page_file, about_us_page_file):
    

    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    driver=webdriver.Chrome(options=chrome_options)

    url = "https://promptior.ai"
    driver.get(url)
    driver.implicitly_wait(20)

    driver.find_elements(By.CLASS_NAME, "about-page")

    save_page_content(driver, landing_page_file)

    driver.implicitly_wait(20)

    button = driver.find_element(By.XPATH, '//a[@href="/about"]/button')

    button.location_once_scrolled_into_view

    ActionChains(driver).move_to_element(button).click().perform()

    save_page_content(driver, about_us_page_file)

    driver.quit()
