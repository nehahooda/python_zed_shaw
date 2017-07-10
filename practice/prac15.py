import random

number = random.randint(1,9)
guess =0
count =0

while guess!= number and guess !="exit":
    guess = raw_input("whats your guess??")

    if guess == "exit":
        break
    guess = int(guess)
    count+=1

    if guess < number:
        print "too low :/"

    elif guess > number:
        print "too high :("
    else:
        print "YAYYYYY...you got it"
        print "AND it took you ",count,"trials :P"