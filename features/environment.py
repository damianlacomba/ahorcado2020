import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#DRIVER LOCAL
#driver = r"C:\Users\Damian\Downloads\chromedriver_win32\chromedriver.exe"

#DRIVER EN EL SERVIDOR
driver = r"/home/travis/virtualenv/python3.8.0/bin/chromedriver"

app = "https://agiles20-ahorcado.herokuapp.com/"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")

def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(options=chrome_options, executable_path=driver)
    context.browser.set_page_load_timeout(time_to_wait=200)

def after_all(context):
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()
