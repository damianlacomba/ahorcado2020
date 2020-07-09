Feature: Continua apretando letras luego de ganar 

   Scenario: Cuando un jugador gana y sigue aprentando letras el juego no se modifica
      Given un ganador 
      When ingresa 6 letras incorrectas
      Then el resultado es ganador 