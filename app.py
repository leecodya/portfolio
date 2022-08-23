from flask import Flask, render_template

app = Flask(__name__)
my_name = "Cody Lee"

@app.route("/")
def home():
    return render_template("home.htm", name_title = my_name)

@app.route("/about")
def about():
    return render_template("about.htm", name_title = my_name)

@app.route("/projects")
def projects():
    return render_template("projects.htm", name_title = my_name)

@app.route("/services")
def services():
    return render_template("services.htm", name_title = my_name)

@app.route("/contact")
def contact():
    return render_template("contact.htm", name_title = my_name)

if __name__ == "__main__":
    app.run()