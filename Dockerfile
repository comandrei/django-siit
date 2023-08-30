FROM python:3.11
RUN apt-get update && apt-get install build-essential graphviz graphviz-dev --assume-yes
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
COPY sample_project app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0:8000" ]