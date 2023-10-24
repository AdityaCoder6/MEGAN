# Import necessary packages

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re
from Speak import *

def Code(Inputtttt):
    warnings.simplefilter("ignore")
    url = "https://deepinfra.com/chat?gclid=CjwKCAjwgsqoBhBNEiwAwe5w0_BdhuFQlkbl6w31E5Sd8lhKBoPuGOXh6vyPDYayq-4B3YmowiGRfhoCUaIQAvD_BwE"
    chrome_driver_path = r'C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Dataset\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--log-level=3')
    service = Service(chrome_driver_path)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    sleep(5)


    File = open(r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Brain\Main\Llama.txt","w")
    File.write("3")
    File.close()


    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/div/div[3]/div/div[2]/div/div/textarea[1]").send_keys(Inputtttt)
    except:
        driver.find_element(by=By.XPATH,value="/html/body/div/div/div[3]/div/div[2]/div/div/textarea[1]").send_keys(Inputtttt)

    sleep(1)
    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/div/div[3]/div/div[2]/button").click()
    except:
        driver.find_element(by=By.XPATH,value="/html/body/div/div/div[3]/div/div[2]/button").click()

    sleep(10)
    File = open(r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Brain\Main\Llama.txt","r")
    Data = File.read()
    Data = str(Data)
    File.close()
    try:
        XpathValue = f'/html/body/div/div/div[2]/div/div[{Data}]/div/div'
        Text = driver.find_element(by=By.XPATH,value=XpathValue).text
        NewText = re.sub(r'\d+\s*','',Text)
        Speak(NewText)
        File = open(r"C:\Users\AKANSHA\OneDrive\Desktop\MEGAN\Brain\Main\Llama.txt","w")
        NewData = int(Data) + 2
        File.write(str(NewData))
        File.close()
    except Exception as e:
            print(e)
