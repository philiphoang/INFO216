from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF, XSD
from rdflib.collection import Collection

g = Graph()

#Read from file and save to Graph g
g.parse(location="triples.txt", format="turtle")

#Write to console
print(g.serialize(format="turtle").decode())


#Remove triples
#Graph.remove((n.Mary, None, None))
#Graph.remove((None, None, n.Mary)) Cade married to Mary

#Iterate
print("------------------------------------------")

for s,p,o in g.triples( (n.Emma, None, None) ):
   print (s,p,o)


#Loop only predicate
for s,p,o in g.triples( (None, ..., None) ):
   print (s,p,o)
