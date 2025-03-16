from selenium import webdriver
from selenium.webdriver.chrome.options import Options

bbc_url="https://www.bbc.co.uk/"


if __name__=="__main__":
    options = Options()
    options.add_argument('--headless=new')    
    driver = webdriver.Chrome(
        options=options)
    driver.get(url=bbc_url)
    driver.quit()
    print("Done with headless ")
