FROM puckel/docker-airflow:2.0.0
COPY dags /usr/local/airflow/dags
# RUN pip install <packages> ...