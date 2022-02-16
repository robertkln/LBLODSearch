# LBLODSearch
Minimal implementation of a word search function for Lokale Besluiten als geLinkte Open Data.

## Explanation of implementation
This implementation allows for searching through entities of the class besluit:Besluit. It assigns points for each element in the data (e.g. title and description) which contains the keyword. All results with a score > 1 are then returned to the user.

##  Endpoints available
- "/"
> A basic frontend allowing for searching and pagination of a single keyword

- "/search"
> An API allowing for making searches and pagination for a single keyword

- "/docs"
> OpenAPI documentation for the /search API 

## How to run

### Docker

> docker build -t lblodsearch . 

> docker run -d --name mysearch -p 80:80 lblodsearch

Open browser at localhost:80

### Demo

Live demo running at: http://141.144.193.89/

