from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3
from plyer import notification
import time
from selenium.webdriver.common.alert import Alert


def notify(title,message,timeout=3,app_icon=None):
    notification.notify(title=title,message=message,timeout=timeout,app_icon=app_icon)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
count = 0

def audio(text):
    engine.say(text)
    engine.runAndWait()

def main_runner(class_link='https://meet.google.com/awg-wgzr-xju'):
    global count

    email_id = "kaladhargopal@gmail.com"
    password = "kaladhargopal."

    try:
        driver = webdriver.Chrome()
        google_accounts = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        driver.get(google_accounts)
        alert = Alert(driver=driver)

        act = ActionChains(driver=driver)

        email_box = driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_box.send_keys(email_id)
        nextbutton = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        nextbutton.click()
        notify(title="Setting Up things for you Kaladhar Sir ",
                            message="Logging in to your school account", timeout=5)
    except Exception as e :
        count+= 1
        if count == 1:
            notify(title="Retrying...", message="Check Your Internet Connection...", timeout=7)
        if count >= 5:
            notify(title='Tried Many times...',message="Couldn't find internet....",timeout=5)
            driver.quit()
            quit()

        print("The error I got is ",e)
        driver.quit()
        main_runner(class_link)


    driver.implicitly_wait(60)
    passwordbox = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passwordbox.send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click() #Click on next button
    driver.implicitly_wait(60)

    time.sleep(5)

    notify(title="Getting Google Meet Link.. ",message="Trying to get into the meeting..",timeout=5)
    driver.get(class_link)
    driver.implicitly_wait(60)
    time.sleep(7)

    # reload = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[3]/div[1]/button/div[2]')
    try:
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/div[1]')
        notify(title='Trying Again...',message="Seems that the meeeting has not started yet... ",timeout=3)
    except Exception as e :
        print("Exception is ",e)
        notify("Trying Again","Trying Again")
        while True:
            if str(driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/div[1]')) =='<selenium.webdriver.remote.webelement.WebElement (session="df8689d54605db2a659df32a1d088209", element="0832bc24-8501-43a3-b017-c21201cb33ad")>':
                notify(title="Camera and MIC permissions are required...",
                       message="Allow the permissions manually to ensure that you are not robot...",
                       timeout=5)
                break
            else:
                driver.refresh()





    mic_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/div[1]')

    # count = 0
    # while True:
    #     if driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[1]') != None:
    #         print("trying again..")
    #         # driver.get(class_link)
    #         driver.refresh()
    #     else:
    #         break
    #     count +=1
    #     if count == 30:
    #         notify(title='Tried Many times..', message="Unexpected error occured", timeout = 3)
    #         quit()

    # notify(title="Camera and MIC permissions are required...",
    #                     message="Allow the permissions manually to ensure that you are not robot...",
    #                     timeout=5)
    notify(title="Now you can enjoy your meeting Kaladhar Sir...",message="All set..",timeout=4)
    # time.sleep(6)
    # ask_to_join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/span/span')
    # ask_to_join.click()


# main_runner('https://meet.google.com/lookup/fwqt6unkfr?authuser=1&hs=179')
main_runner()