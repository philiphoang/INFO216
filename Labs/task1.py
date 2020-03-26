from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, FOAF

g = Graph() #Same as a database, graph with nodes


#Rough method, make a URIref for each node
cade = URIRef("http://example.org/Cade")
married = URIRef("http://example.org/married")
mary = URIRef("http://example.org/Mary")
g.add((cade, married, mary))

#Task 1, better method
n = Namespace("http://example.org/")

#Cade is married to Mary
g.add((n.Cade, FOAF.married, n.Mary))
#g.add((cade, RDF.type, FOAF.person))


#The capital of France is Paris
g.add((n.Paris, n.capital, n.France))

#Cade is 27 years old
g.add((n.Cade, n.age, Literal("27"))) #Literal() brukes om raw data type

#26 years is the age of Mary
g.add((n.Mary, n.age, Literal("26")))

#Marys interests include hiking, chocolate and biology
g.add((n.Mary, n.interest, n.Hiking)) #Riktig er FOAF.interest
g.add((n.Mary, n.interest, n.Chocolate))
g.add((n.Mary, n.interest, n.Biology))

#Mary is a student
g.add((n.Mary, n.occupation, n.Student))

#Paris is a City in France
#g.add((n.Paris, n.partOf, n.France) 

#Correction
g.add((n.Paris, RDF.type, n.City))
g.add((n.Paris, n.locatedIn, n.France))

#Cade and Mary are kind people
g.add((n.Cade, n.personality, n.Kind))
g.add((n.Mary, n.personailty, n.Kind))
g.add((n.Cade, RDF.type, FOAF.Person))
g.add((n.Mary, RDF.type, FOAF.Person))


print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))