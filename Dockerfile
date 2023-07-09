#
FROM python:3.9.10

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./thumb_app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
