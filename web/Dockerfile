FROM openjdk:20
FROM python:latest

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHOUNBEFFERED 1

WORKDIR /web

RUN pip install --upgrade pip
#Необходимые пакеты для установки в виртуальную среду докера
COPY DevBlog_new/requrements.txt .
RUN pip install -r requrements.txt
COPY . .
#Переносим исправленный пакет гугла
COPY DevBlog_new/other_module/google_translate /usr/local/lib/python3.12/site-packages/google_translate

EXPOSE 8000