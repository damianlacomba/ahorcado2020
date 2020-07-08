from behave import given, when, then
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Damian\Downloads\chromedriver_win32\chromedriver.exe")

@given('un jugador')
def step_impl(context):
    driver.get('http://localhost:5000')
    time.sleep(3)
    element = driver.find_element_by_class_name("user")
    element.send_keys("juani")
    driver.find_element_by_class_name("play").click()
    time.sleep(5)
    jugador = driver.find_element_by_tag_name("h1").text

    assert jugador == "Hola, Juani !"

@when('ingresa correctamente todas las letras')
def step_impl(context):
    for i in ["G","A","T","O"]:
        element = driver.find_element_by_id(i)
        element.click()
        time.sleep(2)
    element = driver.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "G A T O"

@then('el resultado es ganador')
def step_impl(context):
    time.sleep(5)
    element = driver.find_element_by_class_name("winner")

    assert element != None

@given('un jugador')
def step_impl(context):
    driver.get('http://localhost:5000')
    time.sleep(3)
    element = driver.find_element_by_class_name("user")
    element.send_keys("juani")
    driver.find_element_by_class_name("play").click()
    time.sleep(5)
    jugador = driver.find_element_by_tag_name("h1").text

    assert jugador == "Hola, Juani !"

@when('ingresa 6 veces letras incorrectas')
def step_impl(context):
    for i in ["H","I","J","K","L","M"]:
        element = driver.find_element_by_id(i)
        element.click()
        time.sleep(2)
    element = driver.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "_ _ _ _"

@then('el resultado es ganador')
def step_impl(context):
    time.sleep(5)
    element = driver.find_element_by_class_name("winner")

    assert element == None