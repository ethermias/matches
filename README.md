# matches

# TDD
https://testdriven.io/blog/fastapi-crud/

## Create Folder Structure 
mkdir backend
mkdir backend/app backend/tests
mkdir backend/app/api backend/app/core
touch .flake8 .gitignore docker-compose.yml README.md
touch backend/.env backend/Dockerfile backend/requirements.txt

Not too bad. We’ll add more in a minute, but for now only four packages:

fastapi - the framework we’re using to build this backend
uvicorn - the ASGI server we’ll use to serve up our app
pydantic - validation library baked into fastapi that we’ll use to handle data models at different stages throughout our application
email-validator - allows pydantic to validate emails

A few interesting things going on here. We have a factory function that returns a FastAPI app with cors middleware configured. Don’t worry too much about the cors stuff - this is a rabbit hole that I don’t feel like diving into at the moment. If you want to read more, MDN has some great docs on it.

You’ll also notice we’re importing this middleware from the starlette package. FastAPI is built on top of starlette, and we’ll occasionally dip into the underlying architecture to accomplish a few things. Just a heads up. You don’t need to worry too much about this either, but feel free to checkout the docs here if you want to learn more.

A few things going on here

We’re setting up our first service - server - and telling it to build using the Dockerfile we just defined.
We’re saving the backend files to volume. More on this later.
We’ll serve up our application with uvicorn, and host the backend on localhost:8000.
All other environment variables will be taken from our .env file.
And finally - lets build our docker container and get our server up and running.

https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c

url1 = "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/teams/"
