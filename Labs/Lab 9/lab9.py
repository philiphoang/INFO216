from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, FOAF, XSD, RDFS

import pandas as pd

import re

ex = Namespace("http://example.org/")
foaf = Namespace("http://xmlns.com/foaf/0.1/Person")

# Load the CSV data as a pandas Dataframe.
csv_data = pd.read_csv("task1.csv")

print(csv_data)

g = Graph()
ex = Namespace("httph://example.org/")
g.bind("ex", ex)
g.bind("foaf", foaf)


print("-----------------------------------")

# You should probably deal with replacing of characters or missing data here:
csv_data["Name"] = csv_data["Name"].str.replace(" ", "_")


# for data in csv_data.columns:
#     csv_data[data] = csv_data[data].str.replace(" ", "_")

# print(csv_data)

# Iterate through each row in order the create triples. First I select the subjects of the triples which will be the names.

for index, row in csv_data.iterrows():
    # row['Name'] selects the name value of the current row.
    subject = row['Name']

    gender = row['Gender']

    country = row['Country']

    expertises = row['Expertises']

    interests = row['Interests']

     #Continue the loop here:
    g.add((Literal(subject), RDF.type, FOAF.person))
    g.add((Literal(subject), ex.gender, Literal(gender)))



# Clean printing of end-results.
print(g.serialize(format="turtle").decode())
