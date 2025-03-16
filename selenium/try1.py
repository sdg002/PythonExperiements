from selenium import webdriver

bbc_url="https://www.bbc.co.uk/"

if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get(url=bbc_url)
    driver.quit()
    print("Hello world")