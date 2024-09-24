FROM python:3.12-bookworm
LABEL authors="dug"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN apt-get update && apt-get install -y \
    libsqlite3-mod-spatialite
COPY app app
COPY migrations migrations
COPY setup setup
COPY wof_datasets wof_datasets
COPY config.py setup.py locality_configs.yml boot.sh swagger.yml routes.py ./
RUN chmod a+x boot.sh


EXPOSE 5000
ENTRYPOINT ["./boot.sh"]