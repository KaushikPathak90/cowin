from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.page_load_strategy = 'none'
# options.page_load_strategy = 'eager'


def get_date_time():
    return (time.strftime("%Y%m%d%H%M%S", time.localtime()))


class Cowin:
    def __init__(self):
        # Download the latest version of Chromedriver from
        # https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip
        # and unzip it and put the path here -
        self.driver = webdriver.Chrome(r"C:\Users\kaush\Downloads\chromedriver_win32_91\chromedriver.exe", options=options)
        # Open chrome browser

        self.driver.get("https://www.cowin.gov.in/home")
        # Launch the URL
        self.driver.maximize_window()
        self.driver.save_screenshot("./images/image" + get_date_time() + ".png")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div").click()
        #Search by District
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[2]/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/mat-option[37]/span").click()
        #West Bengal
        time.sleep(1)
        self.driver.save_screenshot("./images/mage" + get_date_time() + ".png")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[2]/div/div/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/mat-option[29]/span").click()
        #West Bardhaman
        time.sleep(1)
        self.driver.save_screenshot("./images/mage" + get_date_time() + ".png")

    def search(self):            

        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[2]/div/div/div[3]/button").click()
        #Search

        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label").click() 
        #Age 18+


n = 1000000
bot = Cowin()
try:
    i = 1
    while True:
        print("-----\nLoop: " + str(i))
        bot.search()
        time.sleep(5)
        if i == 1:
            for _ in range(10):
                bot.driver.find_element(By.XPATH,"/html").send_keys(Keys.ARROW_DOWN)
        bot.driver.save_screenshot("./images/mage" + get_date_time() + ".png")
        i += 1
        if i > n:
            break
except:
    print("Program returned an error")

print("End")
