Feature: Partida Ganadora palabra GATO

  Scenario: un jugador gana una partida cuando ingresa correctamente las letras
     Given un jugador
      When ingresa correctamente todas las letras
      Then el resultado es ganador
  
  Scenario: un jugador pierde una partida cuando ingresa 6 veces las letras incorrectas
     Given un jugador
      When ingresa 6 veces letras incorrectas
      Then el resultado es perdedor