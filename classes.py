from sys import exit
from random import randint

def exit_bad_selection():
    print "Error: you should not have got to this point."
    print "Our apologies, please restart the story."
    exit(1)

def code_generation(victim):

    code_map = {
        "a": "2",
        "b": "2",
        "c": "2",
        "d": "3",
        "e": "3",
        "f": "3",
        "g": "4",
        "h": "4",
        "i": "4",
        "j": "5",
        "k": "5",
        "l": "5",
        "m": "6",
        "n": "6",
        "o": "6",
        "p": "7",
        "q": "7",
        "r": "7",
        "s": "7",
        "t": "8",
        "u": "8",
        "v": "8",
        "w": "9",
        "x": "9",
        "y": "9",
        "z": "9",
    }

    code = ""

    for char in victim:
        val = code_map.get(char.lower())
        code += (val)

    return str(code)

class Victim(object):

    names = [
        "Anna",
        "Beth",
        "Cass",
        "Dana",
        "Erin",
        "Faye",
        "Gwen",
        "Hope",
        "Indy",
        "Juno",
        "Kate",
        "Lily",
        "Mona",
        "Nina",
        "Olga",
        "Posy",
        "Rose",
        "Sara",
        "Thea",
        "Vera",
        "Wada",
        "Yuna",
        "Zola",
    ]

    def __init__(self):

        self.name = self.names[randint(0,len(self.names) - 1)]

        self.code = code_generation(self.name)

girl = Victim()

class Scene(object):

    def __init__(self):
        self.VISITS = 0

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

    def show_hints(self, hints):
        print "="*10
        for line in hints: print line
        print "="*10

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Opening(Scene):

    def enter(self):
        print "#"*50
        print 'Operator: "Operator, what\'s your emergency?"'
        print 'Caller: "I\'ve seen someone acting suspcious up at the old '
        print '\tfarm house..."'
        print "#"*50
        print "\nYou, a local detective, arrive at the house the caller "
        print "described. Set back off the road, tree lined on all sides of "
        print "the grounds sits an old farm house that has seen better days."
        print "There is land around the house with farmland beyond the border."
        print "The house has a large front porch,  paint peeling from its "
        print "balustrade. The investigation begins...\n\n"
        return 'outside'

class Outside(Scene):

    hints = [
        "walk to the porch",
        "search the garden",
    ]

    def enter(self):


        if self.VISITS == 0:
            print "You look around at the overgrown gardens surrounding the "
            print "house. It looks like nobody has tended to them for a long"
            print "time. Grass comes to the waist with wild weeds throughout."
            print "A dusty track leads up to the porch."

            print "\n\n*** Note: type 'hint' at any point to see ***"
            print "***       acceptable actions.             ***"
        else:
            pass

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "walk to the porch":
                    return 'porch'
                elif choice == "search the garden":
                    print "You search the gardens around the house and find"
                    print "nothing out of the ordinary."
                    self.hints.remove("search the garden")
                    continue
                else:
                    exit_bad_selection()
            else:
                print "That option is not valid here."
                continue

