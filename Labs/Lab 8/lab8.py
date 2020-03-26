import owlrl
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD, FOAF, OWL

g = Graph()

# Namespaces
ex = Namespace("http://example.org/")
dbp = Namespace("http://dbpedia.org/resource/United_States")
geo = Namespace("http://sws.geonames.org/")
schema = Namespace("https://schema.org/")
akt = Namespace("http://www.aktors.org/ontology/portal#")
vcard = Namespace("http://www.w3.org/2006/vcard/ns#")
foaf = Namespace("http://xmlns.com/foaf/0.1/Person")

g.bind("ex", ex)
g.bind("owl", OWL)

g.bind("foaf", foaf)
g.bind("dpb", dbp)
g.bind("geo", geo)
g.bind("vcard", vcard)

# RDFS Tasks from last time.
g.add((ex.Cade, ex.degreeFrom, ex.University_of_California))
g.add((ex.Emma, ex.degreeFrom, ex.University_of_Valencia))
g.add((ex.Cade, ex.degreeSubject, ex.Biology))
g.add((ex.Emma, ex.degreeSubject, ex.Chemistry))
g.add((ex.University_of_California, RDF.type, ex.University))
g.add((ex.University_of_Valencia, RDF.type, ex.University))
g.add((ex.University, RDFS.subClassOf, ex.Higher_Education_Institution))
g.add((ex.expertise, RDFS.range, ex.Subject))
g.add((ex.expertise, RDFS.domain, FOAF.Person))
g.add((ex.degreeSubject, RDFS.subPropertyOf, ex.expertise))
g.add((ex.graduated, RDFS.range, ex.Higher_Education_Institution))
g.add((ex.graduated, RDFS.domain, FOAF.Person))
g.add((ex.degreeFrom, RDFS.subPropertyOf, ex.graduated))
g.add((ex.Biology, RDFS.label, Literal("Biology", lang="en")))
g.add((ex.Biology, RDFS.label, Literal("La Biologie", lang="fr")))
g.add((ex.Biology, RDFS.comment, Literal("Biology is a natural science concerned with the study of life and living organisms, including their structure, function, growth, evolution, distribution, identification and taxonomy.")))
g.add((ex.Chemistry, RDFS.label, Literal("Chemistry", lang="en")))
g.add((ex.Chemistry, RDFS.label, Literal("La Chimie", lang="fr")))
g.add((ex.Chemistry, RDFS.comment, Literal("Chemistry is a branch of physical science that studies the composition, structure, properties and change of matter.", lang="en")))

# Write OWL triples here

#Task 1

#Cade and Emma are two different persons
g.add((ex.Cade, OWL.differentFrom, ex.Emma))

#The country USA above is the same as the DBpedia resource  http://dbpedia.org/resource/United_States (dbr:United_States) and the GeoNames resource http://sws.geonames.org/6252001/ (gn:6252001)
g.add((dbp.United_States, OWL.sameAs, geo + URIRef("6252001")))

#The person class (the RDF type the Cade and Emma resources) in your graph is the 
# same as FOAF's, schema.org's and AKT's person classes 
# (they are http://xmlns.com/foaf/0.1/Person, http://schema.org/Person, and http://www.aktors.org/ontology/portal#Person, respectively.
g.add((ex.Person ,OWL.equivalentClass, foaf.Person)) #Literal("http://xmlns.com/foaf/0.1/Person")
g.add((ex.Person ,OWL.equivalentClass, schema.Person)) #Literal("http://schema.org/Person")
g.add((ex.Person ,OWL.equivalentClass, akt.Person)) #Literal("http://www.aktors.org/ontology/portal#Person")

#Nothing can be any two of a person, a university, or a city at the same time.
g.add((ex.Person, OWL.disjointWith, ex.Person)) 
#g.add((ex.University, OWL.disjointWith. ex.University))
g.add((ex.city, OWL.disjointWith, ex.city))

#The property you have used in your RDF/RDFS graph to represent that 94709 is the US zip code of Berkeley, 
# California in US is a subproperty of VCard's postal code-property (http://www.w3.org/2006/vcard/ns#postal-code).
g.add((ex.California, OWL.sameAs, geo + URIRef("94709")))
g.add((geo + URIRef("94709"), OWL.equivalentProperty, vcard.postalCode))

#No two US cities can have the same postal code
g.add((ex.city, OWL.differentFrom, OWL.city)) #???

#The property you have used for Emma living in Valencia is the same property as FOAF's based near-property (http://xmlns.com/foaf/0.1/based_near)
# and it is the inverse of DBpedia's hometown property (http://dbpedia.org/ontology/hometown, dbo:hometown).
g.add((ex.livingIn, OWL.equivalentProperty, foaf.based_near))
g.add((foaf.living, OWL.inverseOf, dbp.hometown))


#Task 2
g.add((ex.Cade, ex.married, ex.Mary)) #1
g.add((ex.Cade, ex.livesWith, ex.Mary)) #2
g.add((ex.Cade, ex.sibling, ex.Andrew)) #3
g.add((ex.Cade, ex.sibling, ex.Anna)) #4
g.add((ex.Cade, ex.hasFather, ex.Bob)) #5
g.add((ex.Bob, ex.fatherOf, ex.Cade)) #6


#1
g.add((ex.married, RDF.type, OWL.SymmetricProperty)) 
g.add((ex.married, RDF.type, OWL.FunctionalProperty))
g.add((ex.married, RDF.type, OWL.IrreflexiveObjectProperty))

#2
g.add((ex.livesWith, RDF.type, OWL.SymmetricProperty))
g.add((ex.livesWith, RDF.type, OWL.FunctionalProperty))
g.add((ex.livesWith, RDF.type, OWL.IrreflexiveObjectProperty))
g.add((ex.livesWith, RDF.type, OWL.TransitiveProperty)) #???

#3
g.add((ex.sibling, RDF.type, OWL.TransitiveProperty))
g.add((ex.sibling, RDF.type, OWL.SymmetricProperty)) 
g.add((ex.sibling, RDF.type, OWL.IrreflexiveObjectProperty))

#4
g.add((ex.hasFather, RDF.type, OWL.IrreflexiveObjectProperty))
g.add((ex.hasFather, RDF.type, OWL.AsymmetricProperty)) 
g.add((ex.hasFather, RDF.type, OWL.FunctionalProperty))

#5
g.add((ex.fatherOf, RDF.type, OWL.IrreflexiveObjectProperty))
g.add((ex.fatherOf, RDF.type, OWL.AsymmetricProperty)) 


#Task 3

# These three lines add inferred triples to the graph.
owl = owlrl.CombinedClosure.RDFS_OWLRL_Semantics(g, False, False, False)
owl.closure()
owl.flush_stored_triples()

print(g.serialize(format="turtle").decode())

g.serialize(destination="owl_triples.txt", format="turtle")
