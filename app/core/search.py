import requests

headers = {'Accept':'application/sparql-results+json,*/*;q=0.9'}
post = lambda x: requests.post('https://qa.centrale-vindplaats.lblod.info/sparql', data={'query':x}, verify=False, headers=headers)
resultize = lambda x: post(x).json()['results']['bindings']

def shorten(text:str, length: int = 500):
    """Function for shortening descriptions """
    if len(text) > length:
        return(text[0:length] + "...")
    return(text)

def search_meta(keyword):
    """Function for lookin up the amount of search results for a keyword """
    query = """ SELECT (COUNT(*) as ?count) WHERE { SELECT DISTINCT ?uri ?title ?desc ?resultaat WHERE {
               ?uri a <http://data.vlaanderen.be/ns/besluit#Besluit> .
               ?uri <http://data.europa.eu/eli/ontology#description> ?desc .
               ?uri <http://data.europa.eu/eli/ontology#title> ?title ."""
    query += f"BIND(contains(?desc, \"{ keyword }\") + contains(?title, \"{ keyword }\") as ?resultaat)"
    query += f"filter(?resultaat > 0)}} }}"
    return({"amount":resultize(query)[0].get('count').get('value')})

def search(keyword, results, page):
    """Function for searching and returning results for keyword matches in a besluit:Besluit"""

    # Calculate the offset by multiplying the page with the number of results
    # Example: 20 results per page, page 3 requested: 3 * 20 = 60 offset
    calculated_offset = results * page 

    query = """ SELECT DISTINCT ?uri ?title ?desc ?resultaat WHERE {
               ?uri a <http://data.vlaanderen.be/ns/besluit#Besluit> .
               ?uri <http://data.europa.eu/eli/ontology#description> ?desc .
               ?uri <http://data.europa.eu/eli/ontology#title> ?title ."""
    query += f"BIND(contains(?desc, \"{ keyword }\") + contains(?title, \"{ keyword }\") as ?resultaat)"
    query += f"filter(?resultaat > 0)}} order by ?uri limit { results } offset { calculated_offset }"
    raw_results = resultize(query)

    return({"results":[{"uri":item.get("uri").get("value"),
                "title":item.get("title").get("value"),
                "description":item.get("desc").get("value").strip(),
                "description_short":shorten(item.get("desc").get("value").strip()),
                "datapoints":item.get("resultaat").get("value")} for item in raw_results]})