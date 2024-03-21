# matches

fastapi - the framework we’re using to build this backend
uvicorn - the ASGI server we’ll use to serve up our app
pydantic - validation library baked into fastapi that we’ll use to handle data models at different stages throughout our application
email-validator - allows pydantic to validate emails


A few interesting things going on here. We have a factory function that returns a FastAPI app with cors middleware configured. Don’t worry too much about the cors stuff - this is a rabbit hole that I don’t feel like diving into at the moment. If you want to read more, MDN has some great docs on it.

You’ll also notice we’re importing this middleware from the starlette package. FastAPI is built on top of starlette, and we’ll occasionally dip into the underlying architecture to accomplish a few things. Just a heads up. You don’t need to worry too much about this either, but feel free to checkout the docs here if you want to learn more.