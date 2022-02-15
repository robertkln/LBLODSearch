from fastapi import FastAPI, Request
from app.core.frontend import handle_search
from app.core.search import search, search_meta
from app.core.models import SearchResults
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, query: str = None, amount:int = 10, page:int = 0):
    return(handle_search(request=request, query=query, amount=amount, page=page))

@app.get("/search", response_model = SearchResults)
def search_keyword(query: str, results:int = 15, page:int = 0):
    return(search(query, results, page))
