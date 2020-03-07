# Daily Currency Rates

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e5c7140930924a0286ec56dcd7d3c867)](https://app.codacy.com/manual/metin_akin_bursa/currency-rates?utm_source=github.com&utm_medium=referral&utm_content=akinmetin/currency-rates&utm_campaign=Badge_Grade_Settings)

Python project for getting daily currency rate informations for EUR using Postgres & Docker containerization.

## Getting Started

These instructions will get you a copy of the project up and running on a docker container for development and testing purposes.

### High level requirements

*   Use the ``fixer.io`` API to ingest currency rates.
*   Have the ingest & store procedure run daily at 9:00AM.
*   Ingest and store rates for all days except weekends.
*   Ensure the system holds at least the last month of rates information.
*   Use Postgres database for storing data.

### Technical requrements

*   Explain every possible functions, calls etc.
*   Use Python version 3.6+.
*   Use docker for containerization.

### Prerequisites

``Docker``

### Installing

*   Download this repository and extract it to any folder.

*   Build it using ``docker-compose build`` and run it using ``docker-compose up -d``.

*   You can also run python script inside the container using: ``docker-compose run app python currency_rates.py``.

*   Create an ``.env`` file for environmental variables.

*   Environmental Variables
    *   ``API_ENDPOINT``: Complete GET http request.
    *   ``API_KEY``: API key for service authentication.
    *   ``DB_NAME``: Database name for Postgres database server.
    *   ``DB_USER``: Database username for Postgres database server.
    *   ``DB_PASSWORD``: Database username for Postgres database server.
    *   ``DB_HOST``: Hostname or ip of Postgres database server.
    *   ``DB_PORT``: Port of Postgres database server.

## Versioning

| Version       | Date            | Changes                                       |
| ------------- |:---------------:|:--------------------------------------------- |
| v1.0.0        | 05/03/2020      | Initial development                           |
| v1.1.0        | 06/03/2020      | Added some more features and cleaned the code |

## Licensing

All types usage of this project is required permission from owner of the repository.

## Useful Resources

*   [fixer.io quickstart](https://fixer.io/quickstart)
*   [fixer.io documentation](https://fixer.io/documentation)
*   [python api tutorial for beginners](https://www.dataquest.io/blog/python-api-tutorial/)
*   [python get time](https://tecadmin.net/get-current-date-time-python/)
*   [python postgresql](https://stackabuse.com/working-with-postgresql-in-python/)
*   [python postgres check table if exists](https://stackoverflow.com/questions/1874113/checking-if-a-postgresql-table-exists-under-python-and-probably-psycopg2)
*   [postgres data types (postgres float)](https://www.postgresqltutorial.com/postgresql-data-types/)
*   [python get number of days in month](https://stackoverflow.com/questions/4938429/how-do-we-determine-the-number-of-days-for-a-given-month-in-python)