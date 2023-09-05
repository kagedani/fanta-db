FROM continuumio/miniconda3

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Create the environment:
COPY ./env.yaml .
RUN conda env update -f ./env.yaml -n base

COPY ./../../build .

# The code to run when container is started:
# ENTRYPOINT ["python3", "main.py", "&"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]
