import sys

#create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI',
    }

#Create a basic set of states and some cities in them
cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
    }

#Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities
print '-' * 10
print "NY state has :" , cities ['NY']
print "OR state has :" , cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: " , states['Michigan']
print "Florida's abbreviation is : " , states['Florida']

#do it by using the state then cities dict
print '-' * 10
print "Michigan has : ", cities[states['Michigan']]
print "Florida has : ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abbrev)

#print every city in state
print '-' * 10
for state, city in cities.items():
    print "%s state has %s city" % (state, city)

#print now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print 'sorry no texas'

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is %s : " %city

