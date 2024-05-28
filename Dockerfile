FROM gitpod/workspace-full

# Install Airflow dependencies
RUN pip install apache-airflow==2.8.2

# FROM apache/airflow:2.8.2
# COPY requirements.txt /requirements.txt
# RUN pip install --user --upgrade pip
# RUN pip install --no-cache-dir --user -r /requirements.txt
 