from selenium import webdriver
import pyttsx3
from plyer import notification
from webdriver_manager.chrome import ChromeDriverManager
import time

def notify(title,message,timeout=3,app_icon='icon.ico'):
    notification.notify(title=title,message=message,timeout=timeout,app_icon=app_icon)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)
count = 0

def audio(text):
    engine.say(text)
    engine.runAndWait()

def main_runner(class_link='https://meet.google.com/awg-wgzr-xju',email='example@gmail.com',password='1234',gender="boss",name='Master',system_browser= False):
    global count
    # driver = webdriver.Chrome()
    email_id = email
    password = password

    if system_browser:print(f"Using dedailt Browser with the meeting link {class_link}")

    if not system_browser:
        try:
            try:
                driver = webdriver.Chrome(ChromeDriverManager().install())
                google_accounts = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
                driver.get(google_accounts)
                email_box = driver.find_element_by_xpath('//*[@id="identifierId"]')
                email_box.send_keys(email_id)
                nextbutton = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
                nextbutton.click()
                notify(title=f"Setting Up things for you {name} {gender} ",
                                    message="Logging in to your school account", timeout=5)
            except Exception as e :
                if e == 'Message: no such window: target window already closed' or e == 'Message: unknown error: cannot determine loading status':
                    driver.quit()
                    quit()

                else:
                    count += 1
                    if count == 1:
                        notify(title="Retrying...", message="Check Your Internet Connection...", timeout=7)
                    if count >= 5:
                        notify(title='Tried Many times...', message="Couldn't find internet....", timeout=5)
                        return 'cancel'

                print("The error I got is ", str(e))



                notify("Don't close the window until it gets loaded...","Note")
                driver.quit()
                main_runner(class_link) # replace it with the output of classlinkfinder funcation

            driver.implicitly_wait(60)
            passwordbox = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            passwordbox.send_keys(password)
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click() #Click on next button
            driver.implicitly_wait(60)

            time.sleep(5)
            notify(title="Getting Google Meet Link.. ",message="Trying to get into the meeting..",timeout=5)
            driver.get(class_link)
            audio("Please grant us permissions..")
            notify("Permissions...","Mic And Camera Permissions were required, hope you ave Allowed Them")
            notify("Enjoy Your Meeting","ENJOY")
            while True:
                assert driver.get_window_size(),'gayo bro'



        except Exception as e :
            print("Errro I gotta",e)
            audio("Canceling the meeting ")
            notify("Exiting From the Web Automation.... Canceling Meeting","Attention")
            # driver.quit()
            return 'cancel'
    else:
        print(f"Using dedailt Browser with the meeting link {class_link}")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(class_link)
        # import webbrowser
        # try :
        #     c= webbrowser.Chrome()
        #     c.open(class_link)
        # except Exception as e :
        #     webbrowser.open(class_link)



# main_runner('https://meet.google.com/awg-wgzr-xju',system_browser=True)