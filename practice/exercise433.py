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
        print Death.quips[randint(0, len(self.quips)-1)]
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

class LaserWeaponArmory(Scene):
    def enter (self):
        print """
        You do a dive roll into the weapon Armory,crouch and scen the room
        forn more Gothons that might be hiding .Its dead quiet ,too quiet .
        You stand up and run to the far side of the room and find the
        neutron bomb in it container.There's a keypad lock on the box.
        and you need the code to get the bomb out.if you get the code
        wrong 10 times then the close forever and you cant 
        get the bomb.the code is 3 digits"""

        code ="%d%d%d" %(randint(1,9),randint(1,9),randint(1,9))
        guess = raw_input("[keypad]>")
        guesses =0


        while guess != code and guesses <10:
            print "BZZZZZEDDDDD!"
            guesses+=1
            guess = raw_input("[keypad]>")

        if guess == code:
            print"""
            The container clicks open and the eal breaks ,letting gas out.
            You grab the neutron bomb and run as fast as you can to the 
            bridge where yuo must place it in the right spot."""
            return 'the_bridge'
        else:
            print """
            The lock buzzes one last time and then you hear a sickening
            melting sound as the mechanism is fused together.
            You decide to sit there and finally the gothons blow up the 
            ship from their ship and you die"""
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print """
        You burst onto the Bridges with the neutron destruct bomb
        under your arm and suprise 5 gothons who  are trying to
        take control of the ship. Each of them has an even uglier 
        clown costume than the last .They haven't pulled their
        weapons out yet,as they see the active bomb under your
        arm and dont want to set it off."""

        action = raw_input(">")

        if action == "throw the bomb":
            print """
            Ina panic you throw the bomb at the group of gothons.
            and make a leap for the door.Right as you drop it a
            Gothon shoots you right in the back killing you."""

            return 'death'
        elif action =="slowly place the bomb":
            print"""
            you point your blaster at the bomb under your arm 
            and the gothons put thier hands up and start to sweat.
            you inch backward to the doo ,open it and then carefully 
            place the bomb on the floor,pointing your blast at it
            you then jump back through the door,punch close button
            and blast the lock so the othons cant get out.
            now the bomb is placed you run to the escape pod to
            get off this tin can"""
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return "the_bridge"

class EscapePod(Scene):

        def enter(self):
            print """
            you rush through the ship desperately trying to make it to 
            the escape pod before the whole ship explodes.it seems like
            hardly any Gothons are on the ship,so your run is clear of interference.
            You get to the chamber with the escape pods,and 
            now need to pick up =one to take.Some of them might be damaged
            byut you dont have time to look.there 5 pods,which one
            do you take??"""

            good_pod =randint(1,5)
            guess = raw_input("[pod#]>")

            if int (guess)!=good_pod:
                print" you jump into pod %s and hit he eject button." %guess
                print"""
                the pod escpes out nto the void space ,then
                implodes as the hull ruptures,crushing your body
                into jam jelly"""
                return "death"
            else:
                print "you jump into pod %s and hit the eject button."%guess
                print"""
                the pod easily slides out into the space heading to
                the planet below.as it flies to the planet,you look
                back and see your ship implode then explode like a 
                briht star,taking out the gothon ship at the same 
                time,YOU WON!!!!"""
                return 'finished'


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

a_map =Map('central_corridor')
a_game =Engine(a_map)
a_game.play()