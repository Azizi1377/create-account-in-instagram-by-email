from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from fastapi import FastAPI, Query
from selenium import webdriver
import time


app = FastAPI(title="instagram")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=/home/pishtazan/.config/google-chrome/Profile2")

@app.get("/insCode")
def fetchInstagramCode(
    emailName: str = Query(default=..., description="Choose a name for your email"),
    fullName: str = Query(default=..., description="Enter full name for create account in instagram"),
    userName: str = Query(default=..., description="Enter user name for create account in instagram"),
    password: str = Query(default=..., description="Enter password for create account in instagram"),
    ):

    chromeDriver = Service(ChromeDriverManager().install())

    url = 'https://www.guerrillamail.com/'
    gmailDriver = webdriver.Chrome(service=chromeDriver, chrome_options=chrome_options) 

    gmailDriver.current_window_handle 
    gmailDriver.implicitly_wait(1)
    gmailDriver.get(url)
    time.sleep(1)

    gmailDriver.maximize_window
    time.sleep(2)

    emailNameButton=gmailDriver.find_element(by=By.XPATH, value='//*[@id="inbox-id"]')
    emailNameButton.click()
    time.sleep(3)

    buttonSetEmailName=gmailDriver.find_element(by=By.XPATH, value='//*[@id="inbox-id"]/input')
    buttonSetEmailName.send_keys(emailName)
    time.sleep(3)

    selectAddres=gmailDriver.find_element(by=By.XPATH, value='//*[@id="inbox-id"]/button[1]')
    selectAddres.click()
    time.sleep(3)

    fetchEmail=gmailDriver.find_element(by=By.XPATH, value='//*[@id="email-widget"]').text
    print('email is: '+fetchEmail)
    time.sleep(3)

    gmailDriver.execute_script("window.open('about:blank', 'second tab');")
    gmailDriver.switch_to.window("second tab")
    gmailDriver.get('https://www.instagram.com/accounts/emailsignup/')
    # WebDriverWait(gmailDriver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')))
    time.sleep(10)

    inputEmail = gmailDriver.find_element(by=By.NAME, value='emailOrPhone')
    inputEmail.send_keys(fetchEmail)                         
    time.sleep(3)

    inputFullName=gmailDriver.find_element(by=By.NAME, value='fullName')
    inputFullName.send_keys(fullName) 
    time.sleep(3)

    inputUserName=gmailDriver.find_element(by=By.NAME, value='username')
    inputUserName.send_keys(userName) 
    time.sleep(3)

    inputPassword=gmailDriver.find_element(by=By.NAME, value='password')
    inputPassword.send_keys(password) 
    time.sleep(3)

    signupButton=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button')
    signupButton.click()
    time.sleep(6)

    selectMonth=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
    selectMonth.click()
    time.sleep(3)
    selectNameMonth=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[6]')
    selectNameMonth.click()
    time.sleep(3)

    selectDay=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select')
    selectDay.click()
    time.sleep(3)
    selectNumberDay=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[11]')
    selectNumberDay.click()
    time.sleep(3)

    selectYear=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
    selectYear.click()
    time.sleep(3)
    selectNumberYear=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[29]')
    selectNumberYear.click()
    time.sleep(3)

    buttonNext=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button')
    buttonNext.click()
    time.sleep(60)

    gmailDriver.execute_script("window.open('about:blank', 'first tab');")
    gmailDriver.switch_to.window("first tab")
    gmailDriver.get('https://www.guerrillamail.com/')
    time.sleep(7)

    fetchCode=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[3]/div[2]/form/table/tbody/tr[1]/td[3]').text
    subject = list(fetchCode)
    outputCode = subject[1:7]
    verificationCode = ''.join(outputCode)
    print('Code is: '+verificationCode)
    time.sleep(7)

    handles = [] 
    handles = gmailDriver.window_handles 

    for handle in handles: 
        print('handle is: '+handle) 

    gmailDriver.switch_to.default_content() 
    gmailDriver.switch_to.window(handles[1]) 
    time.sleep(7)


    inputCode=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
    inputCode.send_keys(verificationCode)
    time.sleep(3)

    buttonElement=gmailDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    buttonElement.click()
    time.sleep(30)


    return { "fullname": fullName, "username": userName, "password": password}  # "email": inputdomain,
