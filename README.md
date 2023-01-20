# south-park-api
An api that retrieves a random episode of the series South Park. 

This application was builded for fun with Flask framework

## Can also: 
- retrieve a random episode from a specific season.
- retrieve a random episode from a range of seasons.

## Routes

> **GET /** 
        Retrieve a random episode.
   
> **GET /random/season/<specific_season>** 
        Retrieve Episode information
  
> **GET /random/between/<start_season>-<end_season>** 
        Retrieve Season information with episodes list
