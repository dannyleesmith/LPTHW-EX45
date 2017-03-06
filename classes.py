from sys import exit

def exit_bad_selection():
    print "Error: you should not have got to this point."
    print "Our apologies, please restart the story."
    exit(1)

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
            print "timbers. Dust clings to all services. It's clear no one"
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
        "go to the bathroom",
        "go to the front left bedroom",
        "go to the front right bedroom",
        "go to the back right bedroom",
        "go to the back left bedroom",
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
                elif choice == "go to the bathroom":
                    return 'bathroom'
                elif choice == "go to the front left bedroom":
                    return 'bedroom_1'
                elif choice == "go to the back left bedroom":
                    return 'bedroom_2'
                elif choice == "go to the back right bedroom":
                    return 'bedroom_3'
                elif choice == "go to the front right bedroom":
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
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bedroom2(Scene):

    hints = [
        "go to the landing",
        "secret door",
    ]

    def enter(self):

        print "You enter the bedroom 2 scene"

        if self.VISITS == 0:
            print "An intro statement for the first visit to the scene."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
                    return 'landing'
                elif choice == "secret door":
                    return 'loft'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Bedroom3(Scene):

    hints = [
        "go to the landing",
    ]

    def enter(self):

        print "You enter the bedroom 3 scene"

        if self.VISITS == 0:
            print "An intro statement for the first visit to the scene."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
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

        print "You enter the bedroom 4 scene"

        if self.VISITS == 0:
            print "An intro statement for the first visit to the scene."

        self.VISITS += 1

        while True:
            choice = raw_input("> ").lower()

            if choice == "hint" or choice == "hints":
                self.show_hints(self.hints)
                continue
            elif choice in self.hints:
                if choice == "go to the landing":
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
            print "by the sink, and signs of moisture in the bath as if"
            print "someone has showered here recently..."
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
                    return 'landing'
                else:
                    exit_bad_selection
            else:
                print "That option is not valid here."
                continue

class Loft(Scene):

    def enter(self):
        print "You have reached the end of our story"
        return 'finished'

class Finished(Scene):

    def enter(self):
        print "Finished."
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
