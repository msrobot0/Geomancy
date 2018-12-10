import random,re
import time

interpretations ={"Conjunctio":"neutral","Carcer":"negative","Tristitia":"negative","Puer":"negative","Caput Draconis":"neutral","Fortuna Major":"positive","Fortuna Minor":"positive","Albus":"positive","Acquisitio":"positove","Populus":"neutral","Laetitia":"positive","Puella":"positive","Amissio":"negative","Vita":"neutral","Rubeus":"negative","Caudia Draconis":"negative"}

signs = {(1, 1, 2, 2): 'Fortuna Minor', (2, 2, 1, 1): 'Fortuna Major', (2, 1, 1, 2): 'Conjunctio', (2, 2, 1, 2): 'Albus', (2, 2, 2, 1): 'Tristitia', (1, 2, 1, 1): 'Puer', (2, 2, 2, 2): 'Populus', (2, 1, 1, 1): 'Caput Draconis', (1, 2, 2, 1): 'Carcer', (1, 2, 1, 2): 'Amissio', (1, 1, 1, 1): 'Vita', (2, 1, 2, 2): 'Rubeus', (2, 1, 2, 1): 'Acquisitio', (1, 2, 2, 2): 'Laetitia', (1, 1, 2, 1): 'Puella',(1, 1, 1, 2):'Caudia Draconis'}

def toOrdinal(v):
    tmp= [None,"First","Second","Third","Fourth"]
    try:
	ord =  tmp[v]
	if ord is None:
		raise Exception("")
	return ord
    except:
	raise Excepition("No ordinal for %s" % v)
  

def castThePoints(v):
	
	if v%2 == 0:
		return 2
	else:
		return 1

def printDetails(points,name):
		x = 1
		for m in points:
			print "%s %s %s" % (toOrdinal(x),name,signs[tuple(m)],)
			x+= 1
	
def combinePoints(points):
	all = []
	for x in xrange(0,len(points),2):
		tmp = []
		for y in xrange(0,4):
			tmp.append(castThePoints(points[x][y] + points[x+1][y]))
		all.append(tmp)
	return all 
question = raw_input("What is your question? ")
seed = int(int(time.time()*1000.0)/len(question))
random.seed(seed)
mothers =  map((lambda y: map((lambda x: castThePoints(int(random.random()*10))),range(0,4))),range(0,4))
daughters = []
for x in xrange(0,4):
	daughters.append( [mothers[0][x],mothers[1][x],mothers[2][x],mothers[3][x]])
nieces =combinePoints(mothers)+combinePoints(daughters)
witnesses = combinePoints(nieces[:2])+combinePoints(nieces[2:])
judge = combinePoints(witnesses)
print
print question
sign = signs[tuple(judge[0])]
meaning = interpretations[sign]

print "You cast the %s. That is %s" % (sign, meaning)

more  = "Q"
while  not (more.startswith("Y") or more.startswith("N")):
	more =raw_input("Would you like a detail of your geomatic chart? Y/N? ")
	try:
		more = more[0].rstrip('\n').upper()
	except:
		pass
	if more.startswith("Y"):
		printDetails(mothers,"mothers")
		printDetails(daughters,"daughters")
		printDetails(nieces,"nieces")
		printDetails(witnesses,"witnesses")
		printDetails(judge,"judge")
	


