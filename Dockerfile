FROM python:latest

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# install all the requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 8080 for the Flask app to run on
EXPOSE 8080

# execute the Flask app
CMD ["python", "app.py"]