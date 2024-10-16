from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input from the form
        user_name = request.form.get("name")
        user_age = request.form.get("age")


        return render_template("index.html", name=user_name, age=user_age)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
