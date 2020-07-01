Feature: Partida Ganadora palabra Avion

  Scenario: gana una partida cuando ingresa correctamente las letras
     Given una palabra a resolver vacia
      When ingresa correctamente todas las letras
      Then el resultado es ganador