import webbrowser

user_default_browser = False


def openurl(url):
    global user_default_browser
    if user_default_browser:
        webbrowser.open(url)
    else:
        print("Permission denied")
    
def globalChange(state):
    globals()['user_default_browser'] = state
    
globalChange(True)
openurl("https://google.com")