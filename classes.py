from sys import exit

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

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

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self, scene_name):
        pass
