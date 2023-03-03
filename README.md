<p align="center">
  <h3 align="center">Survey Maker API</h3>
  <p align="center">
    An API for create and respond surveys 
    <br>
    <a href="https://github.com/IsmaelBortoluzzi/Survey-Maker-API/issues/new?template=bug.md">Report bug</a>
    ·
    <a href="https://github.com/IsmaelBortoluzzi/Survey-Maker-API/issues/new?template=feature.md&labels=feature">Request feature</a>
  </p>
</p>

## Table of contents

- [What Is This Project](#what-is-this-project)
- [Starting](#starting)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## What Is This Project?

This is an application created to conduct surveys for researches, like google forms.
Reports are easy to be implemented in the future, mainly due to the 
concise database schema of the surveys and answered surveys. The authentication
method is JWT


## Starting 
Linux OS:

- for building the databases and mongo-express manager for development: 

      $ docker-compose -f docker-compose-dev.yml up -d
- for building the databases and mongo-express manager for production: 

      $ docker-compose -f docker-compose-prod.yml up -d
- creating the venv

      $ python3 -m venv venv
- activate venv

      $ source /bin/activate
- install requirements

      $ pip install -r requirements.txt
- migrate the relational database

      $ python manage.py migrate
- run server local

      $ python manage.py runserver

Don't forget to create your own .env based on the .env-example file
Note that the development docker only serve the databases and mongo-express, 
you need to connect to them with the application running locally.
The production docker is ready for use on default port 80
The production docker will work only with DEBUG=0 and the dev one
with DEBUG=1


## Endpoints

You can find all the endpoints in the file ENDPOINTS.md, as well as a postman export file
with a usage of each endpoint. Don't forget to insert the city_inserts and to import
the postman_export_for_testing.json in your local Postman for test


#### Setting Up JWT Token In Postman:

first, get an access token, then click the root directory, go to Authorization, 
select "Bearer Token" and past your access token in the "Token" field. Postman
will generate the correct header for every request.

#### Creating A Survey:

Only authors can create surveys and to make a user an author, you must do it
using django admin interface with a superuser


## Contributing

If you wish to contribute to the project, you can submit your pull request, which will be validated and merged as soon as possible, or open an issue.

## Creators

**Ismael Bortoluzzi**

- <https://github.com/IsmaelBortoluzzi>

## Thanks

Thank you for taking a look at my project!

## Copyright and license

Code released under the [freeBSD License](https://github.com/IsmaelBortoluzzi/Survey-Maker-API/blob/master/LICENSE.md).

Enjoy
