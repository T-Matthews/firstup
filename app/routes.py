from app import app


@app.route('/')
def home():
    greeting = 'Hello Foxes!'
    print(greeting)
    return 'Hello World!'