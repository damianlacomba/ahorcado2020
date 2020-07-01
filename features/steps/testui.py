from behave import given, when, then
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Damian\Downloads\chromedriver_win32\chromedriver.exe")

@given('una palabra a resolver vacia')
def step_impl(context):
    driver.get('http://localhost:5000')
    element = driver.find_element_by_id("palabra")
    palabra = element.text

    assert palabra == "_ _ _ _ _"

@when('ingresa correctamente todas las letras')
def step_impl(context):
    for i in ["A","V","I","O","N"]:
        element = driver.find_element_by_id(i)
        element.click()
        time.sleep(5)
    element = driver.find_element_by_id("palabra")
    palabra = element.text
    
    assert palabra == "A V I O N"

@then('el resultado es ganador')
def step_impl(context):
    time.sleep(10)
    element = driver.find_element_by_id("resultado")
    resultado = element.text.strip()
    assert resultado == "FELICITACIONES GANASTE!!"