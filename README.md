# Data pre/processing for Academic Arborist

## Synopsis

This repo contains the data processing pipeline used to process the input data
for Academic Arborist so that it can be used with the Watson sentiment analysis
service.

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
