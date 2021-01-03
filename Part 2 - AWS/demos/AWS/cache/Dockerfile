FROM python:3.7
RUN pip install flask redis-py boto3
COPY . /app
WORKDIR /app
ENV FLASK_APP=main
CMD ['flask', 'run']

# docker run myflaskapp -p 5000:5000