FROM openjdk:20
FROM python:3.11

ARG MLFLOW_TRACKING_DIRECTORY
ENV MLFLOW_TRACKING_DIRECTORY=${MLFLOW_TRACKING_DIRECTORY}
ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHOUNBEFFERED 1

WORKDIR /web

RUN pip install --upgrade pip
#Необходимые пакеты для установки в виртуальную среду докера
COPY DevBlog_new/requrements.txt .
RUN pip install -r requrements.txt
RUN pip install mlflow
COPY . .
COPY ml/model/MLOps_drug_predict.ipynb /web/mlruns/

EXPOSE 8000

CMD mlflow server \
    --backend-store-uri ${MLFLOW_TRACKING_DIRECTORY}/tracking \
    --default-artifact-root ${MLFLOW_TRACKING_DIRECTORY}/artifacts \
    --host 0.0.0.0

EXPOSE 5000