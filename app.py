from flask import Flask

app=Flask("__name__")

@app.route("/")
def index():
    return "flask app is working(github version)ie through github repo"

if __name__ == "__main__":
    app.run()
