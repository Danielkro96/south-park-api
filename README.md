# south-park-api
An api that retrieves a random episode of the series South Park. 

This application was built for fun with a Flask framework and a Gunicorn WSGI server.

### Can also: 
- retrieve a random episode from a specific season.
- retrieve a random episode from a range of seasons.

### Routes

> **GET /random** 
        Retrieve a random episode.
   
> **GET /random/season/<specific_season>** 
        Retrieve a random episode from a specific season
  
> **GET /random/between/<start_season>-<end_season>** 
        Retrieve a random episode from a range of seasons
