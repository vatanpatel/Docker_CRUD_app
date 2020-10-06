<<<<<<< HEAD
# Greendeck Task1

1. Download and install  [Docker](https://www.docker.com/get-started).

#

2. Navigate to directory and git clone this repo there:
    ```bash
    $ git clone https://github.com/vatanpatel/greendeck_task1.git
    $ cd greendeck_task1
    ```

#

3. Build a docker at the same location as Dockerfile (This might take a while):
    ```bash
    $ docker build -t green .
    ```

#

4. Run the docker at localhost:5000/:
    ```bash
    $ docker run -p 5000:5000 green
    ```
    And that's it! we are up and running @ localhost/5000/
#

5. Give a request to the server. You can use __Postman__ app @ localhost:5000/:
    
    __See the opening screen (*home.html*)__
    ```bash
    GET /
    ```

    __Post (Add) a data to database:__ 
    ```bash
    POST /data
    body request: {"name":"a", "brand_name":"b", "regular_price_value": "12", "offer_price_value": "32", "currency": "CAG", "classification_l1": "a", "classification_l2": "b", "classification_l3": "c", "classification_l4": "d", "image_url": "https://"}
    ```
    __Get all data & specific data by id:__
    ```bash
    GET /data
    GET /data/100
    ```
    __Update a data by id__:
    ```bash
    PUT /data/{:id}
    body request: {"name":"a", "brand_name":"b", "regular_price_value": "12", "offer_price_value": "32", "currency": "CAG", "classification_l1": "a", "classification_l2": "b", "classification_l3": "c", "classification_l4": "d", "image_url": "https://"}
    ```
    __Delete a data by id:__
    ```bash
    DELETE /data/100
    ```

#

=======
1. install docker
2. navigate to directory and git pull this repo there
3. docker build -t green .
4. docker run -p 5000:5000 green


database connection:
install postgresql-client

psql -W -U sgpostgres -p 5432 -h SG-task-1109-pgsql-master.servers.mongodirector.com -d postgres

username password in https://console.scalegrid.io/postgresqlclusters/1109/clusterDetails
to test entries in table, once logged in then type:
 
1. /c green
2. SELECT * from products;
>>>>>>> dbb03528676a74edf4871b39e9c6c0fdb1962004
