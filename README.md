# Data pre/processing for Academic Arborist

## Synopsis

This repo contains the data processing pipeline used to process the input data
for Academic Arborist so that it can be used with the Watson sentiment analysis
service.

This program uses `chromedriver` to parse reviews from the course assessment
portal, and it saves the data to a JSON file with the following schema:

- Each key is a tuple consisting of the (professor's first name, professor's
  last name)
- Each value is a list of strings which are the reviews that were collected for
  that professor

## Development

Create a virtual environment with

```sh
python -m venv .venv
```

activate it:

```sh
source .venv/bin/activate[.sh|.fish]
```

Install dependencies with:

```sh
pip install -r requirements.txt
```

Run the main script:

```sh
python main.py reviews.html
```
