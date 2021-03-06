from behave import given, when, then
import time

url = 'https://agiles20-ahorcado.herokuapp.com/'

@given('un jugador')
def welcome(context):
    context.browser.get(url)
    time.sleep(3)
    element = context.browser.find_element_by_class_name("user")
    element.send_keys("juani")
    context.browser.find_element_by_class_name("play").click()
    time.sleep(5)
    

@when('ingresa correctamente todas las letras')
def correct_words(context):
    for i in ["G","A","T","O"]:
        element = context.browser.find_element_by_id(i)
        element.click()
        time.sleep(2)
    element = context.browser.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "G A T O"

@then('el resultado es ganador')
def win(context):
    time.sleep(5)
    element = context.browser.find_element_by_class_name("winner")

    assert element != None



@when('ingresa 6 veces letras incorrectas')
def incorrect_words(context):
    for i in ["H","I","J","K","L","Y"]:
        element = context.browser.find_element_by_id(i)
        element.click()
        time.sleep(3)
    element = context.browser.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "G A T O"

@then('el resultado es perdedor')
def step_impl(context):
    time.sleep(5)
    element = context.browser.find_element_by_class_name("loser")

    assert element != None


@when('ingresa letras correctas e incorrectas')
def step_impl(context):
    for i in ["H","G","J","A","L","Y","T","O"]:
        element = context.browser.find_element_by_id(i)
        element.click()
        time.sleep(3)
    element = context.browser.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "G A T O"

@given('un ganador')
def step_impl(context):
    context.browser.get(url)
    time.sleep(3)
    element = context.browser.find_element_by_class_name("user")
    element.send_keys("juani")
    context.browser.find_element_by_class_name("play").click()
    time.sleep(5)
    

    for i in ["G","A","T","O"]:
        element = context.browser.find_element_by_id(i)
        element.click()
        time.sleep(2)
    element = context.browser.find_element_by_id("word")
    palabra = element.text
    
    assert palabra == "G A T O"

@given("un usuario en la pagina principal sin registrarse")
def step_impl(context):
    context.browser.get(url)
    jugador = context.browser.find_element_by_class_name("user").text
    assert jugador == ""

@when("ingresa a jugar")
def step_impl(context):
    context.browser.get(url)

@then("permance en el index hasta ingresar su nombre")
def step_impl(context):
    url_value = context.browser.current_url
    assert url_value == url