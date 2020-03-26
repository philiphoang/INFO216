from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD, RDFS
import owlrl.RDFSClosure

g = Graph()
ex = Namespace("http://example.org/")
g.bind("foaf", FOAF)
g.bind("ex", ex)


g.add((ex.Cade, ex.degreeFrom, ex.University_of_California))
g.add((ex.Emma, ex.degreefrom, ex.University_of_Valencia))
g.add((ex.Cade, ex.degreeSubject, ex.Biology))
g.add((ex.Emma, ex.degreeSubject, ex.Chemistry))

#Define Cade and Emma as Person)
g.add((ex.Cade, RDF.type, FOAF.Person))
g.add((ex.Emma, RDF.type, FOAF.Person))

#University of California and University of Valencia are both Universities
g.add((ex.University_of_California, RDF.type, ex.University))
g.add((ex.University_of_Valencia, RDF.type, ex.University))

#All universities are higher education instituttions (HEIs)
g.add((ex.University, RDFS.subClassOf, ex.Higher_Education_Institution))

#That a person has a degree in a subject means that the person has expertise in that subject
g.add((ex.degreeSubject, RDFS.subPropertyOf, ex.expertise))

#Only persons can have an expertise, 
g.add((ex.expertise, RDFS.domain, FOAF.Person)) 

# and what they have expertise in is always a subject
g.add((ex.expertise, RDFS.range, ex.degreeSubject)) #Ikke nodvendig? Linje 28

#Having a degree from a HEI means that you have also graduated from that HEI
g.add((ex.degreeFrom, RDFS.subPropertyOf, ex.graduatedFrom))

g.add((ex.graduatedFrom, RDFS.range, ex.Higher_Education_Institution))

#Only persons can graduate from a HEI
g.add((ex.graduatedFrom, RDFS.domain, FOAF.Person))


g.add((ex.Biology, RDFS.label, Literal("Biology")))


rdfs = owlrl.RDFSClosure.RDFS_Semantics(g, False, False, False)
rdfs.closure()
rdfs.flush_stored_triples()


universities = g.query("""
PREFIX ex: <http://example.org/>
ASK {
    ex:University_of_California rdf:type ex:Higher_Education_Institution.
} 
""")
print(bool(universities))




