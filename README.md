# Welcome
Our task is to create a REST API using Python and host it locally using Docker.
We will be working on two of the most important concepts of software engineering for this task. APIs and Containerization.

We have a customer for which we have dump of 5000 products in JSON format. These products are sold on their E-Commerce platform. The data contains the product name, price and other information. The goal of this task is to allow the user to interact with a database of products using APIs which are available on localhost via Docker.

We have a CSV file. It is a list of ~5000 e-commerce products and its information.
We host the data on cloud as postgresql database.
We create an API that allows the user to do basic CRUD operations on the data.
The user can Create new objects, Read the data, Update or Delete the objects in the database you selected before.
We then Dockerize our REST API application. The docker run command would deploy the API on localhost at a 5000 port. The user can then use the API endpoints to perform CRUD operations.
We also test the endpoints using Postman or Curl and share screenshots.


### How to use:

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

    And that's it! we are up and running @ localhost:5000/
#

5. To give a request to the server, You can use __Postman__ app @ localhost:5000/:
    
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
    PUT /data/100
    body request: {"name":"a", "brand_name":"b", "regular_price_value": "12", "offer_price_value": "32", "currency": "CAG", "classification_l1": "a", "classification_l2": "b", "classification_l3": "c", "classification_l4": "d", "image_url": "https://"}
    ```

    __Delete a data by id:__

    ```bash
    DELETE /data/100
    ```

#
### Screenshots

[![Step 1: Get All Products](https://ibb.co/m9wvNMS)](https://ibb.co/m9wvNMS)

#

[![Step 2: Add data using Post](https://ibb.co/X2SHZtF)](https://ibb.co/X2SHZtF)

#

[![Step 3: Check if the data is added](https://ibb.co/9hCL43m)](https://ibb.co/9hCL43m)

#

[![Step 4: Delete the newly created data](https://ibb.co/2n8H2cB)](https://ibb.co/2n8H2cB)

#

[![Step 5: Check if update is made](https://ibb.co/1X7PPMT)](https://ibb.co/1X7PPMT)

#

[![Step 6: Delete the newly created data](https://ibb.co/whQp5cB)](https://ibb.co/whQp5cB)

#

[![Step 7: Check if the data is deleted](https://ibb.co/SwWcHk9)](https://ibb.co/SwWcHk9)

#
#
