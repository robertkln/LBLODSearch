from pydantic import BaseModel, HttpUrl

class SearchResult(BaseModel):
    uri: str
    title: str
    description: str
    description_short:str
    datapoints:int

class SearchResults(BaseModel):
    results:list [SearchResult]