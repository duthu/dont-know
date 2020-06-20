from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hello345678900'
app.permanent_session_lifetime = timedelta(minutes=3)
@app.route("/")
def home():
	return render_template("index.html")
	flash("hello welcome to the home page!" "info")

@app.route("/login", methods=["POST", "GET"]) 
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		if user == "hh":
			import pyttsx3 as speech
			engine = speech.init()
			rate = engine.getProperty('rate')
			engine.setProperty('rate', 175)
			engine.say("hallo Griffin. how have you been?")
			engine.runAndWait()
			return "welcome back"

		return redirect(url_for("user"))
	else:
		return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return f"<h1>{user}</hl>"
	else:
		return redirect(url_for("login"))
@app.route("/logout")
def logout():
	session.pop("user", None)
	flash("you have been logged out!", "info")
	return render_template("login.html")
if __name__ == "__main__":
	app.run(debug=True)