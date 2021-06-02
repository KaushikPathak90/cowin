from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.page_load_strategy = 'none'
# options.page_load_strategy = 'eager'


def get_date_time():
    return (time.strftime("%Y%m%d%H%M%S", time.localtime()))


class Cowin:
    def __init__(self):
        # Download the latest version of Chromedriver from
        # https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip
        # and unzip it and put the path here -
        self.driver = webdriver.Chrome(r"C:\Users\kaush\Downloads\chromedriver_win32_91\chromedriver.exe", options=options)
        # Open chrome/firefox browser

        self.driver.get("https://www.cowin.gov.in/home")
        # Launch the URL

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]/div").click()
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[3]/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/mat-option[37]/span").click()                                                                                                                         
        #West Bengal

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[3]/div/div/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/mat-option[29]/span").click()
        #West Bardhaman

    def search(self):            

        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[3]/div/div/div[3]/button").click() 
        #Search

        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label").click() 
        #Age 18+

        ## Current World Population
        #print("Current World Population: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[1]/div/span").text.title()) 

        ## Today:  Births, Deaths and population growth today
        #print("TODAY")
        #print("Births today: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div[2]/span").text.title())
        #print("Deaths today: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[3]/div[2]/span").text.title())
        #print("Population Growth today: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div/div[4]/div[2]/span").text.title())

        ## This Year:  Births, Deaths and population growth today
        #print("THIS YEAR")
        #print("Births this year: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/span").text.title())
        #print("Deaths this year: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[3]/div[2]/span").text.title())
        #print("Population Growth this year: " + self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[2]/div/div[4]/div[2]/span").text.title())


n = 100000
bot = Cowin()
try:
    i = 1
    while True:
        print("-----\nLoop: " + str(i))
        bot.search()
        time.sleep(5)
        bot.driver.save_screenshot("./image" + get_date_time() + ".png")
        i += 1
        if i > n:
            break
except:
    print("Program returned an error")

print("End")