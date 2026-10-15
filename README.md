# Simple-Color-Game-Python-
Simple Color Game using Python and Tkiner

How to play:
1. Execute the main.py on the project’s root folder.
2. Press the “START GAME” button.
3. Choose a color on the bottom side of the window.
4. Place a bet amount and save it.
5. Make sure that a bet was placed on at least 1 color.
6. Press the “ROLL!” button to start the color randomizer.
7. Wait for it to randomly choose 3 winning colors.
8. A result will pop up.
9. Press the “CLOSE” button found in the RESULT AREA and repeat from step 3.



Project Structure:

 main.py
o Entry point of the program.

 ColorGame
  o The ColorGame module / package.
  o __init__.py
  
  o main.py
     Configures the tkinter Window instance.
  
  o constants.py
     Contains mutable package-scoped variables.
  
  o state.py
     Contains the game state.
  
  o handler.py
     Contains functions that make the program interactive.
     Contains the game logic.

  o layout.py
     Creates the necessary widgets for the program.
     Binds “click” event to buttons.

o bindings.py
   Contains event bindings for widgets like KeyPress, Mouse Enter, and Mouse Leave.
