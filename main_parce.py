from selenium import webdriver
import time

def save_html(url, page):
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')


    try:
        driver.get(url=url+str(page))
        time.sleep(3)
        with open('index.html', 'w') as f:
            f.writelines(driver.page_source)


    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()