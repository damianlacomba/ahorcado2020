Feature: Resultador de un jugador de la palabra GATO


    
  Scenario: un jugador gana una partida cuando ingresa correctamente las letras
     Given un jugador
      When ingresa correctamente todas las letras
      Then el resultado es ganador
  
  Scenario: un jugador pierde una partida cuando ingresa 6 veces las letras incorrectas
     Given un jugador
      When ingresa 6 veces letras incorrectas
      Then el resultado es perdedor
   
   Scenario: un jugador gana una partida cuando letras correctas e incorrectas en seis intentos
     Given un jugador
      When ingresa letras correctas e incorrectas
      Then el resultado es ganador

   Scenario: Cuando un jugador gana y sigue aprentando letras el juego no se modifica
      Given un ganador
       When ingresa 6 veces letras incorrectas
       Then el resultado es ganador
      
   
 

