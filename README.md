# ChestQuest 💰
A simple exploration-based treasure hunting game built in Python.

The goal of the game is to locate a hidden chest somewhere on the map
before you run out of time or energy. The player moves by clicking on
the map, and receives feedback based on how close they are to the chest.


How the Game Works:

- A chest is randomly generated somewhere on the map.
- The player moves by clicking different locations.
- After each move, the game evaluates the distance between the player
  and the chest.
- Based on this distance, feedback is given:
    * Hot   -> very close
    * Warm  -> getting closer
    * Cold  -> far away
- When the chest is found, the player earns gold and advances.


Energy & Weather System:

- Every move costs energy.
- The amount of energy lost depends on the weather:
    * Sunny  -> lower energy drain
    * Rainy  -> moderate energy drain
    * Stormy -> high energy drain
- If energy reaches zero, the game ends.


Wheel Rewards:

- After completing a level, the player spins a reward wheel.
- Possible rewards include:
    * Gold
    * Extra time
    * Power boosts
- Rewards are randomly selected to add replay value.


Healstone Shop:

- Players can spend gold on healstones.
- Healstones restore energy but cost gold, forcing the player to
  decide between saving gold or surviving longer.


Technical Details:

- Written in Python.
- Uses a simple graphics library for rendering and mouse input.
- Game logic is broken into functions for readability and maintainability.
- Randomization is used for chest placement, weather, and rewards.


Files Included:

- chestQuest.pyw 
  -> Main game file

- chestQuest_beta_test.py 
  -> Beta testing version used during development.

- test_Cases_chestQuest.py
  -> Test cases and manual testing notes used to verify game logic.

- start_screen.png and gameplay_screen.png
  -> two png files showing a preview of the gameplay


How to Run:

1. Make sure Python is installed.
2. Ensure the required graphics module is downloaded (graphics.py).
3. Run the main file: chestQuest.pyw
4. Have fun!


Notes:

Future improvements may include:
- Better balancing of rewards
- Cleaner constants for costs and distances
- Additional levels or mechanics

- Developed in collaboration with Methsaan Wickramasinghe
