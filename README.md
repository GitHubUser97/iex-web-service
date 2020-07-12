# IEX Web Service

This service provides a REST and Websocket interface to retrieve and stream the IEX historic data.

## Installation

```
We need to fill in these details after.
```

## Usage

Install the requirements
```bash
pip install -r requirements.txt
```

Prepare the database and migrations

```bash
flask db migrate
python manage.py db migrate
python manage.py db upgrade
```

## Run the service
```bash
python manage.py runserver
```

## Endpoints

- /api/health_check (GET) - Gives health status of the service.

## Links of interest

IEX Developer Api: https://iextrading.com/developers/docs/

## Contributing

Pick a issue/task from the issues pane and submit a pull reuqest.

## License
[MIT](https://choosealicense.com/licenses/mit/)
