# Unsplash Thumbnails

Search and store thumbnails for free from unsplash images. Online images can be extremely large and slow to load. This is where a thumbnail creator can come in handy. A thumbnail creator can reduce the size of images, making it easier to access, and share.
## Prerequisites

Create a free Unsplash account and access the developers / API product. Create an app on the platform and copy the access key and paste it on the `.envexample`. Rename `.envexample` to `.env`

## Installation

Download the project, then create and activate virtual environment in the project directory

```shell
python -m venv venv
# on windows
./venv/Scripts/activate
# on unix
source venv/bin/activate
```

Install dependencies from `requirements.txt`

```shell
pip3 install -r requirements.txt
```

## Run the application

Run uvicorn server and connect to development enviroment `http://127.0.0.1:8000/`

```
uvicorn thumb_app.main:app --reload
```

## Overview
Here’s a summary of the thumbnail API endpoints:

| Endpoint              | HTTP Verb | Request Body    | Action                                                       |
| --------------------- | --------- | --------------- | ------------------------------------------------------------ |
| `/`                   | `GET`     |                 | Returns a `Welcome!` string                             |
| `/search`                | `POST`    | Search term and optionally color and orientation | Shows the created `thumbnail_key`  |
| `/{thumbnail_key}`          | `GET`     |                 | Shows thumbnail |

For easy API access open a browser on `http://127.0.0.1:8000/docs` and use the endpoints.

## Examples
#### Docs Page

![image-20220915170537097](./screenshots/image-20220915170537097.png)

#### Search Request
![image-20220915170755970](./screenshots/image-20220915170755970.png)
#### View Thumbnail

![image-20220915170856440](./screenshots/image-20220915170856440.png)

![image-20220915171150838](./screenshots/image-20220915171150838.png)
