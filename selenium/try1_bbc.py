from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

bbc_url="https://www.bbc.co.uk/"

def analyze_page_source(d: webdriver.Chrome):
    print(f"page source={len(d.page_source)}")
    all_li_elements=d.find_elements(by= By.TAG_NAME,value="li")
    print("got LI elements")
    print(all_li_elements)
    for li_element in all_li_elements:
        print(li_element)
    pass

if __name__=="__main__":
    options = Options()
    options.add_argument('--headless=new')    
    driver = webdriver.Chrome(
        options=options)
    driver.get(url=bbc_url)
    analyze_page_source(d=driver)
    driver.quit()
    print("Done")
