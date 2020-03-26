from SPARQLWrapper import SPARQLWrapper, JSON, POST, DIGEST

namespace = "kb"
sparql = SPARQLWrapper("http://localhost:9999/blazegraph/namespace/" + namespace + "/sparql")


#SELECT all triples in your graph
sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    SELECT *
    WHERE {?s ?p ?o}
    LIMIT 20
""")
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
        print(result["p"]["value"])

print
#SELECT all the interest of Cade
sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    SELECT * 
    WHERE {
        ex:Cade ex:interest ?interest.
    }
""")
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["interest"]["value"])

print
#SELECT the city and country of where Emma lives
sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    SELECT DISTINCT ?city ?country 
    WHERE {
        ex:Emma ex:address ?address.
        ?address ex:city ?city.
        ?address ex:country ?country.
    }
""")
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["country"]["value"])
    print(result["city"]["value"])

print
#SELECT only people who are older than 26 
sparql.setQuery("""
    PREFIX ex: <http://example.org/> 
	PREFIX foaf: <http://xmlns.com/foaf/0.1/> 

    SELECT ?name ?age
    WHERE {
        ?person foaf:name ?name.
        ?person ex:age ?age.
        FILTER(?age > 26)
    }
""")
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["name"]["value"] + " " + result["age"]["value"])


print
#SELECT everyone who graduated with a Bachelor Degree
sparql.setQuery("""
    PREFIX ex: <http://example.org/> 

    SELECT DISTINCT ?name ?level
    WHERE {
        ?person foaf:name ?name.
        ?person ex:degree ?degree.
        ?degree ex:degreeLevel ?level.
        FILTER(?level = "Bachelor").
    }
""")
sparql.setReturnFormat(JSON)

results = sparql.query().convert() 

for result in results["results"]["bindings"]:
    print(result["name"]["value"] + " " + result["level"]["value"])


print 
#DELETE DATA that Cade is interest Photography
sparql.method = 'POST'
sparql.setQuery("""
    PREFIX ex: <http://example.org/>

    DELETE WHERE {
        ex:Cade ex:interest ex:Photography
    }
""")

sparql.setQuery("""
    PREFIX ex: <http://example.org/>
    SELECT * 
    WHERE {
        ex:Cade ex:interest ?interest.
    }
""")
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["interest"]["value"])


print
#INSERT DATA 
sparql.method = 'POST'
sparql.setQuery("""
    PREFIX ex: <http://example.org>
    INSERT DATA {
        ex:Sergio a foaf:Person.
    }
""")
