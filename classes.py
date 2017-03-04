from sys import exit

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

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
        print "Opening."
        return 'finished'

class Outside(Scene):

    def enter(self):
        pass

class Porch(Scene):

    def enter(self):
        pass

class Hallway(Scene):

    def enter(self):
        pass

class Reception(Scene):

    def enter(self):
        pass

class Lounge(Scene):

    def enter(self):
        pass

class Kitchen(Scene):

    def enter(self):
        pass

class DiningRoom(Scene):

    def enter(self):
        pass

class Landing(Scene):

    def enter(self):
        pass

class Bedroom1(Scene):

    def enter(self):
        pass

class Bedroom2(Scene):

    def enter(self):
        pass

class Bedroom3(Scene):

    def enter(self):
        pass

class Bedroom4(Scene):

    def enter(self):
        pass

class Bathroom(Scene):

    def enter(self):
        pass

class Loft(Scene):

    def enter(self):
        pass

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
