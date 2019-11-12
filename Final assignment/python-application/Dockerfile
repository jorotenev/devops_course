FROM kennethreitz/pipenv@sha256:e5ee93444c52f36791f799e611d01b6950d819c676723a13c160a918c7f2d786
COPY . /app
WORKDIR /app
EXPOSE 5000
EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0"]