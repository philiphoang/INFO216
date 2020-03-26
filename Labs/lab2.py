from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF, XSD
from rdflib.collection import Collection

g = Graph()

n = Namespace("http://example.org/")

#Cade lives in 1516 Henry Street, Berkely, California, 94709, USA
g.add((n.Cade, n.street, Literal("1516 Henry Street")))
g.add((n.Cade, n.city, n.Berkely))
g.add((n.Cade, n.state, n.California))
g.add((n.Cade, n.zipcode, Literal("94709")))
g.add((n.Cade, n.country, n.USA))

#FOAF.based_near?


#He has a B.Sc. in biology from the University of California, Berkely from 2011
cade_degree = BNode()
g.add((n.Cade, n.degree, cade_degree))
g.add((cade_degree, n.degreeLevel, Literal("Bachelor")))
g.add((cade_degree, n.interest, n.Biology)) #Change n.interest
g.add((cade_degree, n.university, n.University_of_California)) #Bytt ut place
g.add((cade_degree, n.city, n.Berkely))
g.add((cade_degree, n.year, Literal("2011")))


#His interests include birds, ecology, the enviornment, photography and travelling
cade_interest = BNode()
g.add((n.Cade, n.interest, cade_interest))
Collection(g, cade_interest,
    [n.birds, n.ecology, n.environment, n.photography, n.travelling])


#He has visited Canada and France
cade_visited = BNode()
g.add((n.Cade, n.visited, cade_visited))
Collection(g, cade_visited,
    [n.Canada, n.France])

#Emma Dominguez lives in Carrer de la Guardia Civil 20, 46020, Valencia, Spain
g.add((n.Emma, n.street, Literal("Carrer de La Guardia Civil 20")))
g.add((n.Emma, n.city, n.Valencia))
g.add((n.Emma, n.zipcode, Literal("46020")))
g.add((n.Emma, n.country, n.Spain))


#She has a M.Sc. in chemistry from the University of Valencia from 2015
emma_degree = BNode()
g.add((n.Cade, n.degree, cade_degree))
g.add((emma_degree, n.degreeLevel, Literal("Master")))
g.add((emma_degree, n.interest, n.Chemistry)) #CHange n.interest
g.add((emma_degree, n.university, Literal("University of Valencia")))
g.add((emma_degree, n.year, Literal("2001")))


#Her areas of expertise include waste management, toxic waste, air pollution
emma_expertise = BNode()
g.add((n.Emma, n.expertise, emma_expertise))
Collection(g, emma_expertise,
    [n.waste_management, n.toxic_waste, n.air_pollution])


#Her interests include bike riding, music and travelling
emma_interest = BNode()
g.add((n.Emma, n.expertise, emma_interest))
Collection(g, emma_interest,
    [n.bike_riding, n.music, n.travelling])


#She has visited Portugal, Italy, France, Germany, Denmark and Sweden
emma_visited = BNode()
g.add((n.Emma, n.expertise, emma_visited))
Collection(g, emma_visited,
    [n.Portugal, n.Italy, n.France, n.Germany, n.Denmark, n.Sweden])


#Cade knows Emma
g.add((n.Cade, FOAF.knows, n.Emma))


#They met in Paris in August 2014
met = BNode()
g.add((n.Cade, n.met, met))
g.add((met, FOAF.person, n.Emma))
g.add((met, n.city, n.Paris))
g.add((met, n.year, Literal("2014")))

#Two-ways
g.add((n.Cade, n.partOf, n.Meeting1))
g.add((n.Emma, n.partOf, n.Meeting1))
g.add((n.meet, RDF.type, meeting))
g.add((meeting, n.city, n.Paris))


#Print to console
print(g.serialize(format="turtle").decode())


#Write graph to file
g.serialize(destination="triples.txt", format="turtle")
