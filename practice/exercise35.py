from sys import exit

def gold_room():
    print "this room is full of gold.How much do you take?"
    next = raw_input(">")
    if "0" in next or "1" in next:
    	how_much = int(next)
    else:
    	dead("man!!learn how to enter a number")

    if how_much<50:
    	print "nice..you are not greedy...you win!"
    	exit(0)
    else:
    	dead("you are greedy!bastard!")


def bear_room():
	print "ther is a bear here.."
	print "the bear has a bunch of honey"
	print "the fat bear is front of another door"
	print "how are you going to move the bear?"
	bear_moved = False
	while True:
		next = raw_input(">")

		if next == "take honey":
			dead("the bear looks at you and then slap your face off")
		elif next == "taunt bear" and not bear_moved:
			print "the bear has moved from the door,you can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("the bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no ides what that means."


def tt_room():
	print "here you see the great evil mojo jojo."
	print "he,it,whatever stares you and you go insane."
	print "do you flee for your life or eat your head?"

	next = raw_input(">")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that was tasty!")
	else:
		tt_room()

def dead(why):
	print why,"good job!"
	exit(0)

def start():
	print "you are in dark room."
	print "there is a door to your right and left."
	print "which one do you take?"

	next = raw_input(">")

	if next == "left":
		bear_room()
	elif next == "right":
		tt_room()
	else:
		dead("you stumble aroung the room until you starve.")

start()
