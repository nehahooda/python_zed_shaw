from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This is yet not configured.Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n__________"
            next_scene_name =current_scene.enter()
            current_scene =self.scene_map.next_scene(next_scene_name)
class Deat(Scene):
    quips = [
        "YOU DIED."
    ]
    def enter(self):
        print Death.quips[randint(0,len(self.quips))]
        exit(1)


