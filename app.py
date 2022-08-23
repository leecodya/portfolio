from flask import Flask, render_template

app = Flask(__name__)
my_name = "Cody Lee"

@app.route("/")
def home():
    return render_template("home.htm", name_title = my_name)

if __name__ == "__main__":
    app.run()