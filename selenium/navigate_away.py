from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


bbc_url="https://www.bbc.co.uk/"

def get_all_links(d: webdriver.Chrome):
    all_li_elements=d.find_elements(by= By.TAG_NAME,value="li")
    print("got LI elements")
    print(all_li_elements)
    for li_element in all_li_elements:
        print(li_element.text)
    print("-----------------")

def load_home(d: webdriver.Chrome):
    print(f"Going to load {bbc_url}")
    d.get(url=bbc_url)
    print(f"Loaded {bbc_url}")
    #d.implicitly_wait()
    
    sports_anchor = WebDriverWait(timeout=10, driver=d).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Sport")))
    print("Got sports link")
    print(sports_anchor.text)
    sports_url=sports_anchor.get_attribute("href")
    print(f"Going to nav to {sports_url}")
    d.get(url=sports_url)
    print("Should have got sports page")
    #wait for page load
    get_all_links(d=d)



if __name__=="__main__":
    options = Options()
    options.add_argument('--headless=new')    
    driver = webdriver.Chrome(
        options=options)
    load_home(d=driver)
    driver.quit()
    print("Done")
