#This software will run a very basic flask program capable of running a simple web application
#Imports flask and sets the variable "app" for later use for debug mode.
from flask import Flask, render_template


app = Flask(__name__, template_folder="Web_Templates")
#no clue what this does.
@app.route("/")

def home():
    return render_template("MainPage.html")
app.route("/aboutpage")
def about():
    return render_template("AboutPage.html")






#This will run the app identified as flask from earlier.
if __name__ == "__main__":
    app.run(debug=True)