import webbrowser

def opener(url):
    try:
        c = webbrowser.get('chrome')
        c.open(url)
    except Exception as e :
        webbrowser.open(url)
