from backend.app import create_app

app = create_app(False)

@app.route("/")
def home():
    return "Welcome"


if __name__ == "__main__":
    app.run(debug=True)
