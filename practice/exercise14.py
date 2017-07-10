from sys import argv

script ,user_name = argv
prompt ='>'

print "Hi %s,Im the %s script." %(user_name,script)
print "id like to ask you a few questions."
print "do you like me %s" %user_name
likes = raw_input(prompt)

print "where do you live%s" %user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer =raw_input(prompt)

print """
alright,so u said %r about
you like in %r.not sure
and u have a %r computer.nice.
"""%(likes,lives,computer)