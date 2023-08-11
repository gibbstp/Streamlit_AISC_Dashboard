FROM python:3.10-bullseye

RUN apt-get update && \
    apt-get update -y && \
    pip install --upgrade pip && \
    curl -sSL https://install.python-poetry.org | python3 - 
    
ENV PATH="${PATH}:/root/.local/bin" \
    POETRY_HOME="/home/poetry" \    
    POETRY_VIRTUALENVS_CREATE=false

RUN poetry self update

WORKDIR /app

COPY pyproject.toml ./

RUN poetry install
#RUN poetry export --output requirements.txt --dev --without-hashes && \
#    pip install -r requirements.txtpwd
