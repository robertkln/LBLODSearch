from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.core.search import search, search_meta
from math import ceil

templates = Jinja2Templates(directory="app/templates")

def handle_search(request:Request, query:str, amount:int, page:int):
    if query != None:
            results = search(query, amount, page)
            results_meta = search_meta(query)
            last_page = ceil(int(results_meta['amount']) / amount)
            return(templates.TemplateResponse("result.html", {"request": request, "results": results, "meta":results_meta, "page":page, 
                                                                    "amount":amount, 'query':query, "last_page":last_page}))
    return(templates.TemplateResponse("search.html", {"request": request}))