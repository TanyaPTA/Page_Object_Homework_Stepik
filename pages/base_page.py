class BasePage():
def __init__(self, browser, url):
    self.browser = browser
    self.url = url

def open(self):
    #метод открывает нужную страницу исп-я метод get()
    self.browser.get(self.url)