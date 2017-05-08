#dictionaries
states ={
'Maharahtra':'MH',
'Haryana':'HY',
'Uttar Pradesh':'UP'
}


cities = {
'New Delhi': 'ND',
'Kolkata': 'KL',
'Mumbai':'MU',
'Chennai':'CH',
'Rohtak':'RK',
'Banglore':'BG'}

cities['LK']= 'Lucknow'
cities['HY']= 'Hyderabad'



print '_'*10
print "UP states has:",cities['LK']
print "HR states has:",cities['RH']

print '_'*10
print "Uttar Pradesh's abbreviation is:",states['Uttar Pradesh']
print "haryana's abbrevaition is :",states['Haryana']

print '_'*10
print "Haryana has:",cities[states['Haryana']]

print '_'*10
for states,abbrev in states.items():
  print"%s is abbreviated %s"%(state,abbrev)

print '_'*10
for abbrev,city in cities.items():
   print "%s has the city %s"%(abbrev,city)

print '_'*10
for state,abbrev in states.items():
 	print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])
 
print '_'*10
state = states.get('Texas',None)

if not state:
 	print "sorry,no texas."
city = cities.get('TX','Does not exist')
print "the ciyt for the state 'TX' is %s" %city
