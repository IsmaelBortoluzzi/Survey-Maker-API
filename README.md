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
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## What Is This Project?

This is an application created to conduct surveys for researches, like google forms.
Reports are easy to be implemented in the future, mainly due to the 
concise database schema of the surveys and answered surveys.


## Starting 
Linux OS:

- for building the databases and mongo-express manager: 

      $ docker-compose up -d
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


## Contributing

If you wish to contribute to the project, you can submit your pull request, which will be validated and merged as soon as possible, or open an issue.

## Creators

**Ismael Bortoluzzi**

- <https://github.com/IsmaelBortoluzzi>

## Thanks

Thank you for taking a look at my project!

## Copyright and license

Code released under the [MIT License](https://github.com/IsmaelBortoluzzi/Risc-V-Interpreter/blob/master/LICENSE).

Enjoy
