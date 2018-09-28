# fast food fast API

[![Build Status](https://travis-ci.com/unah254/FFF.svg?branch=ft-test-models)](https://travis-ci.com/unah254/FFF)      [![Maintainability](https://api.codeclimate.com/v1/badges/2381ed78f4521ea137e7/maintainability)](https://codeclimate.com/github/unah254/FFF/maintainability)   [![Coverage Status](https://coveralls.io/repos/github/unah254/FFF/badge.svg)](https://coveralls.io/github/unah254/FFF)
 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3ea9993eaae9495ba0a2f080163727d1)](https://www.codacy.com/app/unah254/FFF?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=unah254/FFF&amp;utm_campaign=Badge_Grade)

# API Documentation
https://documenter.getpostman.com/view/5299590/RWaRNkLr

# Heroku link
https://fastfoodapp-api-heroku.herokuapp.com



# API Endpoints

| EndPoint                  | Functionality                 |
| --------------------------| ------------------------------|
| api/v1/orders             | Get all the orders.           |
| api/v1/order/Id           | Fetch a specific order        |
| api/v1/order              | Place a new order.            |
| api/v1/orders/Id          | Update the status of an order.|
| api/v1/order/Id           | Delete a specific order.      |

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
# Testing
```
$ python -m pytest
```






