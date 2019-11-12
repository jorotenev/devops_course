# Tails task - backend
- The first task of showing the `stores.json` + their coordinates is in `app.pages.views.index_stores` (business logic in `app.stores.static`)
    - available at [http://tails-task.tenev.tech/](http://tails-task.tenev.tech/)
- The second task with the radius search is in `app.api.views` (business logic in `app.stores.radius_search`)
    - available via GET [http://tails-task.tenev.tech/api/radius/AL11RJ/1000](http://tails-task.tenev.tech/api/radius/AL12RJ/10000) 
    - `/api/<postcode>/<int:radius>`
    - radius is in meters
    - response is `application/json`
## Comments about the solution
* I've added a memoization decorator - so that requests to the `postcodes.io` are cached
    * it's implemented in `app.helpers.memoize` and tested in `tests.test_helpers.test_memoization`
    * it's a simple implementation using an in-memory cache based on the md5 sum of the request
    * the cache expires after a configurable amount of time
* For the radius search, it's needed to calculate the distance between two geolocations. The distance is calculated via [geopy's geodesic distance](https://geopy.readthedocs.io/en/stable/#geopy.distance.geodesic) 
* The solution uses a flask seed project that I maintain [here](https://github.com/jorotenev/flask_docker). The structure is influenced by the [work](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) of Miguel Grinberg.
    * In the current task's project I've made some modifications to the seed project which I will merge upstream :)
* The solution is hosted via AWS ECS Fargate (I used the Dockerfile to build an image and host it on ECR)
## Run
* Install [pipenv](https://github.com/pypa/pipenv#installation)
* `$ pipenv install # to create a venv & install packages`
* `$ pipenv shell # activate the venv`
* To run the flask app (see below the Note for PyCharm users)  
`$ flask run`

## To run with docker-compose
The `pipenv` image is used. Since there's only a `latest` tag, below I reference a specific [image build](https://hub.docker.com/r/kennethreitz/pipenv/builds/btyyzsg7po9kakddpc2lsrm/).
* `docker image pull kennethreitz/pipenv@sha256:e5ee93444c52f36791f799e611d01b6950d819c676723a13c160a918c7f2d786`
* `docker-compose up`

# Debug the app
* You need an `.env` file at the root of the repo with the following contents.   
  The `FLASK_RUN_x` env vars are optional.    
  Flask's built-in cli module will automatically pick up the `.env` and `.flaskenv` files for you.
    ```
    FLASK_ENV=development
    
    FLASK_RUN_HOST=0.0.0.0
    FLASK_RUN_PORT=8080
    ```  


* Alternatively, you can set the `FLASK_ENV` yourself in your shell and then just run `flask run`
#### Note for PyCharm users
* When running via PyCharm and assuming that pipenv is used, you need to select the correct Python [interpreter](https://www.jetbrains.com/help/pycharm/configuring-language-interpreter.html).
    ```
    $ pipenv shell
    (some_app-tKuPD0ya) $ which python
    /home/georgi/.local/share/virtualenvs/some_app-tKuPD0ya/bin/python
    ```

* When creating a run configuration, select as "Module name" (the default is to execute a script) `flask` and as Parameters `run`. For older versions of the IDE, see [this](https://stackoverflow.com/questions/22081065/create-a-pycharm-configuration-that-runs-a-module-a-la-python-m-foo)

## Test
Example for `unittest`.  
To run them via PyCharm
* You need the '.env_test' file placed in the repo root with the `FLASK_ENV=testing` env var  
* Create a new Python test run configuration with the `/tests` as the __Path__ target and the root of the repo as a working directory
