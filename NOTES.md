#My Problem
I need to create a game in Python to satisfy LPTHW exercise 45. I need to import a class from a separate file. It is recommended to use an engine to progress through the levels or scenes.

#My Scenario
A simplistic game that takes the player through a house. The player. a detective, has been sent to an address after an anonymous tip. Eerily silent, it's clear that something is amiss. The detective approaches an old house, in the country, set back off the road, wooded on all sides. Enters through a door on an elevated porch. He steps into a dusty hallway. Cupboard under the stairs reveals no clues. Downstairs is four rooms, clockwise from the hallway these are reception room, lounge, kitchen, dining room, and back into the hallway. The stairs are L shaped leading onto a landing with windows to the front of the house, 4 bedrooms in the corners, and a bathroom rear centre. Our detective finds themself in a master bedroom where a gap in the wallpaper gives away a sliding panel that was shut in a hurry. Behind it is a thick wooden door with a number pad, 4 digits are required. The detective might guess the number, or he may get stuck. Lost for what the number might be he searches the room. He finds a picture by the bed of a man standing in front of the house with his hands on the shoulders of a young girl. He recognises her from an unsolved case of a missing girl ten years ago... he tears the picture out of the frame and her name is on the back... what if her name is the code... he returns to the lock... success! How has the kidnapper lasted this long? Our detective pushes the heavy door back to find a set of stairs. He ascends into the loft space where he finds a room decorated far more recently than the rest of the house. He sees a body on a divan bed in the corner of this secret loft room... he whispers her name but she doesn't move... he approaches and finds she is barely conscious. He doesn't notice the wardrobe door has opened, when he hears a gun being cocked... "Save her, or you'll both be dead."

#Scenes

outside - starting point, leads to porch

porch - from outside, leads to hallway

hallway - leads to dining room, reception, or use stairs for landing, and there's a cupboard under the stairs

reception - leads to lounge or hallway

lounge - leads to kitchen or reception

kitchen - leads to dining room or lounge

dining room - leads to hallway or kitchen

landing - leads to bedroom 1, 2, 3, 4, bathroom, or use stairs for hallway

bedroom 1 - front left

bedroom 2 - rear left, inspection reveals a gap in the wallpaper, hidden door, lock puzzle, stairs to loft

bedroom 3 - read right

bedroom 4 - front right

loft - the final scene

#Keywords
* Player
* Scenes
* Descriptions
* Interactions
* Locked door
* Picture in frame
* Outside
* Porch
* Hallway
* Reception
* Lounge
* Kitchen
* Dining Room
* Landing
* Bedroom 1
* Bedroom 2
* Bedroom 3
* Bedroom 4

#Layout
* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Outside
  * Porch
  * Hallway
  * Reception
  * Lounge
  * Kitchen
  * Dining Room
  * Landing
  * Bedroom 1
  * Bedroom 2
  * Bedroom 3
  * Bedroom 4