class Porch(Scene):

    hints = [
        "enter the house",
    ]

    def enter(self):

        if self.VISITS == 0:
            print "The steps creak as you walk up them. A fine film of dust"
            print "covers every surface. The porch light casing is broken and"
            print "discoloured. The door is open..."
        else:
            print "You step onto the porch."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "enter the house":
                    print "You walk through the door, into the hallway."
                    return 'hallway'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Hallway(Scene):

    hints = [
        "look in the cupboard",
        "go to the reception",
        "go to the dining room",
        "go upstairs",
    ]

    def enter(self):

        if self.VISITS == 0:
            print "A stale smell hangs in the air. It's clear that the house"
            print "does not have many visitors. To the left is a reception"
            print "area, to the right a dining room. In front of you is a"
            print "cupboard with a staircase starting on the right with a left"
            print "turn half way up that would take you to the landing."
        else:
            pass

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "look in the cupboard":
                    print "The cupboard door sticks as you try to open it."
                    print "There is nothing inside except some old news papers"
                    print "covering the floor. You close the door again."
                    self.hints.remove("look in the cupboard")
                    continue
                elif choice == "go to the reception":
                    return 'reception'
                elif choice == "go to the dining room":
                    return 'dining_room'
                elif choice == "go upstairs":
                    print "You walk up the stairs and onto the landing."
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Reception(Scene):

    hints = [
        "go to the lounge",
        "go to the hallway",
        "inspect the fireplace",
    ]

    def enter(self):

        print "You walk into the reception room."

        if self.VISITS == 0:
            print "Cobwebs are in every corner. Thick dust covers the mantle"
            print "around the fireplace. The furniture is old and worn. The"
            print "fireplace looks like it has not been used in some time."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "inspect the fireplace":
                    print "You crouch in front of the fireplace to get a"
                    print "closer look at the ash. This fire was a long time"
                    print "ago and it looks like someone was burning more than"
                    print "just logs! You think you can see signs of burned"
                    print "clothing. What has happened here?"
                    self.hints.remove("inspect the fireplace")
                    continue
                elif choice == "go to the lounge":
                    return 'lounge'
                elif choice == "go to the hallway":
                    print "You walk into the hallway."
                    return 'hallway'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Lounge(Scene):

    hints = [
        "go to the kitchen",
        "go to the reception",
    ]

    def enter(self):

        print "You walk into the lounge."

        if self.VISITS == 0:
            print "The first thing you notice as you walk into the lounge is"
            print "that there is a back door that has been nailed shut with"
            print "timbers. Dust clings to all surfaces. It's clear no one"
            print "has been using this room."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the kitchen":
                    return 'kitchen'
                elif choice == "go to the reception":
                    return 'reception'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Kitchen(Scene):

    hints = [
        "go to the dining room",
        "go to the lounge",
    ]

    def enter(self):

        print "You walk into the kitchen."

        if self.VISITS == 0:
            print "This kitchen has not been used in some time, and not"
            print "cleaned even longer still. The fridge has been turned off,"
            print "there's no crockery to be found and a putrid smell rises"
            print "from the sink drain."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the dining room":
                    return 'dining_room'
                elif choice == "go to the lounge":
                    return 'lounge'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class DiningRoom(Scene):

    hints = [
        "go to the kitchen",
        "go to the hallway",
    ]

    def enter(self):

        print "You walk into the dining room."

        if self.VISITS == 0:
            print "The dining table that would have once stood central in the"
            print "room has been tipped on one end and stood in front of the"
            print "window. Someone did not want people looking in too closely."
            print "The chairs are pushed to the outside of the room, and a"
            print "large, worn out rug lays on the floor in the centre of the"
            print "room."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the kitchen":
                    return 'kitchen'
                elif choice == "go to the hallway":
                    print "You walk into the hallway."
                    return 'hallway'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Landing(Scene):

    hints = [
        "examine the landing area more closely",
        "go to the back room",
        "go to the front left room",
        "go to the front right room",
        "go to the back right room",
        "go to the back left room",
        "go downstairs",
    ]

    def enter(self):

        if self.VISITS == 0:
            print "The stairs were bare, their varnish worn over the years."
            print "The landing is windowed to the front of the house, walls"
            print "make up the other three sides, with one door on the back"
            print "wall and two doors each on the left and right. The front"
            print "window has tattered old curtains still hanging from a bowed"
            print "rail, the weight starting to pull the fixings out of the"
            print "wall."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "examine the landing area more closely":
                    print "Something seems off about the landing..."
                    print "Your eyes dart around the scene, looking between"
                    print "the window... the doors... the railings around the"
                    print "stairs... the ceiling...\n"
                    print "... the ceiling... that's strange. Why is there no"
                    print "hatch to the loft?"
                    self.hints.remove("examine the landing area more closely")
                    continue
                elif choice == "go to the back room" or \
                choice == "go to the bathroom":
                    try:
                        self.hints.remove("go to the back room")
                        self.hints.append("go to the bathroom")
                    finally:
                        return 'bathroom'
                elif choice == "go to the front left room" or \
                choice == "go to the front left bedroom":
                    try:
                        self.hints.remove("go to the front left room")
                        self.hints.append("go to the front left bedroom")
                    finally:
                        return 'bedroom_1'
                elif choice == "go to the back left room" or \
                choice == "go to the back left bedroom":
                    try:
                        print "You walk into the main bedroom."
                        self.hints.remove("go to the back left room")
                        self.hints.append("go to the back left bedroom")
                    finally:
                        return 'bedroom_2'
                elif choice == "go to the back right room":
                        return 'bedroom_3'
                elif choice == "go to the front right room" or \
                choice == "go to the front right bedroom":
                    try:
                        self.hints.remove("go to the front right room")
                        self.hints.append("go to the front right bedroom")
                    finally:
                        return 'bedroom_4'
                elif choice == "go downstairs":
                    return 'hallway'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bedroom1(Scene):

    hints = [
        "go to the landing",
    ]

    def enter(self):

        if self.VISITS == 0:
            print "You walk into a small single bedroom, all of the furniture"
            print "has been removed, discolouration on the walls where"
            print "pictures used to hang. It was probably a child's room."
        else:
            print "You walk into the small single bedroom."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
                    print "You leave the room and walk back onto the landing"
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bedroom2(Scene):

    hints = [
        "inspect the nightstand",
        "inspect the dresser",
        "go to the landing",
    ]

    def __init__(self):
        self.VISITS = 0
        Bedroom2.KEY = 0
        self.ATTEMPTS = 0

    def enter(self):

        if self.VISITS == 0:
            print "You walk into a large bedroom, the size of which feels off"
            print "for some reason. This room still has furniture. A large"
            print "dresser on the opposite wall in the left corner. To the"
            print "right under the window is a double bed with a nightstand on"
            print "one side. The walls in this room are wood panelled."
        else:
            pass

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "inspect the nightstand":
                    print "The nightstand has a drawer at the top and shelf"
                    print "space underneath. The shelf holds a couple of crime"
                    print "novels, covers and corners well thumbed. You open"
                    print "the drawer and find sleeping tablets and a matchbox"
                    print "with an old logo on it. You have not seen that logo"
                    print "in some time so you decide to pick up the matchbox."
                    print "You shake it and something with some weight moves"
                    print "around inside... you slide the matchbox open and"
                    print "find a key."
                    if Bedroom3.DOOR_TRIES >= 1:
                        print "Maybe this is for that locked door?"
                    else:
                        print "You put the key in your pocket."
                    Bedroom2.KEY = 1
                    self.hints.remove("inspect the nightstand")
                    pass
                elif choice == "inspect the dresser":
                    print "You look over the dresser and you can see the dust"
                    print "has been disturbed. You try to pull open a stiff"
                    print "drawer but the whole dresser slides. You look down"
                    print "at the legs and find they are sat on furniture"
                    print "gliders. Why would you want to move a dresser that"
                    print "much?"
                    self.hints.remove("inspect the dresser")
                    self.hints.append("move the dresser")
                    continue
                elif choice == "move the dresser":
                    print "You slide the dresser away from the wall where you"
                    print "then find the wood panelling has been cut away to"
                    print "reveal a short door that comes up to waist"
                    print "height. The wood looks thick and heavy, and it is"
                    print "locked with a number pad."
                    self.hints.remove("move the dresser")
                    self.hints.append("try the number pad")
                    continue
                elif choice == "try the number pad":
                    print "You crouch in front of the door and look at the"
                    print "number pad."
                    if self.ATTEMPTS == 0:
                        print "You recognise the type of lock, it should be a"
                        print "%d digit code." % len(girl.code)
                    print "*** NOTE: Enter C to go back to the room ***"
                    while True:
                        if self.ATTEMPTS >= 10 and self.ATTEMPTS % 5 == 0:
                            if Bedroom3.NAME_KNOWN == 1:
                                print "You need to keep going for %s!" % girl.name
                                print "What if her captor user her name as the code?"
                                if self.ATTEMPTS >= 30:
                                    print "*** HINT ***"
                                    print "============="
                                    print "  1   2   3  "
                                    print "     ABC DEF "
                                    print "  4   5   6  "
                                    print " GHI JKL MNO "
                                    print "  7   8   9  "
                                    print "PQRS TUV WXYZ"
                                    print "============="
                            else:
                                print "Maybe there are more clues in the house?"

                        else:
                            pass

                        digits = raw_input("# ")

                        if digits == girl.code:
                            print "The lock clicks as you punch in the"
                            print "code and you cautiously push the heavy"
                            print "door open, revealing a staircase."
                            return 'loft'
                        elif digits == "C" or digits == "c":
                            print "You leave the lock and turn your"
                            print "attention back to the room."
                            return 'bedroom_2'
                        elif not digits:
                            continue
                        else:
                            print "That was not the code, try again."
                            self.ATTEMPTS += 1
                            continue

                elif choice == "go to the landing":
                    print "You leave the room and walk back onto the landing"
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bedroom3(Scene):

    hints = [
        "go to the landing",
    ]

    def __init__(self):
        self.VISITS = 0
        Bedroom3.DOOR_TRIES = 0
        Bedroom3.NAME_KNOWN = 0

    def enter(self):

        if Bedroom2.KEY == 0:
            print "The door to this room is locked."
            Bedroom3.DOOR_TRIES = 1
            return 'landing'
        elif Bedroom2.KEY == 1:
            print "You take the key that you found and put it in the door."
            print "The lock clicks, you turn the handle, and open the door."
            Bedroom3.DOOR_TRIES = 2
        else:
            pass

        if self.VISITS == 0:
            print "You could not have imagined that this would be the scene."
            print "The walls are covered in newspaper clippings and"
            print "photographs. The articles are about a girl who disappeared"
            print "ten years ago, not long after you had joined the force. She"
            print "went missing outside of her home, no one had seen her since."
            print "Her name was %s." % girl.name
            print "The photographs... they are of her... most around the age"
            print "she was when she went missing but some... some of them are"
            print "of her older than that... and one of them... one of them"
            print "was taken outside this house. What else are you going to"
            print "find here? Was she held here? Is she still here?"
            Bedroom3.NAME_KNOWN = 1
        else:
            print "You return to the large bedroom with all of the clippings."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
                    print "You leave the room and walk back onto the landing"
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bedroom4(Scene):

    hints = [
        "go to the landing",
    ]

    def enter(self):

        if self.VISITS == 0:
            print "Walking into a bedroom at the front right of the house you"
            print "again find no furnishings. A slight crack in the window has"
            print "made this room feel much colder than the rest of the house."
            print "You gaze around but see nothing of interest."
        else:
            print "You walk into the bedroom at the front right of the house."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
                    print "You leave the room and walk back onto the landing"
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bathroom(Scene):

    hints = [
        "go to the landing",
    ]

    def enter(self):

        if self.VISITS == 0:
            print "You walk into a bathroom, dark and damp, the window has"
            print "been covered with black bags to block the light coming in."
            print "Although the rest of the house looks like it has been"
            print "untouched for some time, this room looks like it's been"
            print "used much more recently. There's a toothbrush in a glass by"
            print "the sink, and signs of moisture in the bath as if someone"
            print "has showered here recently..."
        else:
            print "You walk into the bathroom. There's nothing more to see"
            print "here."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
                    print "You leave the room and walk back onto the landing"
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Loft(Scene):

    def enter(self):
        if Bedroom3.NAME_KNOWN == 1:
            print "You rush up the stairs and into a fresh, clean, well"
        else:
            print "You ease up the stairs and into a fresh, clean, well"

        print "decorated room that stands in stark contrast to the rest of"
        print "the house you just came through."
        print "You look around the room, there are no windows but lots of"
        print "lamps and fairy lights flood your eyes with light that you"
        print "need to adjust to after the dimness of the rooms below."

        print "In the corner you spot a bed covered with blankets. The"
        print "slightest of movement of the covers rising and falling tells"
        print "you that someone is under them."

        if Bedroom3.NAME_KNOWN == 1:
            print "Your heart races, is she still here? Still alive?"
            print 'You shout, "%s", and rush to the bed' % girl.name.upper()
            print "It's her, you're sure of it. You try to wake her."
        else:
            print "Is someone being kept here? Who is it?"
            print "You stride over to the bed."
            print "You find a teenage girl lying in the bed, barely breathing."
            print "You try to rock her awake and start checking her vitals."

        print "\n\nYou do not notice that the wardrobe behind you has opened."
        print "You do not notice that a man has stepped out of it."
        print "You do notice though when he cocks his gun. You wheel around"
        print "and find it levelled at your chest.\n\n"

        print 'The Man: "Help her. Or you\'ll both be dead."'

        return 'finished'

class Finished(Scene):

    def enter(self):
        print "=" * 40
        print "Thank you for playing along with this interactive story."
        print "=" * 40
        exit(0)

class Map(object):

    scenes = {
        'opening': Opening(),
        'outside': Outside(),
        'porch': Porch(),
        'hallway': Hallway(),
        'reception': Reception(),
        'lounge': Lounge(),
        'kitchen': Kitchen(),
        'dining_room': DiningRoom(),
        'landing': Landing(),
        'bedroom_1': Bedroom1(),
        'bedroom_2': Bedroom2(),
        'bedroom_3': Bedroom3(),
        'bedroom_4': Bedroom4(),
        'bathroom': Bathroom(),
        'loft': Loft(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
