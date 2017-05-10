from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "This is yet not configured.Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n__________"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "YOU DIED."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips))]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print """
        The Gothons Planet percal #25 have invade ypur ship and destroyed.
        your entire crew.You are the last surviving member and your last
        mission is to get the neutron destruct bomb from Armory
        put it in the bridges and blow the ship after getting into an
        escape pod.\n
        You're running down the corridor to weapons Armory when a 
        Gothon jumps out,red scaly skin ,dark grimy teeth and evil clown costume.
        flowing around his hate filled body.He's blocking the door to the Armory and about to pu
        pull a weapon to blast you."""

        action = raw_input('>')
        if action == "shoot!":
            print"""
            Quick on the draw you yank out your blaster and fire it at the Gothon
            HIs clown costume is flowing and moving around his body,which throws
            off your aim.Your laser hits his costumebut misses him entirely.This
            completely ruins his brand new costunmes his mother bight him,which makes him fl
            in the rage and blast you repeatedly in the face until
            you are dead.YThen he eats you."""
            return 'death'
        elif action == "dodge":
            print """
            like a worlds class boxer you dodge,weave,slip and slide right
            as the Gothon blaster cranks a laer past your head.
            In the middle of your artful dodge your foot slips and yu 
            bang your head on the metal wall and pass out.
            you wake up shortly ater only to die as the Gothhon stomps on
            you head and eats you."""
            return 'death'
        elif action == "tell a joke":
            print"""
            Lucky for you they made you learn gothon insults in the cademy 
            you tell the Gothon joke you knoe
            blah,blah,blah,blah
            The gothon stops ,tries no to laughhand then bursts out lauh=ghing and cant move
            while he's laughing you run up and shoot him square in the head
            putting him down,then jump through the waepon armory door."""
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
