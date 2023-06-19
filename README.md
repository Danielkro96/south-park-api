# south-park-api
This application features an API that retrieves a random episode from the popular series South Park.

It is built using the Flask framework and powered by a Gunicorn WSGI server.

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
