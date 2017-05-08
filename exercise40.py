#objects and all
class Song(object):
	def __init__(self,lyrics):
		self.lyrics =lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday =Song(["happy birthday to you","I dont want to get sued","so I'll stop right here"])

bulls_on_parade = Song(["they rally arounf the family","with ockts full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()