# fast food fast API

[![Build Status](https://travis-ci.com/unah254/FFF.svg?branch=ft-test-models)](https://travis-ci.com/unah254/FFF)      [![Maintainability](https://api.codeclimate.com/v1/badges/2381ed78f4521ea137e7/maintainability)](https://codeclimate.com/github/unah254/FFF/maintainability)
<a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a>    [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3ea9993eaae9495ba0a2f080163727d1)](https://www.codacy.com/app/unah254/FFF?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=unah254/FFF&amp;utm_campaign=Badge_Grade)

# API Endpoints

| EndPoint              | Functionality                 |
| ----------------------| ------------------------------|
| GET /orders           | Get all the orders.           |
| GET /orders/<orderId> | Fetch a specific order        |
| POST /orders          | Place a new order.            |
| PUT /orders/<orderId> | Update the status of an order.|
| PUT /orders/<orderId> | Delete a specific order.      |

# Prerequisites
1.Python 3: https://www.python.org/downloads/                                        
2.Flask_restful: https://flask-restful.readthedocs.io/en/latest/installation.html
# Running app
```
$ virtualenv env
$ cd env
$ git clone https://github.com/unah254/FFF.git
$ source env/bin/activate
$ cd FFF
$ export APP_SETTINGS=development
$ python run.py

```





