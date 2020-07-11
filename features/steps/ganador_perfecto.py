from behave import given, when, then
from features import environment
import time

@given('un jugador')
def welcome(context):
    context.browser.get('https://agiles20-ahorcado.herokuapp.com/jugar/')
    time.sleep(3)
    element = environment.driver.find_element_by_class_name("user")
    element.send_keys("juani")
    environment.driver.find_element_by_class_name("play").click()
    time.sleep(5)
    jugador = environment.driver.find_element_by_tag_name("h1").text


@when('ingresa correctamente todas las letras')
def correct_words(context):
    for i in ["G","A","T","O"]:
        element = environment.driver.find_element_by_id(i)
        element.enviroment.click()
        time.sleep(2)
    element = environment.driver.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "G A T O"

@then('el resultado es ganador')
def win(context):
    time.sleep(5)
    element = environment.driver.find_element_by_class_name("winner")

    assert element != None