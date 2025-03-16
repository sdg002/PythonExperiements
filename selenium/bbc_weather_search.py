from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BBC_WEATHER_URL="https://www.bbc.co.uk/weather"
POSTCODE_ELEMENT_ID="ls-c-search__input-label"
SEARCH_LOCATION="RG4"

def get_all_weather_days(d: webdriver.Chrome):
    all_li_elements=d.find_elements(by= By.XPATH,value="//a[contains(@id,'daylink')]")
    print("got LI elements")
    print(all_li_elements)
    for li_element in all_li_elements:
        print(li_element.text)
    print("-----------------")

def load_weather(d: webdriver.Chrome):
    print(f"Going to load {BBC_WEATHER_URL}")
    d.get(url=BBC_WEATHER_URL)
    print(f"Loaded {BBC_WEATHER_URL}")
    #d.implicitly_wait()
    
    postcode_element = WebDriverWait(timeout=10, driver=d).until(EC.presence_of_element_located((By.ID,POSTCODE_ELEMENT_ID)))
    print(f"Got post code element, {postcode_element.tag_name=}")

    postcode_element.send_keys(SEARCH_LOCATION)
    print(f"Send search text:{SEARCH_LOCATION} to the input box")

    submit_xpath="//button[@title='Search for a location']"
    submit_button=d.find_element(by=By.XPATH,value=submit_xpath)
    print(f"Got the submit button {submit_button=}")
    url_before_click=d.current_url
    submit_button.click()
    print("Submit button click")
    #expected_url=f"{}/{SEARCH_LOCATION}"
    WebDriverWait(timeout=10, driver=d).until(lambda x: x.current_url != url_before_click)
    print(f"after wait, current url={d.current_url}")
    input("waiting...press a key to continue")
    print(f"Current url={d.current_url}")
    print("--------------------------")
    get_all_weather_days(d=d)
    #print(d.page_source)
    # print(sports_anchor.text)
    # sports_url=sports_anchor.get_attribute("href")
    # print(f"Going to nav to {sports_url}")
    # d.get(url=sports_url)
    # print("Should have got sports page")
    # #wait for page load
    # get_all_links(d=d)



if __name__=="__main__":
    options = Options()
    options.add_argument('--headless=new')    #comment this to make it visible
    driver = webdriver.Chrome(
        options=options)
    load_weather(d=driver)
    driver.quit()
    print("Done")
