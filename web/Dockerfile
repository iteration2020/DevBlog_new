FROM openjdk:20
FROM python:3.10

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHOUNBEFFERED 1

WORKDIR /web

RUN pip install --upgrade pip
#Необходимые пакеты для установки в виртуальную среду докера
COPY DevBlog_new/requrements.txt .
RUN pip install -r requrements.txt
COPY . .

EXPOSE 8000