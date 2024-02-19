# OneFin Backend Assignment 
It's an assignment task from OneFin

# Getting Started

### Installation Guide
* Clone the repo.
* Navigate to project directory
* Install pipenv if not installed already
* Run pipenv shell, it's activates Pipenv virtual environment
* pip install -r requirements.txt 
* python manange.py runserver
* Open your favourite browser and run http://localhost:8000/
* (OPTIONAL) Create your own an .env file in your project root folder and add your variables. See my .env for assistance.

### API Endpoints
| HTTP Verbs | Authentication | Endpoints | Action |
| --- | --- | --- | --- |
| POST | NO | /register/  | Register user and return JWT token |
| GET |  YES |/movies/  | To retrieve all movies from 3rd party api |
| GET |  YES |/collection/  | To retrieve all collections of authenticate user |
| POST | YES |/collection/  | To create new collection with provided movies |
| GET |  YES |/collection/:pk  | To retrieve details of a single collection |
| PUT |  YES |/collection/:pk  | To edit the details of a collection |
| DELETE | YES |/collection:pk  | To delete a collection |
| GET |  YES | /request-count/  | Return the total number of requests servered by the server |
| GET |  YES | /request-count/reset/  | Reset total requests servered by the server |


## Overview

This document provides detailed documentation for the OneFin-Assignment REST API. It includes information on how to interact with the API, available endpoints, request/response formats, authentication, and examples.

# Authenticate User's Collections Listview
<p align="center">
  <a href="https://shub.pythonanywhere.com/profile">
    <img alt="Responsive" src="https://raw.githubusercontent.com/Shubhansh-Simple/OneFin-Assignment/main/Screenshots/Collection-List-View.png" height="500" /> 
  </a>
</p>

<hr>

## Base URL

The base URL for all API endpoints is:

```
https://localhost:8000/collections/
```

## Authentication

OneFin-Assignment API uses JWT token-based authentication. To authenticate requests, include an `Authorization` header in the following format:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Available Endpoints

### 1. Endpoint 1

- **URL**: `/endpoint1`
- **Method**: `GET`
- **Description**: Description of what this endpoint does.
- **Parameters**:
  - `param1`: Description of parameter 1. *(Optional)*
- **Example Request**:
  ```http
  GET /endpoint1?param1=value1 HTTP/1.1
  Host: api.example.com
  Authorization: Bearer YOUR_ACCESS_TOKEN
  ```
- **Example Response**:
  ```json
  {
    "key": "value"
  }
  ```

### 2. Endpoint 2

- **URL**: `/endpoint2`
- **Method**: `POST`
- **Description**: Description of what this endpoint does.
- **Request Body**:
  ```json
  {
    "key": "value"
  }
  ```
- **Example Request**:
  ```http
  POST /endpoint2 HTTP/1.1
  Host: api.example.com
  Authorization: Bearer YOUR_ACCESS_TOKEN
  Content-Type: application/json

  {
    "key": "value"
  }
  ```
- **Example Response**:
  ```json
  {
    "message": "success"
  }
  ```

## Error Handling

The API returns standard HTTP status codes for errors. Error responses will include a JSON object with details about the error.

Example error response:

```json
{
  “movies”: [
    {
      “genres”: This field is required,
    },
  ]
}
```

<hr>

# Authenticate User's Collections Detailview
<p align="center">
  <a href="https://shub.pythonanywhere.com/profile">
    <img alt="Responsive" src="https://raw.githubusercontent.com/Shubhansh-Simple/OneFin-Assignment/main/Screenshots/Collection-Detail-View.png" height="500" /> 
  </a>
</p>

## Conclusion

This concludes the documentation for the OneFin-Assignment REST API. For any further assistance

