# Tutorial

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
